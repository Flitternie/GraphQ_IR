package fig.record;

interface SubsetOracle {
  public boolean inSubset(int i);
  public int getLowerBound(); // inSubset = false for anything < lower bound
  public int getUpperBound(); // inSubset = false for anything >= upper bound
}

/**
 * Selects a subset of the indices from a set 0, ..., n-1.
 * Usage: call needTotalCount() to find out if we need the total count n.
 * If so, call getOracle(n), otherwise use getOracle(0).
 */
public interface SubsetHint {
  public boolean needTotalCount();
  public SubsetOracle getOracle(int n);
}
