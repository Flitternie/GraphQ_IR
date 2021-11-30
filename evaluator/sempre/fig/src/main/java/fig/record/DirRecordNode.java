package fig.record;

import java.io.*;
import java.util.*;

/**
 * A directory entries.  Children are files and directories.
 */
public class DirRecordNode extends PathRecordNode {
  private boolean isLoading;

  public DirRecordNode(LoadFileState state, File path) {
    super(state, path);
  }
  public DirRecordNode(LoadFileState state, String key, String value, File path) {
    super(state, key, value, path);
  }

  public void loadChildren() {
    if(isLoading) return; // Prevent infinite loop

    isLoading = true;

    // All the files we currently have loaded
    Map<String, RecordNode> currNodes = new HashMap<String, RecordNode>();
    for(RecordNode child : getChildren())
      currNodes.put(child.getKey(), child);

    // Going to fill up this array with new children
    List<RecordNode> newChildren = new ArrayList<RecordNode>();

    // Get the list of new files
    String[] names = getPath().list();
    for(String name : names) {
      // Try to reuse old file objects if possible
      RecordNode node = currNodes.get(name);
      if(node == null) node = newPathNode(this, state, name); // Need new one
      if(node != null) newChildren.add(node); // Add if it's good
    }

    setChildren(newChildren);
    super.loadChildren();

    isLoading = false;
  }
  
  public RecordNode shallowCopy(String key, String value) {
    DirRecordNode node = new DirRecordNode(state, key, value, getPath());
    node.setChildren(getChildren());
    return node;
  }
  public RecordNode withoutChildren() {
    return new DirRecordNode(state, getPath()).disableLoading();
  }

  public String getDescription(RecordNode.DescriptionType type) {
    if(type == RecordNode.DescriptionType.human)
      return super.getDescription(type);
    else
      return ".dir\t" + getPath() +
        (getValue() == null ? "" : "\t"+getValue());
  }
}
