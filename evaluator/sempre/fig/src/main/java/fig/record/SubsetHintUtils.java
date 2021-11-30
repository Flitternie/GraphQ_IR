package fig.record;

import java.util.*;

public class SubsetHintUtils {
  // Keep only the subset of the children specified by hint.
  // This is the default way of applying the hint,
  // if we don't want to integrate the hint with the generation
  // of the result record node.
  public static RecordNode applyHint(SubsetHint hint, RecordNode result) {
    return applyHint(hint, result, null, null);
  }

  // Apply the hint, and on each node we're keeping, apply the cmd
  // on that node with specified the local environment.
  public static RecordNode applyHint(SubsetHint hint, RecordNode result,
      CommandNode cmd, LocalCommandEnv localEnv) {
    // Don't change anything
    if(hint == ConstantSubsetHint.allHint && cmd == null) return result;

    // Aggregate new results here
    FullRecordNode newResult =
      new FullRecordNode(result.getKey(), result.getValue());
    List<RecordNode> childRecords = result.getChildren();

    SubsetOracle oracle = hint.getOracle(childRecords.size());
    int lower = oracle.getLowerBound();
    int upper = Math.min(oracle.getUpperBound(), childRecords.size());

    // Loop through the relevant parts of the result.
    for(int i = lower; i < upper; i++) {
      RecordNode childRecord = childRecords.get(i);
      if(!oracle.inSubset(i)) continue;
      if(cmd == null)
        newResult.addChild(childRecord);
      else
        newResult.addChild(cmd.exec(localEnv.withCurrRecord(childRecord).withIndex(i)));
    }
    return newResult;
  }
}
