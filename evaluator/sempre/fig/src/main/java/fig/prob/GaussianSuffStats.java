package fig.prob;

/**
 * Sufficient statistics for a univariate Gaussian:
 *  - sum of data points
 *  - sum of squares of data points
 *  - number of data points
 */
public class GaussianSuffStats implements SuffStats {
  private double sum, sumSq;
  private double n;

  public GaussianSuffStats()                                   { sum = 0;         sumSq = 0;           n = 0;       }
  public GaussianSuffStats(double x)                           { sum = x;         sumSq = x*x;         n = 1;       }
  public GaussianSuffStats(GaussianSuffStats stats)            { sum = stats.sum; sumSq = stats.sumSq; n = stats.n; }
  public GaussianSuffStats(double sum, double sumSq, double n) { this.sum = sum;  this.sumSq = sumSq;  this.n = n;  }

  public void add(double x) { // Add a data point
    sum += x;
    sumSq += x;
    n++;
  }
  public void add(SuffStats _stats) { // Add several data points
    GaussianSuffStats stats = (GaussianSuffStats)_stats;
    sum += stats.sum;
    sumSq += stats.sumSq;
    n += stats.n;
  }
  public void sub(double x) { // Remove a data point
    sum -= x;
    sumSq -= x*x;
    n--;
  }
  public void sub(SuffStats _stats) { // Remove several data points
    GaussianSuffStats stats = (GaussianSuffStats)_stats;
    sum -= stats.sum;
    sumSq -= stats.sumSq;
    n -= stats.n;
  }

  public SuffStats reweight(double scale) {
    // Just multiply since these are all natural parameters
    return new GaussianSuffStats(scale*sum, scale*sumSq, scale*n);
  }

  public double getSum() { return sum; }
  public double getSumSq() { return sumSq; }
  public double numPoints() { return n; }

  public String toString() {
    return String.format("sum(%.3f),sumSq(%.3f),n(%.1f)", sum, sumSq, n);
  }
}
