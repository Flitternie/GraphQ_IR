package fig.prob;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.*;

/**
 * Prior over parameters: mean ~ Gaussian, var = constant
 * Likelihood given parameters: Gaussian(mean, var)
 */
public class MargMeanGaussian implements MargDistrib<Gaussian> {
  private Gaussian meanDistrib;
  private double varSpike;

  public MargMeanGaussian(Gaussian meanDistrib, double varSpike) {
    this.meanDistrib = meanDistrib;
    this.varSpike = varSpike;
  }

  private Gaussian getMeanPosterior(GaussianSuffStats stats) {
    double px = meanDistrib.getMean();
    double pv = meanDistrib.getVar();
    double postMean, postVar;
    if(stats.numPoints() < 1e-200) {
      postMean = (pv*stats.getSum() + varSpike*px)/varSpike;
      postVar = pv;
    }
    else {
      double lx = stats.getSum() / stats.numPoints();
      double lv = varSpike / stats.numPoints();
      postMean = (pv*lx + lv*px) / (pv+lv);
      postVar = pv*lv / (pv+lv);
    }
    return new Gaussian(postMean, postVar);
  }
  public MargMeanGaussian getPosterior(SuffStats stats) {
    return new MargMeanGaussian(getMeanPosterior((GaussianSuffStats)stats), varSpike);
  }

  public double margLogLikelihood(SuffStats stats) {
    // Compute using Bayes rule
    double sum = 0;
    sum += Gaussian.logProb(meanDistrib.getMean(), meanDistrib.getVar(), 0); // p(theta = 0)
    sum += Gaussian.logProb(0, varSpike, (GaussianSuffStats)stats); // p(x | theta = 0)
    sum -= getMeanPosterior((GaussianSuffStats)stats).logProb(0); // p(theta = 0 | x)
    return sum;
  }

  public double logProb(SuffStats stats) {
    // Only consider mean, assume variances are same
    return meanDistrib.logProb(stats);
  }
  public double logProbObject(Gaussian distrib) {
    // Only consider mean, assume variances are same
    return meanDistrib.logProbObject(distrib.getMean());
  }
  public double crossEntropy(Distrib<Gaussian> _that) {
    // Only consider mean, assume variances are same
    MargMeanGaussian that = (MargMeanGaussian)_that;
    return meanDistrib.crossEntropy(that.meanDistrib);
  }

  public double predLogLikelihood(SuffStats condStats, SuffStats predStats) {
    return getPosterior((GaussianSuffStats)condStats).margLogLikelihood(predStats);
  }

  public Gaussian sampleObject(Random random) {
    return new Gaussian(meanDistrib.sample(random), varSpike);
  }

  public double expectedLogLikelihood(SuffStats _stats) {
    GaussianSuffStats stats = (GaussianSuffStats)_stats;
    double sum = 0;
    sum += stats.numPoints() *
      (Gaussian.LOG_INV_SQRT_2_PI - 0.5*Math.log(varSpike));
    sum += -1/(2*varSpike) *
      (stats.getSumSq() // x^2
       - 2*stats.getSum()*meanDistrib.getMean()
         + meanDistrib.getSecondMoment());
    return sum;
  }

  public Gaussian getMeanDistrib() { return meanDistrib; }
  public double getVarSpike() { return varSpike; }

  public String toString() {
    return String.format("mean(%s),var(%.3f)", meanDistrib, varSpike);
  }
}
