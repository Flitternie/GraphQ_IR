package fig.prob;

import java.util.*;
import fig.basic.*;

public class Beta implements BetaInterface {
  private double alpha, beta;

  public Beta(double alpha, double beta) {
    this.alpha = alpha;
    this.beta = beta;
  }

  // Compute log probability
  public double logProb(double x) { return logProb(alpha, beta, x); }
  public static double logProb(double alpha, double beta, double x) {
    // $p(x|\alpha,\beta) = \Gamma(\alpha+\beta)/(\Gamma(\alpha) \Gamma(\beta))
    // x^(\alpha-1) (1-x)^(\beta-1)$
    return
      NumUtils.logGamma(alpha+beta) -
      NumUtils.logGamma(alpha) - NumUtils.logGamma(beta) +
      (alpha-1)*Math.log(x) + (beta-1)*Math.log(1-x);
  }
  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(Double x) { return logProb(x); }

  public double sample(Random random) { return sample(random, alpha, beta); }
  public static double sample(Random random, double alpha, double beta) {
    double a = Gamma.sample(random, alpha, 1);
    double b = Gamma.sample(random, beta, 1);
    return a/(a+b);
  }
  public Double sampleObject(Random random) { return sample(random); }

  // If b = true, return \E \log X
  // If b = false, return \E \log (1-X)
  // where X \sim Beta(\alpha, \beta)
  public double expectedLog(boolean b) {
    if(b) return DirichletUtils.expectedLog(alpha, totalCount());
    else  return DirichletUtils.expectedLog(beta, totalCount());
  }

  public double crossEntropy(Distrib<Double> _that) {
    Beta that = (Beta)_that;
    double sum = 0;
    sum += DirichletUtils.thatTotalCountContrib(that.totalCount());
    sum += DirichletUtils.elementContrib(alpha, that.alpha, totalCount());
    sum += DirichletUtils.elementContrib(beta, that.beta, totalCount());
    return sum;
  }

  public double getAlpha() { return alpha; }
  public double getBeta() { return beta; }
  public double getMean() { return alpha/(alpha+beta); }
  public double getMode() {
    if(alpha <= 1 || beta <= 1)
      return alpha > beta ? 1-DistribUtils.margin : DistribUtils.margin;
    return (alpha-1)/(alpha+beta-2);
  }
  public double totalCount() { return alpha+beta; }

  // Return a distribution that's a spike at the mode
  public BetaInterface modeSpike() {
    return new DegenerateBeta(getMode());
  }

  public BetaInterface perturb(Random random) {
    double x = NumUtils.bound(sample(random), DistribUtils.margin, 1-DistribUtils.margin);
    return new Beta(totalCount()*x, totalCount()*(1-x));
  }
  public BetaInterface degeneratePerturb(Random random) {
    return new DegenerateBeta(sample(random));
  }

  public String toString() {
    return String.format("Beta(%.3f,%.3f)", alpha, beta);
  }
}
