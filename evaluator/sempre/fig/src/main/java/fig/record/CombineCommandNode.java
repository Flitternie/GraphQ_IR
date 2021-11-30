package fig.record;

import java.util.*;
import fig.basic.*;

/**
 * A combine command node has many children.
 * Two ways to combine the result nodes:
 *   CONCAT: concatenate them.
 *   AND: keep on going down its children until one returns something empty
 *        or we reach the last child.
 *   COMPOSE: apply the output of one child to the next's.
 *
 * Presumably, the command hierarchy will resemble the record hierarchy.
 * This needs to be made more precise.
 *
 * Another way to get a limited form composition is just with the normal
 * command hierachy.
 */
public class CombineCommandNode extends FullRecordNode implements CommandNode {
  public enum CombineType { CONCAT, AND, COMPOSE };
  public CombineType combineType;

  public CombineCommandNode(CombineType combineType) {
    super(combineType.toString(), null);
    this.combineType = combineType;
  }

  public RecordNode exec(LocalCommandEnv localEnv) {
    if(combineType == CombineType.CONCAT) {
      // This function is messed up
      FullRecordNode result = new FullRecordNode("concat", null);
      for(RecordNode childCmd : getChildren())
        result.addChild(((CommandNode)childCmd).exec(localEnv.withHintIsDefault()));
      return localEnv.applyHint(result);
    }
    else if(combineType == CombineType.AND) {
      RecordNode result = LeafRecordNode.nullNode; // Failed result
      for(RecordNode childCmd : getChildren()) {
        result = ((CommandNode)childCmd).exec(localEnv.withHintIsSame());
        if(isFailure(result)) break; // Failed!
      }
      return result;
    }
    else if(combineType == CombineType.COMPOSE) {
      RecordNode result = LeafRecordNode.nullNode; // Failed result
      for(RecordNode childCmd : getChildren()) {
        result = ((CommandNode)childCmd).exec(localEnv.withHintIsDefault());
        // Setup for next command in the composition
        localEnv = localEnv.withCurrRecord(result);
      }
      return localEnv.applyHint(result);
    }
    else
      throw new RuntimeException("Unknown combine type: " + combineType);
  }

  // Return null if can't do it
  public static CombineType parseCombineType(String s) {
    if(s == null) return CombineType.COMPOSE;
    if(s.equals("+")) return CombineType.CONCAT;
    if(s.equals("&")) return CombineType.AND;
    if(s.equals("@")) return CombineType.COMPOSE;
    throw Exceptions.unknownCase;
  }

  public static boolean isFailure(RecordNode record) {
    return record.numChildren() == 0;
  }

  public RecordNode withoutChildren() {
    return new CombineCommandNode(combineType);
  }
}
