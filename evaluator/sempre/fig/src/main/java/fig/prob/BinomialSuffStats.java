package fig.prob;

public class BinomialSuffStats implements SuffStats {
  private double trueCount, falseCount;
  
  public BinomialSuffStats() { }
  public BinomialSuffStats(boolean x) {
    trueCount = x ? 1 : 0;
    falseCount = x ? 0 : 1;
  }
  public BinomialSuffStats(double trueCount, double falseCount) {
    this.trueCount = trueCount;
    this.falseCount = falseCount;
  }
  
  public void add(SuffStats _stats) {
    BinomialSuffStats stats = (BinomialSuffStats)_stats;
    trueCount += stats.trueCount;
    falseCount += stats.falseCount;
  }

  public void sub(SuffStats _stats) {
    BinomialSuffStats stats = (BinomialSuffStats)_stats;
    trueCount -= stats.trueCount;
    falseCount -= stats.falseCount;
  }

  public SuffStats reweight(double scale) {
    // Just multiply since these are all natural parameters
    return new BinomialSuffStats(scale*trueCount, scale*falseCount);
  }

  public double getTrueCount() { return trueCount; }
  public double getFalseCount() { return falseCount; }
  public double totalCount() { return trueCount+falseCount; }

  public String toString() {
    return String.format("+(%.3f),-(%.3f)", trueCount, falseCount);
  }
}
