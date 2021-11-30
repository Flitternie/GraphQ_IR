package fig.record;

import fig.basic.*;
import java.util.*;

/**
 * A structured record node.
 * Store it specifically to save memory.
 * For example:
 * .struct index leftValue rightValue
 * 0 A B
 * Creates a node (index, 0) with two children, (leftValue, A) and (rightValue, B)
 */
public class StructRecordNode implements RecordNode {
  private String[] keys, values;

  public StructRecordNode(String[] keys, String[] values) {
    this.keys = keys;
    this.values = values;
    if(keys.length != values.length)
      throw Exceptions.bad("StructRecordNode: mis-match in length: keys are [%s] (%d), values are [%s] (%d)",
        StrUtils.join(keys, " | "), keys.length,
        StrUtils.join(values, " | "), values.length);
  }

  public String getKey() { return keys[0]; }
  public String getValue() { return values[0]; }
  public double getDoubleValue() { return RecordNodeUtils.getDoubleValue(this); }
  public String getDescription(RecordNode.DescriptionType type) {
    return RecordNodeUtils.getDescription(getKey(), getValue(), type);
  }

  public List<RecordNode> getChildren() { // Inefficient
    List<RecordNode> children = new ArrayList<RecordNode>();
    for(int i = 1; i < keys.length; i++)
      children.add(new LeafRecordNode(keys[i], values[i]));
    return children;
  }
  public List<RecordNode> getChildren(String key) {
    // Assume the keys are unique
    for(int i = 1; i < keys.length; i++)
      if(key.equals(keys[i]))
        return Collections.singletonList((RecordNode)new LeafRecordNode(keys[i], values[i]));
    return Collections.EMPTY_LIST;
  }
  public int numChildren() { return keys.length - 1; }
  public int numChildren(String queryKey) {
    for(String key : keys)
      if(key.equals(queryKey))
        return 1;
    return 0;
  }

  public void addChild(RecordNode node) { throw Exceptions.unsupported; }

  public RecordNode shallowCopy(String key, String value) {
    String[] newKeys = (String[])keys.clone();
    String[] newValues = (String[])values.clone();
    newKeys[0] = key;
    newValues[0] = value;
    return new StructRecordNode(newKeys, newValues);
  }

  public RecordNode withoutChildren() {
    return new LeafRecordNode(getKey(), getValue());
  }
}
