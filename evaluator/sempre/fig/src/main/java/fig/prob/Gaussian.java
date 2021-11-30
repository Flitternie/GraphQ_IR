package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * Univariate Gaussian distribution.
 */
public class Gaussian implements Distrib<Double> {
  private double mean, var;

  public final static double LOG_INV_SQRT_2_PI = -Math.log(Math.sqrt(2*Math.PI));

  public Gaussian(double mean, double var) {
    this.mean = mean;
    this.var = var;
  }

  // Compute log probability
  public double logProb(double x) { return logProb(mean, var, x); }
  public static double logProb(double mean, double var, double x) {
    return -0.5*(x-mean)*(x-mean)/var + LOG_INV_SQRT_2_PI - 0.5*Math.log(var);
  }
  public static double logProb(double mean, double var, double sum, double sumSq, double n) {
    return -0.5*(sumSq - 2*mean*sum + mean*mean)/var + n*(LOG_INV_SQRT_2_PI - 0.5*Math.log(var));
  }
  public static double logProb(double mean, double var, GaussianSuffStats stats) {
    return -0.5*(stats.getSumSq() - 2*mean*stats.getSum() + mean*mean)/var +
      stats.numPoints()*(LOG_INV_SQRT_2_PI - 0.5*Math.log(var));
  }
  public double logProb(SuffStats stats) { return logProb(mean, var, (GaussianSuffStats)stats); }
  public double logProbObject(Double x) { return logProb(x); }

  public double sample(Random random) { return sample(random, mean, var); }
  public static double sample(Random random, double mean, double var) {
    return SampleUtils.sampleGaussian(random) * Math.sqrt(var) + mean;
  }
  public Double sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Double> _that) {
    Gaussian that = (Gaussian)_that;
    double sum = 0;
    sum += LOG_INV_SQRT_2_PI - 0.5*Math.log(that.var);
    sum += -1/(2*that.var) *
      (this.getSecondMoment() // x^2
       - 2*this.getMean()*that.getMean() // - 2 x \mu
         + that.getMean()*that.getMean()); // + \mu^2
    return sum;
  }

  public double getMean() { return mean; }
  public double getSecondMoment() { return var + mean*mean; }
  public double getVar() { return var; }

  public String toString() {
    return String.format("Gaussian(%.3f,%.3f^2)", mean, Math.sqrt(var));
  }
}
