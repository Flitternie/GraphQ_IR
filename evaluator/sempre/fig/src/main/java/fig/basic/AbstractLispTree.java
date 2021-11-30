package fig.basic;

import java.io.*;
import java.util.*;

// LispTree is either a string value or children (list of LispTrees).
// Override newTree() to make this a concrete class.
public abstract class AbstractLispTree<TreeType extends AbstractLispTree> implements MemUsage.Instrumented {
  public String value;  // Only for leaf
  public List<TreeType> children;  // Only for non-leaves

  public boolean isLeaf() { return children == null; }
  public TreeType child(int i) { return children.get(i); }
  public TreeType addChild(TreeType tree) { children.add(tree); return (TreeType)this; }
  public TreeType addChild(String value) { addChild(newLeaf(value)); return (TreeType)this; }

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize * 2) +
           8 +  // Unexplained
           MemUsage.getBytes(value) +
           MemUsage.getBytes(children);
  }

  public int numLeaves() {
    if (isLeaf()) return 1;
    int n = 0;
    for (TreeType arg : children)
      n += arg.numLeaves();
    return n;
  }
  public int numNodes() {
    if (isLeaf()) return 1;
    int n = 1;
    for (TreeType arg : children)
      n += arg.numNodes();
    return n;
  }

  // List operation (inefficient right now)
  public TreeType head() { return child(0); }
  public TreeType tail() {
    TreeType result = newTree();
    result.children = children.subList(1, children.size());
    return result;
  }
  public TreeType cons(TreeType tail) {
    TreeType result = newList();
    result.addChild(this);
    for (TreeType x : (List<TreeType>)tail.children)
      result.addChild(x);
    return result;
  }

  //// Factory methods: create new instances

  protected abstract TreeType newTree();

  public TreeType newLeaf(String value) {
    TreeType tree = newTree();
    tree.value = value;
    return tree;
  }
  public TreeType newList() {
    TreeType tree = newTree();
    tree.children = new ArrayList<TreeType>();
    return tree;
  }
  public <K,V> TreeType newList(Map<K,V> items) { TreeType tree = newList(); for (Map.Entry<K,V> e : items.entrySet()) tree.addChild(newList(e.getKey()+"", e.getValue()+"")); return tree; }
  public <T> TreeType newList(List<T> items) { TreeType tree = newList(); for (T x : items) tree.addChild(x+""); return tree; }
  public TreeType newList(String t1, String t2) { TreeType tree = newList(); tree.addChild(t1); tree.addChild(t2); return tree; }
  public TreeType newList(String t1, TreeType t2) { TreeType tree = newList(); tree.addChild(t1); tree.addChild(t2); return tree; }
  public TreeType newList(TreeType t1, String t2) { TreeType tree = newList(); tree.addChild(t1); tree.addChild(t2); return tree; }
  public TreeType newList(TreeType t1, TreeType t2) { TreeType tree = newList(); tree.addChild(t1); tree.addChild(t2); return tree; }

  // Shortcut for creating lists (convert objects to strings)
  public TreeType L(Object... items) {
    TreeType tree = newList();
    for (Object item : items) {
      if (item instanceof AbstractLispTree) tree.addChild((TreeType)item);
      else if (item == null) tree.addChild(newLeaf(null));
      else tree.addChild(item.toString());
    }
    return tree;
  }

  public TreeType convert(AbstractLispTree tree) {
    if (tree.isLeaf()) {
      return newLeaf(tree.value);
    } else {
      TreeType result = newList();
      for (AbstractLispTree child : (List<AbstractLispTree>)tree.children)
        result.addChild(convert(child));
      return result;
    }
  }

  static class ParseLispTreeIterator<TreeType extends AbstractLispTree> implements Iterator<TreeType> {
    public ParseLispTreeIterator(BufferedReader reader, TreeType proto) {
      this.reader = reader;
      this.proto = proto;
      advance();  // Initialize
    }

    public void remove() { }
    public boolean hasNext() {
      skipSpace();
      return c != 0;
    }
    public TreeType next() {
      start_line_num = line_num;
      start_i = i;
      return recurse();
    }
    
    private TreeType proto;
    private BufferedReader reader;
    private int start_line_num = -1, start_i = -1;  // Where we were when we started this madness
    private int line_num = 0;  // Current line
    private String line = null;  // Current line
    private int i = -1;  // Current position in line
    private int n = 0;  // Length of line
    private char c = 0;  // Current character

    // Invariant after first advance: we're sitting on a character
    private void error(String msg) {
      throw new RuntimeException(String.format("%s from %s:%s to %s:%s", msg, start_line_num, start_i, line_num, i));
    }

    // Move one character
    private void advance() {
      i++;
      // If exhausted line, then go to next
      while (i == n) {
        try {
          line = reader.readLine();
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
        if (line == null) {
          i = n = 0;
          break;
        }
        line += "\n";
        line_num++;
        n = line.length();
        i = 0;
      }
      c = (line == null ? 0 : line.charAt(i));
    }

    private void skipSpace() {
      while (c != 0) {
        if (c == '#') {  // Comment: Ignore to the end of the line
          while (c != 0 && c != '\n') advance();
        } else if (Character.isWhitespace(c)) {  // Whitespace
          advance();
        } else {  // Regular character
          break;
        }
      }
    }

    // Consume a LispTree and return it
    private TreeType recurse() {
      skipSpace();
      if (c == 0)  // Nothing
        return null;
      else if (c == '(') {  // List
        advance();
        TreeType tree = (TreeType)proto.newList();
        while (true) {
          skipSpace();
          if (c == 0) {
            error("Missing ')'");
          } else if (c == ')') {  // End
            advance();
            break;
          }
          tree.addChild(recurse());
        }
        return tree;
      } else {  // Primitive
        if (c == ')') error("Extra ')'");
        boolean escaped = false;
        boolean in_quote = false;
        boolean isNull = false;
        StringBuilder value = new StringBuilder();
        while (c != 0) {
          if (escaped) {
            if (c == 'n')  // Newline
              value.append('\n');
            else if (c == 't')  // Tab
              value.append('\t');
            else if (c == '0')  // Null
              isNull = true;
            else
              value.append(c);
            escaped = false;
          } else if (c == '\\') {
            escaped = true;
          } else if (c == '"') {
            in_quote = !in_quote;
          } else {
            if (!in_quote && (Character.isWhitespace(c) || c == ')')) break;
            value.append(c);
          }
          advance();
        }
        if (escaped) error("Missing escaped character");
        if (in_quote) error("Missing end quote");
        return (TreeType)proto.newLeaf(isNull ? null : value.toString());
      }
    }
  }

  public Iterator<TreeType> parseFromFile(String path) {
    try {
      BufferedReader in = IOUtils.openIn(path);
      return new ParseLispTreeIterator(in, this);
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public TreeType parseFromString(String str) {
    BufferedReader in = new BufferedReader(new StringReader(str));
    Iterator<TreeType> it = new ParseLispTreeIterator(in, this);
    if (!it.hasNext())
      throw new RuntimeException("Invalid: "+str);
    return it.next();
  }

  // To string
  private static final int defaultMaxWidth = 180;
  @Override public String toString() { return toStringWrap(Integer.MAX_VALUE); }
  public String toStringWrap() { return toStringWrap(defaultMaxWidth); }
  public String toStringWrap(int maxWidth) { return toStringWrap(maxWidth, maxWidth); }  // Wrap at maxWidth
  public String toStringWrap(int maxWidth, int subMaxWidth) {  // Wrap at maxWidth, children wrap at subMaxWidth
    StringWriter out = new StringWriter();
    print(maxWidth, subMaxWidth, out);
    return out.toString();
  }
  public void print(Writer out) { print(defaultMaxWidth, defaultMaxWidth, out); }
  public void print(int maxWidth, int subMaxWidth, Writer out) {
    try {
      toStringHelper(maxWidth, subMaxWidth, "", out);
    } catch(IOException e) {
      throw new RuntimeException(e);
    }
  }

  // Return number of characters it would take to render this tree on one line.
  // Can give up when it exceeds maxWidth
  protected int numChars(int maxWidth) {
    // Don't take into account escaping for now, not exact...
    if (isLeaf()) return value == null ? 0 : value.length();
    int sum = 1 + children.size();  // Spaces and parens
    for (TreeType child : children) {
      sum += child.numChars(maxWidth - sum);
      if (sum > maxWidth) return sum;  // Break early
    }
    return sum;
  }

  protected void toStringHelper(int maxWidth, int subMaxWidth, String indent, Writer out) throws IOException {
    if (isLeaf()) {
      out.append(indent);
      if (value == null) {
        out.append("\\0");
      } else {
        boolean shouldQuote = value.length() == 0;
        for (int i = 0; i < value.length(); i++) {
          char c = value.charAt(i);
          if (Character.isWhitespace(c) || c == '(' || c == ')' || c == '#') {
            shouldQuote = true;
            break;
          }
        }
        if (shouldQuote) out.append('"');
        for (int i = 0; i < value.length(); i++) {
          char c = value.charAt(i);
          if (c == '"' || c == '\\') {
            out.append('\\');
            out.append(c);
          } else if (c == '\n') {
            out.append('\\');
            out.append('n');
          } else if (c == '\t') {
            out.append('\\');
            out.append('t');
          } else {
            out.append(c);
          }
        }
        if (shouldQuote) out.append('"');
      }
    } else {
      // Try laying out on one line
      if (numChars(maxWidth) <= maxWidth) {
        out.append(indent);
        boolean first = true;
        out.append('(');
        for (TreeType subtree : children) {
          if (!first) out.append(' ');
          subtree.toStringHelper(Integer.MAX_VALUE, Integer.MAX_VALUE, "", out);
          first = false;
        }
        out.append(')');
      } else {
        out.append(indent);
        out.append('(');
        boolean first = true;
        String newIndent = indent+"  ";
        for (TreeType subtree : children) {
          if (first && subtree.isLeaf()) {
            subtree.toStringHelper(Integer.MAX_VALUE, Integer.MAX_VALUE, "", out);
          } else {
            out.append('\n');
            subtree.toStringHelper(subMaxWidth, subMaxWidth, newIndent, out);
          }
          first = false;
        }
        out.append('\n');
        out.append(indent);
        out.append(')');
      }
    }
  }
}
