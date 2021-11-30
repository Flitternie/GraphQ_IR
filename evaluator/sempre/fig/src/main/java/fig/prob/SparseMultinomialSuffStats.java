package fig.prob;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.*;

// Sufficient statistics for the multinomial: counts for each of 
// the observations (which are sparse).
public class SparseMultinomialSuffStats extends TDoubleMap implements SuffStats {
  private double totalCount = 0; // For efficiency

  public SparseMultinomialSuffStats() { }
  public SparseMultinomialSuffStats(TDoubleMap map) {
    incrMap(map, +1);
    totalCount += map.sum();
  }

  public static SparseMultinomialSuffStats singleton(Object key) {
    SparseMultinomialSuffStats stats = new SparseMultinomialSuffStats();
    stats.put(key, 1);
    stats.totalCount = 1;
    return stats;
  }

  public void add(SuffStats _stats) {
    SparseMultinomialSuffStats stats = (SparseMultinomialSuffStats)_stats;
    incrMap(stats, +1);
    totalCount += stats.totalCount;
  }
  public void sub(SuffStats _stats) {
    SparseMultinomialSuffStats stats = (SparseMultinomialSuffStats)_stats;
    incrMap(stats, -1);
    totalCount -= stats.totalCount;
  }
  public SuffStats reweight(double scale) {
    // Not very efficient
    SparseMultinomialSuffStats stats = new SparseMultinomialSuffStats();
    stats.incrMap(this, scale);
    return stats;
  }

  public double getCount(Object o) { return get(o, 0); }
  public double totalCount() { return totalCount; }

  public String toString() {
    return String.format("Mult(%s)",
      MapUtils.topNToString(this, 20));
  }

  public static final SparseMultinomialSuffStats emptyStats = new SparseMultinomialSuffStats();
}
