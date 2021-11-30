package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * Want to raise a distribution to an inverse temperature.
 * But we need to evaluate marginal log likelihoods
 */
public class TemperedMargDistrib<T extends Distrib> implements MargDistrib<T> {
  private MargDistrib<T> distrib;
  private double temperature;

  public TemperedMargDistrib(MargDistrib<T> distrib, double temperature) {
    this.distrib = distrib;
    this.temperature = temperature;
  }

  public double margLogLikelihood(SuffStats stats) {
    return distrib.margLogLikelihood(stats) / temperature;
  }

  public double predLogLikelihood(SuffStats condStats, SuffStats predStats) {
    return distrib.predLogLikelihood(condStats, predStats) / temperature;
  }

  public MargDistrib getPosterior(SuffStats stats) {
    return new TemperedMargDistrib(distrib.getPosterior(stats), temperature);
  }

  public double expectedLogLikelihood(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProb(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProbObject(T x) { throw Exceptions.unsupported; }
  public T sampleObject(Random random) { throw Exceptions.unsupported; }
  public double crossEntropy(Distrib<T> distrib) { throw Exceptions.unsupported; }
}
