package fig.prob;

import java.util.*;
import java.io.*;
import fig.basic.*;

public class MultinomialSuffStats implements SuffStats {
  private double[] counts;
  private double totalCount;
  
  public MultinomialSuffStats(int numDim) {
    this.counts = new double[numDim];
    this.totalCount = 0;
  }
  public MultinomialSuffStats(double[] x) {
    this.counts = x;
    this.totalCount = ListUtils.sum(x);
  }
  public MultinomialSuffStats(int numDim, int i) {
    this.counts = new double[numDim];
    counts[i]++;
    this.totalCount = 1;
  }
  public MultinomialSuffStats(double[] counts, double totalCount) {
    this.counts = counts;
    this.totalCount = totalCount;
  }
  public MultinomialSuffStats(MultinomialSuffStats stats) {
    this.counts = stats.counts.clone();
    this.totalCount = stats.totalCount;
  }
  
  public void add(SuffStats _suffStats) {
    MultinomialSuffStats suffStats = (MultinomialSuffStats) _suffStats;
    ListUtils.incr(counts, +1, suffStats.counts);
    totalCount += suffStats.totalCount;
  }

  public void sub(SuffStats _suffStats) {
    MultinomialSuffStats suffStats = (MultinomialSuffStats) _suffStats;
    ListUtils.incr(counts, -1, suffStats.counts);
    totalCount -= suffStats.totalCount;
  }

  public void add(int i, double x) {
    counts[i] += x;
    totalCount += x;
  }

  public SuffStats reweight(double scale) {
    return new MultinomialSuffStats(
      ListUtils.mult(scale, counts),
      scale*totalCount);
  }

  public double getCount(int i) { return counts[i]; }
  public double[] getCounts() { return counts; }
  public int dim() { return counts.length; }
  public double totalCount() { return totalCount; }

  public String toString() {
    return "counts("+StrUtils.join(counts)+")";
  }
}
