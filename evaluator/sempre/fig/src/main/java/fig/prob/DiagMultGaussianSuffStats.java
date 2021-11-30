package fig.prob;

import fig.basic.*;

/**
 * Sufficient statistics for a diagonal multivariate Gaussian:
 *  - sum of data points
 *  - sum of squares of data points
 *  - number of data points
 */
public class DiagMultGaussianSuffStats implements SuffStats {
  public DiagMultGaussianSuffStats(int numDim) {
    sum = new double[numDim];
    sumSq = new double[numDim];
    n = 0;
  }
  public DiagMultGaussianSuffStats(double[] x) {
    sum = new double[x.length];
    sumSq = new double[x.length];
    for(int i = 0; i < x.length; i++) {
      sum[i] = x[i];
      sumSq[i] = x[i]*x[i];
    }
    n = 1;
  }
  public DiagMultGaussianSuffStats(DiagMultGaussianSuffStats stats) {
    sum = stats.sum.clone();
    sumSq = stats.sumSq.clone();
    n = stats.n;
  }
  public DiagMultGaussianSuffStats(double[] sum, double[] sumSq, double n) {
    this.sum = sum;
    this.sumSq = sumSq;
    this.n = n;
  }

  public void add(double[] x) { // Add a data point
    for(int i = 0; i < sum.length; i++) {
      sum[i] += x[i];
      sumSq[i] += x[i]*x[i];
    }
    n++;
  }
  public void add(SuffStats _stats) { // Add several data points
    DiagMultGaussianSuffStats stats = (DiagMultGaussianSuffStats)_stats;
    for(int i = 0; i < sum.length; i++) {
      sum[i] += stats.sum[i];
      sumSq[i] += stats.sumSq[i];
    }
    n += stats.n;
  }
  public void sub(double[] x) { // Remove a data point
    for(int i = 0; i < sum.length; i++) {
      sum[i] -= x[i];
      sumSq[i] -= x[i]*x[i];
    }
    n--;
  }
  public void sub(SuffStats _stats) { // Remove several data points
    DiagMultGaussianSuffStats stats = (DiagMultGaussianSuffStats)_stats;
    for(int i = 0; i < sum.length; i++) {
      sum[i] -= stats.sum[i];
      sumSq[i] -= stats.sumSq[i];
    }
    n -= stats.n;
  }

  public SuffStats reweight(double scale) {
    return new DiagMultGaussianSuffStats(
      ListUtils.mult(scale, sum),
      ListUtils.mult(scale, sumSq),
      scale*n);
  }

  public double[] getMean() {
    double[] x = new double[sum.length];
    for(int i = 0; i < sum.length; i++)
      x[i] = sum[i] / n;
    return x;
  }

  public GaussianSuffStats getComponent(int i) {
    return new GaussianSuffStats(sum[i], sumSq[i], n);
  }
  public double[] getSum() { return sum; }
  public double[] getSumSq() { return sumSq; }
  public double getSum(int i) { return sum[i]; }
  public double getSumSq(int i) { return sumSq[i]; }
  public double numPoints() { return n; }
  public int dim() { return sum.length; }

  public String toString() {
    return String.format("sum(%s),sumSq(%s),n(%.1f)", Fmt.D(sum), Fmt.D(sumSq), n);
  }

  private double[] sum, sumSq;
  private double n;
}
