package fig.record;

import fig.basic.*;
import java.io.*;
import java.util.*;

/**
 * A file consists of a path and a character offset into that file.
 * Assume all files are UTF8.
 */
public class FileRecordNode extends PathRecordNode {
  // The offset from the beginning of the file (see OffsetReader)
  private int offset;

  // Number of lines (number of descendent nodes in this file)
  // If this number is within state maxLoadSize, then we will load the entire subtree at once
  private int numLines = -1; // -1 means we don't know

  public FileRecordNode(LoadFileState state, String key, String value, File path, int offset) {
    super(state, key, value, path);
    this.offset = offset;
  }
  public FileRecordNode(LoadFileState state, File path, int offset) {
    super(state, path);
    this.offset = offset;
  }
  public FileRecordNode(LoadFileState state, File path) {
    super(state, path);
    this.offset = 0;
  }

  public int getOffset() { return offset; }

  // Return number of leading tabs
  private static int countIndent(String line) {
    int n = 0;
    while(n < line.length() && line.charAt(n) == '\t') n++;
    return n;
  }
  static Random rand = new Random();

  public void loadChildren() {
    clearChildren();

    int maxIndent = Integer.MAX_VALUE; // How deep we're going to load
    // Just load children (but not their children) if this node has too many
    // lines or we don't know how many lines there are
    if(numLines == -1 || numLines > state.getMaxLoadSize()) maxIndent = 0;

    try {
      boolean alreadyOpened = state.alreadyOpened(getPath());
      OffsetReader in = state.getReader(getPath(), getOffset());

      if(state.verbose(1) && !alreadyOpened)
        state.getReceiver().printErr(
            String.format("Loading %s:%d", getPath(), getOffset()));

      // Stack is the sequence of nodes from root to current node plus an empty slot
      List<FullRecordNode> stack = new ArrayList<FullRecordNode>();
      stack.add(this); stack.add(null);

      String[] currStructKeys = null; // Applies as long as indent doesn't change
      int currLineNum = 0;
      int rootIndent = 0;
      FileRecordNode lastNode = null; // Last node created
      int lastNodeLineNum = -1; // Line of the last node created
      boolean warnedAboutZeros = false;
      while(true) {
        // Read the current line and peek at the next line
        String currLine = in.readLine();
        if(currLine == null) break;
        // Sometimes files written over the network end up with lots of zeros in them,
        // these usually get fixed later, but we want to be able to just ignore those lines
        if(currLine.indexOf(0) != -1) {
          if(!warnedAboutZeros)
            state.getReceiver().printErr(
              String.format("Got a bunch of zeros at line " + (currLineNum+1) + " in file " + getPath() +
                "; skipping line; this should be fixed when the file is flushed\n"));
          warnedAboutZeros = true;
          continue;
        }
        String nextLine = in.peekNextLine();

        // Figure out indent
        int currIndent = countIndent(currLine);
        if(currLineNum == 0) rootIndent = currIndent; // If first line, this is the basis of our indent
        currIndent -= rootIndent; // Adjustment

        if(currIndent < 0) break; // We're done loading
        if(currIndent <= maxIndent) { // Load if we're not going too deep
          int prevIndent = stack.size()-2; // Previous indent
          int nextIndent = nextLine == null ? 0 : countIndent(nextLine) - rootIndent;
          boolean currHasChildren = nextIndent > currIndent;

          // Disable the .struct mechanism if current node has children
          if(currHasChildren) currStructKeys = null;

          // Get the key, value
          String key = null, value = null;
          String[] values = null; // Used if we're in the struct node
          int startKeyPosition = currIndent + rootIndent;
          currLine = currLine.substring(startKeyPosition); // Remove indent
          if(currStructKeys == null || currLine.startsWith(".struct")) { 
            // Read <key>\t<value>
            int sep = currLine.indexOf('\t');
            if(sep == -1) sep = currLine.length();
            key = currLine.substring(0, sep).intern();
            value = (sep+1 < currLine.length() ? currLine.substring(sep+1) : null);
          }
          else {
            // We're in the .struct mode, so this line isn't key, value pair,
            // but just a set of values for the struct node
            values = StrUtils.split(currLine, "\t");
          }

          // Indent: update the stack
          if(currIndent > prevIndent+1)
            throw new RuntimeException("Invalid jump from indent " + prevIndent + " to " + currIndent + " at line " + (currLineNum+1) + " in " + getPath()+":"+in.getOffset());
          for(int i = prevIndent; i < currIndent; i++) stack.add(null);
          for(int i = prevIndent; i > currIndent; i--) stack.remove(stack.size()-1);

          if(".struct".equals(key)) {
            // This is a special (key, value) pair
            // Set the current structure
            if(value == null)
              currStructKeys = null; // Disable keys
            else
              currStructKeys = StrUtils.split(value, "\t");
          }
          else {
            // Create a new node
            FullRecordNode parent = stack.get(stack.size()-2);
            RecordNode node;
            if(currStructKeys != null)
              node = new StructRecordNode(currStructKeys, values);
            else if(!currHasChildren) {
              // Set special nested files
              if(key.equals(".dir"))
                node = new DirRecordNode(state, new File(value));
              else if(key.equals(".file")) {
                String[] pathOffset = StrUtils.split(value, "\t");
                node = new FileRecordNode(state,
                    new File(pathOffset[0]),
                    Utils.parseIntHard(pathOffset[1]));
              }
              else if(key.equals(".array")) {
                // As if we had many <key>\t<value> lines
                // Format: .array\t<key>\t<value1>\t<value2>...
                values = StrUtils.split(value, "\t");
                key = values[0];
                node = null;
                for(int j = 1; j < values.length; j++) {
                  value = values[j];
                  node = new LeafRecordNode(key, value);
                  // Save the last one for adding later
                  if(j < values.length-1) parent.addChild(node);
                }
              }
              else {
                node = new LeafRecordNode(key, value);
              }
            }
            else if(currIndent == maxIndent) {
              // Set number of lines of last created file node
              if(lastNode != null) lastNode.numLines = currLineNum - lastNodeLineNum;

              // This node has children, but we're already at maxIndent, so
              // make a pointer to the file instead of loading it
              //System.out.println("CREATE " + key + " " + in.getOffset());
              node = lastNode =
                new FileRecordNode(state, key, value, getPath(), in.getOffset());
              lastNodeLineNum = currLineNum+1; // Location of children
            }
            else {
              node = new FullRecordNode(key, value);
              stack.set(stack.size()-1, (FullRecordNode)node);
            }
            if(node != null) parent.addChild(node);
          }

          // Disable structure once we're done with that level
          if(nextIndent < currIndent) currStructKeys = null;
        }

        // Increment line number
        currLineNum++;
        if(state.verbose(1) && !alreadyOpened && currLineNum % 10000 == 0)
          state.getReceiver().printErr(".");
      }

      // Set number of lines of last created file node
      if(lastNode != null) lastNode.numLines = currLineNum - lastNodeLineNum;

      // Make the number of lines we just loaded is equal to what
      // we were told before
      // File could have changed, which is why we're reloading
      /*if(numLines != -1 && numLines != currLineNum)
        throw new RuntimeException(String.format(
          "Mis-match: got numLines=%d before, now read currLineNum=%d", numLines, currLineNum));*/
      numLines = currLineNum;

      if(state.verbose(1) && !alreadyOpened)
        state.getReceiver().printErr("\n");
    } catch(IOException e) {
      throw new RuntimeException(e);
    }

    super.loadChildren();
  }

  public boolean outOfDate() {
    // Nested files should not check loading status, otherwise
    // we're going to thrash the disk with senseless requests;
    // Leave this job to the file node with offset 0
    if(offset != 0) return lastLoadedTime == 0; // Just check if have loaded before
    return super.outOfDate();
  }

  public RecordNode shallowCopy(String key, String value) {
    FileRecordNode node = new FileRecordNode(state, key, value, getPath(), getOffset());
    node.setChildren(getChildren());
    return node;
  }
  public RecordNode withoutChildren() {
    return new FileRecordNode(state, getKey(), getValue(), getPath(), getOffset()).disableLoading();
  }

  public String getDescription(RecordNode.DescriptionType type) {
    if(type == RecordNode.DescriptionType.human)
      return super.getDescription(type) +
        (isChildrenLoaded() ? "" :
          (numLines == -1 ? " ..." : " ("+numLines+" lines)"));
    else
      return ".file\t" + getPath() + "\t" + getOffset() +
        (getValue() == null ? "" : "\t"+getValue());
  }
}
