package fig.record;

import java.util.*;
import fig.basic.*;

// Return the same value for each index: implements the emptyset and the whole set.
class ConstantOracle implements SubsetOracle {
  private boolean value;
  private ConstantOracle(boolean value) { this.value = value; }
  public int getLowerBound() { return 0; }
  public int getUpperBound() { return value ? Integer.MAX_VALUE : 0; }
  public boolean inSubset(int i) { return value; }
  public static ConstantOracle trueOracle = new ConstantOracle(true);
  public static ConstantOracle falseOracle = new ConstantOracle(false);
}
class ConstantSubsetHint implements SubsetHint {
  private ConstantOracle oracle;
  public ConstantSubsetHint(ConstantOracle oracle) { this.oracle = oracle; }
  public boolean needTotalCount() { return false; }
  public SubsetOracle getOracle(int n) { return oracle; }
  public static final ConstantSubsetHint allHint =
    new ConstantSubsetHint(ConstantOracle.trueOracle);
  public static final ConstantSubsetHint noneHint =
    new ConstantSubsetHint(ConstantOracle.falseOracle);
}

/**
 * Selects a subset of the indices based on a [start, end) interval
 * and a step or a count.
 * The arguments are start, end, step/count.
 * start and end can be a absolute index (3) or a relative fraction (0.3f).
 * step (+3) is the number to skip, count is the total number of approximately
 * evenly-spaced indices to keep.
 */
public class PeriodicSubsetHint implements SubsetHint {
  private ArgsParser parser;

  public PeriodicSubsetHint(List<String> args, VarBindingList bindings) {
    this.parser = new ArgsParser(VarBindingList.varEscapeChar, args);
    parser.setNames("start", "end", "stepcount").parse(bindings);
  }

  private boolean indexRequiresTotalCount(String s) {
    return s.endsWith("f") || Utils.parseIntEasy(s, 0) < 0;
  }

  public boolean needTotalCount() {
    return indexRequiresTotalCount(parser.get("start", "")) ||
           indexRequiresTotalCount(parser.get("end", "")) ||
           (!parser.get("stepcount", "").equals("") && !parser.get("stepcount", "").startsWith("+"));
  }

  public SubsetOracle getOracle(int n) {
    if(!needTotalCount()) return new PeriodicOracle(Integer.MAX_VALUE);
    return new PeriodicOracle(n);
  }

  private class PeriodicOracle implements SubsetOracle {
    private int start, end, step, count;

    public PeriodicOracle(int n) {
      // format: start, end, step/count
      // start and end can either be an absolute position
      // (negative for from the back of the list)
      // or a fraction of n (ends with f)
      // step/count is either absolute step +3 or count of number of
      // equally-spaced entries to keep
      this.start = parser.get("start", "").endsWith("f") ?
        (int)(parser.getDouble("start", 0)*n) :
        parser.getInt("start", 0);
      this.end = parser.get("end", "").endsWith("f") ?
        (int)(parser.getDouble("end", 1)*n) :
        parser.getInt("end", n);
      this.step = 1;
      this.count = n;
      if(parser.get("stepcount", "").startsWith("+")) {
        count = -1;
        step = Utils.parseIntEasy(parser.get("stepcount", "").substring(1), -1); // +step
      }
      else {
        count = parser.getInt("stepcount", -1); // number of entries
        step = -1;
      }

      // Make bounds right
      if(start < 0) start += n;
      if(end <= 0) end += n;
      start = NumUtils.bound(start, 0, n);
      end = NumUtils.bound(end, 0, n);

      if(step != -1) count = Math.max((end-start)/step, 1);
      else if(count != -1) step = Math.max((end-start)/count, 1);
      else {
        count = end-start;
        step = 1;
      }
    }

    public int getLowerBound() { return start; }
    public int getUpperBound() { return end; }

    public boolean inSubset(int i) {
      return
        i >= start && i < end &&
        (i-start) % step == 0 && (i-start)/step < count;
    }
  }
}
