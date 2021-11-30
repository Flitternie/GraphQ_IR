package fig.prob;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.*;

/**
 * Prior over parameters: mean ~ Gaussian, variance ~ delta.
 * Likelihood of data given parameters: Gaussian(mean, var)
 */
public class MargMeanDiagMultGaussian implements MargDistrib<DiagMultGaussian> {
  // Here a diagonal multivariate Gaussian distribution
  private DiagMultGaussian meanDistrib; // Gaussian prior over the mean of the multivariate Gaussian
  private double[] varSpikes; // Dirac-delta prior over the variance

  public MargMeanDiagMultGaussian(DiagMultGaussian meanDistrib, double[] varSpikes) {
    this.meanDistrib = meanDistrib;
    this.varSpikes = varSpikes;
  }
  public MargMeanDiagMultGaussian(int numDim, Gaussian meanDistrib, double varSpike) {
    this.meanDistrib = new DiagMultGaussian(numDim, meanDistrib);
    this.varSpikes = ListUtils.newDouble(numDim, varSpike);
  }

  public MargMeanGaussian getComponent(int i) {
    return new MargMeanGaussian(meanDistrib.getComponent(i), varSpikes[i]);
  }

  public MargDistrib getPosterior(SuffStats _stats) {
    DiagMultGaussianSuffStats stats = (DiagMultGaussianSuffStats)_stats;
    Gaussian[] meanDistribs = new Gaussian[dim()];
    double[] varSpikes = new double[dim()];
    for(int i = 0; i < dim(); i++) { // Do it to each component independently
      MargMeanGaussian posterior = getComponent(i).getPosterior(stats.getComponent(i));
      meanDistribs[i] = posterior.getMeanDistrib();
      varSpikes[i] = posterior.getVarSpike();
    }
    return new MargMeanDiagMultGaussian(
        new DiagMultGaussian(meanDistribs), varSpikes);
  }

  public double margLogLikelihood(SuffStats stats) {
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += getComponent(i).margLogLikelihood(((DiagMultGaussianSuffStats)stats).getComponent(i));
    return sum;
  }

  public double predLogLikelihood(SuffStats condStats, SuffStats predStats) {
    return getPosterior((DiagMultGaussianSuffStats)condStats).margLogLikelihood(predStats);
  }

  public double logProb(SuffStats stats) {
    return meanDistrib.logProb(stats);
  }
  public double logProbObject(DiagMultGaussian distrib) {
    // Assume the varSpike = distrib.var, otherwise log prob is -infinity
    return meanDistrib.logProbObject(distrib.getMean());
  }

  public double crossEntropy(Distrib<DiagMultGaussian> _distrib) {
    // We'll just assume the varSpikes are the same,
    // otherwise the crossEntropy is -infinity
    MargMeanDiagMultGaussian distrib = (MargMeanDiagMultGaussian)_distrib;
    return meanDistrib.crossEntropy(distrib.meanDistrib);
  }

  public double expectedLogLikelihood(SuffStats _stats) {
    DiagMultGaussianSuffStats stats = (DiagMultGaussianSuffStats)_stats;
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += getComponent(i).expectedLogLikelihood(stats.getComponent(i));
    return sum;
  }

  public DiagMultGaussian sampleObject(Random random) {
    return new DiagMultGaussian(meanDistrib.sample(random), varSpikes);
  }

  public int dim() { return varSpikes.length; }

  public String toString() {
    return String.format("mean(%s),var(%s)", meanDistrib, Fmt.D(varSpikes));
  }
}
