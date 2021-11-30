package fig.record;

import java.util.*;

/**
 * The RecordNode is the basic building block of the entire framework.
 * Almost everything is a RecordNode.
 */
public interface RecordNode {
  // strict is machine readable
  public static enum DescriptionType { human, machine };

  // Basic functionality
  public String getKey();
  public String getValue();
  public double getDoubleValue(); // For sorting
  public String getDescription(DescriptionType type);

  // Functionality concerning children
  // Return collection of keys that children use
  public List<RecordNode> getChildren();
  public List<RecordNode> getChildren(String key);
  public int numChildren();
  public int numChildren(String key);
  public void addChild(RecordNode child);

  // Return a copy of the current node, but replacing key and value,
  // but keeping a reference to the same children.
  public RecordNode shallowCopy(String key, String value);
  // Return a copy of the record node, but without the children
  public RecordNode withoutChildren();
}
