package fig.prob;

import java.io.*;
import java.util.*;
import fig.basic.*;

public class MargBinomial implements MargDistrib<Binomial> {
  private BetaInterface prior;
  
  public MargBinomial(BetaInterface prior) {
    this.prior = prior;
  }

  public double margLogLikelihood(SuffStats _stats) {
    if(prior instanceof DegenerateBeta)
      return expectedLogLikelihood(_stats);
    return predLogLikelihood(null, _stats);
  }

  public double predLogLikelihood(SuffStats _condStats, SuffStats _predStats) {
    BinomialSuffStats condStats = (BinomialSuffStats)_condStats;
    BinomialSuffStats predStats = (BinomialSuffStats)_predStats;
    Beta bprior = (Beta)prior; // Assume not degenerate
    double sum = 0;
    sum += DirichletUtils.logGammaRatio(
      bprior.getAlpha() + (condStats == null ? 0 : condStats.getTrueCount()),
      predStats.getTrueCount());
    sum += DirichletUtils.logGammaRatio(
      bprior.getBeta() + (condStats == null ? 0 : condStats.getFalseCount()),
      predStats.getFalseCount());
    sum -= DirichletUtils.logGammaRatio(
      bprior.totalCount() + (condStats == null ? 0 : condStats.totalCount()),
      predStats.totalCount());
    return sum;
  }

  public double logProb(SuffStats stats) {
    return prior.logProb(stats);
  }
  public double logProbObject(Binomial bin) {
    return prior.logProbObject(bin.getProb());
  }
  public double crossEntropy(Distrib<Binomial> _that) {
    MargBinomial that = (MargBinomial)_that;
    return this.prior.crossEntropy(that.prior);
  }

  public double expectedLog(boolean b) { return prior.expectedLog(b); }

  public double expectedLogLikelihood(SuffStats _stats) {
    BinomialSuffStats stats = (BinomialSuffStats)_stats;
    double sum = 0;
    sum += stats.getTrueCount() * prior.expectedLog(true);
    sum += stats.getFalseCount() * prior.expectedLog(false);
    NumUtils.assertIsFinite(sum);
    return sum;
  }

  public BetaInterface getPrior() { return prior; }

  public MargBinomial getPosterior(SuffStats _stats) {
    BinomialSuffStats stats = (BinomialSuffStats)_stats;
    return new MargBinomial(
      new Beta(prior.getAlpha()+stats.getTrueCount(),
               prior.getBeta()+stats.getFalseCount()));
  }

  public MargBinomial modeSpike() {
    return new MargBinomial(prior.modeSpike());
  }

  public MargBinomial perturb(Random random) {
    Beta dprior = (Beta)prior; // Assume not degenerate
    return new MargBinomial(dprior.perturb(random));
  }
  public MargBinomial degeneratePerturb(Random random) {
    Beta dprior = (Beta)prior; // Assume not degenerate
    return new MargBinomial(new DegenerateBeta(dprior.sample(random)));
  }

  public Binomial sampleObject(Random random) {
    return new Binomial(prior.sampleObject(random));
  }

  public String toString() {
    return String.format("MargBinomial(%s)", prior);
  }
}
