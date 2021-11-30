package fig.record;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.stderr;

/**
 * A filter command node operates on a record node by
 * returning a record node that only has a subset of its children.
 * It will apply its child to each of the children that survived.
 */
public class FilterCommandNode extends TwigRecordNode implements CommandNode {
  private RecordNodeMatcher matcher;

  public FilterCommandNode(RecordNodeMatcher matcher, CommandNode child) {
    super("filter", matcher.toString(), child);
    this.matcher = matcher;
  }

  public RecordNode exec(LocalCommandEnv localEnv) {
    RecordNode record = localEnv.getCurrRecord(); 
    // If reqKey exists, it could help efficiency, but currently it doesn't do that
    //String reqKey = matcher.getReqKey();
    CommandNode childCmd = (CommandNode)getChild();

    // If we match all, then we can do this quite quickly.
    if(matcher.matchesAll())
      return SubsetHintUtils.applyHint(localEnv.getHint(),
          record, childCmd, localEnv);

    FullRecordNode result =
      new FullRecordNode(record.getKey(), record.getValue());
    List<RecordNode> childRecords = record.getChildren();
      //(reqKey == null ? record.getChildren() : record.getChildren(reqKey));

    SubsetHint hint = localEnv.getHint();
    VarBindingList bindings = localEnv.getVarBindingList();
    SubsetOracle oracle = null;
    if(matcher.getKeyMatcher() instanceof OrMatcher || matcher.getValueMatcher() instanceof OrMatcher) {
      // Handle OrMatchers separately.  For correctness, we don't need this
      // block of code, but we want to display the results in order.
      // MASSIVELY INEFFICIENT
      Matcher keyMatcher = matcher.getKeyMatcher();
      Matcher valueMatcher = matcher.getValueMatcher();
      List<Matcher> keyMatchers =
        (keyMatcher instanceof OrMatcher) ?
        ((OrMatcher)keyMatcher).getMatchers() : ListUtils.newList(keyMatcher);
      List<Matcher> valueMatchers =
        (valueMatcher instanceof OrMatcher) ?
        ((OrMatcher)valueMatcher).getMatchers() : ListUtils.newList(valueMatcher);

      // Go through the records, 
      for(int q = 0; q < 2; q++) {
        // First time through the loop (q=0) is to count
        // Second is to actually get the 
        if(q == 0 && !hint.needTotalCount()) { // Don't need count
          oracle = hint.getOracle(0);
          continue;
        }
        int n = 0; // Count
        for(Matcher k : keyMatchers) { // Go through the matchers in order...
          for(Matcher v : valueMatchers) {
            for(RecordNode childRecord : childRecords) { // For each record...
              if(k.matches(childRecord.getKey(), bindings) &&
                 v.matches(childRecord.getValue(), bindings)) {
                if(q == 1 && oracle.inSubset(n))
                  result.addChild(childCmd.exec(
                    localEnv.withCurrRecord(childRecord).withHintIsDefault().withIndex(n)));
                n++;
              }
            }
          }
        }
        if(q == 0) oracle = hint.getOracle(n);
      }
    }
    else {
      // Just plow through the results normally and filter
      for(int q = 0; q < 2; q++) {
        // First time through the loop (q=0) is to count
        // Second is to actually get the 
        if(q == 0 && !hint.needTotalCount()) { // Don't need count
          oracle = hint.getOracle(0);
          continue;
        }
        int n = 0; // Count
        for(RecordNode childRecord : childRecords) {
          if(matcher.matches(childRecord, bindings)) {
            if(q == 1 && oracle.inSubset(n)) {
              result.addChild(childCmd.exec(
                localEnv.withCurrRecord(childRecord).withHintIsDefault().withIndex(n)));
            }
            n++;
          }
        }
        if(q == 0) oracle = hint.getOracle(n);
      }
    }
    return result;
  }

  public RecordNode withoutChildren() {
    return new FilterCommandNode(matcher, null);
  }
}
