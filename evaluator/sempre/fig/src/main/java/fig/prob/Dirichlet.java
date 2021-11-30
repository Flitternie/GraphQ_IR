package fig.prob;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * Dirichlet distribution.
 */
public class Dirichlet implements DirichletInterface, Serializable {
  private static long serialVersionUID = 42;

  private double[] alpha;
  private double totalCount;

  public Dirichlet(int numDim, double alpha) {
    this.alpha = ListUtils.newDouble(numDim, alpha);
    this.totalCount = alpha * numDim;
  }
  public Dirichlet(double[] alpha) {
    this.alpha = alpha;
    this.totalCount = ListUtils.sum(alpha);
  }

  // Compute log probability
  public double logProb(double[] x) { return logProb(alpha, totalCount, x); }
  public static double logProb(double[] alpha, double totalCount, double[] x) {
    // $p(x|\alpha) = \Gamma(\sum_i \alpha_i)/(\prod_i \Gamma(\alpha_i))
    // \prod_i x^(\alpha_i-1)$
    if(NumUtils.equals(totalCount, alpha.length)) return 0; // Uniform distribution
    double sum = NumUtils.logGamma(totalCount);
    for(int i = 0; i < alpha.length; i++) {
      sum -= NumUtils.logGamma(alpha[i]);
      sum += (alpha[i]-1)*Math.log(x[i]);
    }
    return sum;
  }
  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(double[] x) { return logProb(x); }

  public double[] sample(Random random) { return sample(random, alpha); }
  public static double[] sample(Random random, double[] alpha) {
    double[] x = new double[alpha.length];
    for(int i = 0; i < alpha.length; i++)
      x[i] = Gamma.sample(random, alpha[i], 1);
    NumUtils.normalize(x);
    return x;
  }
  public double[] sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<double[]> _that) {
    Dirichlet that = (Dirichlet)_that;
    double sum = 0;
    sum += DirichletUtils.thatTotalCountContrib(that.totalCount());
    for(int i = 0; i < alpha.length; i++)
      sum += DirichletUtils.elementContrib(this.alpha[i], that.alpha[i], this.totalCount());
    return sum;
  }
  public double expectedLog(int i) {
    return DirichletUtils.expectedLog(alpha[i], totalCount);
  }
  public double[] expectedLog() {
    double[] result = new double[dim()];
    for(int i = 0; i < dim(); i++)
      result[i] = expectedLog(i);
    return result;
  }

  public DirichletInterface modeSpike() {
    return new DegenerateDirichlet(getMode());
  }

  public Dirichlet perturb(Random random) {
    // Sample from the Dirichlet to get a new mean.
    // Use the same concentration.
    // WARNING: the sample might get close to the boundaries
    return new Dirichlet(ListUtils.mult(totalCount, sample(random)));
  }

  public double[] getMean() {
    double[] mean = (double[])alpha.clone();
    NumUtils.normalize(mean);
    return mean;
  }
  public double[] getMode() {
    // HACK
    double[] mode = ListUtils.add(alpha, -1);
    for(int i = 0; i < mode.length; i++) // Fix anything that dips below
      mode[i] = Math.max(mode[i], DistribUtils.margin);
    NumUtils.normalize(mode);
    return mode;
  }
  public double[] getAlpha() { return alpha; }
  public double getAlpha(int i) { return alpha[i]; }
  public double totalCount() { return totalCount; }
  public int dim() { return alpha.length; }

  public String toString() { return String.format("Dirichlet(%s)", Fmt.D(alpha)); }
}
