package fig.record;

import java.util.*;

/**
 * A record node without children.
 */
public class LeafRecordNode extends AbstractRecordNode {
  public LeafRecordNode(String key, String value) {
    super(key, value);
  }

  public List<RecordNode> getChildren() { return Collections.EMPTY_LIST; }
  public void addChild(RecordNode node) { }

  public RecordNode shallowCopy(String key, String value) {
    return new LeafRecordNode(key, value);
  }

  public static final LeafRecordNode nullNode = new LeafRecordNode(null, null);
}
