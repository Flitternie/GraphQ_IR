package fig.basic;

import java.util.*;

// Keeps track of statistics (moments) of a sequence of numbers.
public class StatFig {
  public StatFig() { min = Double.POSITIVE_INFINITY; max = Double.NEGATIVE_INFINITY; }

  public void add(boolean x) { add(x ? 1 : 0); }
  public void add(double x) { add(null, x); }
  public void add(Object key, double x) {
    count++;
    sum += x;
    sumsq += x*x;
    if (x < min) { min = x; minKey = key; }
    if (x > max) { max = x; maxKey = key; }
  }
  public void add(StatFig fig) {
    count += fig.count;
    sum += fig.sum;
    sumsq += fig.sumsq;
    if (fig.min < min) { min = fig.min; minKey = fig.minKey; }
    if (fig.max > max) { max = fig.max; maxKey = fig.maxKey; }
  }

  public double count() { return count; }
  public double mean() { return sum/count; }
  public double sum() { return sum; }
  public double variance() { return sumsq/count - mean()*mean(); }
  public double stddev() { return Math.sqrt(variance()); }
  public double min() { return min; }
  public double max() { return max; }
  public Object minKey() { return minKey; }
  public Object maxKey() { return maxKey; }
  public double range() { return max-min; }

  public String toString() {
    if(count == 0) return "NaN (0)";
    return render(min, minKey) + "/ << " + Fmt.D(mean()) + " ~ " + Fmt.D(stddev()) + " >> /" + render(max, maxKey) + " (" + count + ")";
  }
  private String render(double x, Object key) {
    return Fmt.D(x) + (key == null ? "" : "@"+key);
  }

  private double min, max;
  private Object minKey, maxKey;
  private double sum, sumsq;
  private int count;
}
