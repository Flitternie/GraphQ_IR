package fig.record;

import java.util.*;

/**
 * Most of the record node functionality is here.
 */
public abstract class AbstractRecordNode implements RecordNode {
  private final String key, value;

  public AbstractRecordNode(String key, String value) {
    this.key = key;
    this.value = value;
  }

  // Basic functionality
  public String getKey() { return key; }
  public String getValue() { return value; }
  public double getDoubleValue() { return RecordNodeUtils.getDoubleValue(this); }
  public String getDescription(RecordNode.DescriptionType type) {
    return RecordNodeUtils.getDescription(getKey(), getValue(), type);
  }

  // Functionality concerning children
  // Return collection of keys that children use
  public List<RecordNode> getChildren(String key) {
    // Override this function if can do better than linear time lookup
    List<RecordNode> matchedChildren = new ArrayList<RecordNode>();
    for(RecordNode child : getChildren())
      if(child.getKey().equals(key))
        matchedChildren.add(child);
    return matchedChildren;
  }
  public int numChildren() {
    // Override if getChildren() is slow and there's a faster way
    return getChildren().size();
  }
  public int numChildren(String key) {
    // Override if there's a faster way
    return getChildren(key).size();
  }

  public String toString() { return getDescription(DescriptionType.human); }

  // Warning: we lose the structure of the node this way.
  // For data nodes, it's not a big deal, but for command nodes,
  // this is unacceptable, so we need to override it for those.
  public RecordNode withoutChildren() {
    return new LeafRecordNode(getKey(), getValue());
  }
}
