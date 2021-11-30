package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * Multivariate Gaussian distribution with diagonal covariance.
 */
public class DiagMultGaussian implements Distrib<double[]> {
  private double[] mean, var;

  public DiagMultGaussian(double[] mean, double var) {
    this.mean = mean;
    this.var = ListUtils.newDouble(mean.length, var);
  }
  public DiagMultGaussian(double[] mean, double[] var) {
    this.mean = mean;
    this.var = var;
  }
  public DiagMultGaussian(Gaussian[] distrib) {
    this.mean = new double[distrib.length];
    this.var = new double[distrib.length];
    for(int i = 0; i < dim(); i++) {
      mean[i] = distrib[i].getMean();
      var[i] = distrib[i].getVar();
    }
  }
  public DiagMultGaussian(int numDim, Gaussian distrib) {
    this.mean = ListUtils.newDouble(numDim, distrib.getMean());
    this.var = ListUtils.newDouble(numDim, distrib.getVar());
  }

  public double logProb(double[] x) {
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += Gaussian.logProb(mean[i], var[i], x[i]);
    return sum;
  }
  public double logProb(SuffStats _stats) {
    DiagMultGaussianSuffStats stats = (DiagMultGaussianSuffStats)_stats;
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += Gaussian.logProb(mean[i], var[i], stats.getSum(i), stats.getSumSq(i), stats.numPoints());
    return sum;
  }
  public double logProbObject(double[] x) { return logProb(x); }

  public double[] sample(Random random) {
    double[] x = new double[mean.length];
    for(int i = 0; i < dim(); i++)
      x[i] = Gaussian.sample(random, mean[i], var[i]);
    return x;
  }
  public double[] sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<double[]> _that) {
    DiagMultGaussian that = (DiagMultGaussian)_that;
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += this.getComponent(i).crossEntropy(that.getComponent(i));
    return sum;
  }

  public Gaussian getComponent(int i) { return new Gaussian(mean[i], var[i]); }
  public double[] getMean() { return mean; }
  public double[] getVar() { return var; }
  public double getMean(int i) { return mean[i]; }
  public double getVar(int i) { return var[i]; }
  public int dim() { return mean.length; }

  public String toString() {
    return String.format("mean(%s),var(%s)", Fmt.D(mean), Fmt.D(var));
  }

}
