package fig.prob;

import java.io.*;
import java.util.*;
import fig.basic.*;

public class MargMultinomial implements MargDistrib<Multinomial>, Serializable {
  private static long serialVersionUID = 42;

  private DirichletInterface prior;
  
  public MargMultinomial(DirichletInterface prior) {
    this.prior = prior;
  }

  public double margLogLikelihood(SuffStats _stats) {
    if(prior instanceof DegenerateDirichlet)
      return expectedLogLikelihood(_stats);
    return predLogLikelihood(null, _stats);
  }

  public double predLogLikelihood(SuffStats _condStats, SuffStats _predStats) {
    MultinomialSuffStats condStats = (MultinomialSuffStats)_condStats;
    MultinomialSuffStats predStats = (MultinomialSuffStats)_predStats;
    Dirichlet dprior = (Dirichlet)prior; // Assume not degenerate
    double sum = 0;
    for(int i = 0; i < dprior.dim(); i++) {
      sum += DirichletUtils.logGammaRatio(
        dprior.getAlpha(i) + (condStats == null ? 0 : condStats.getCount(i)),
        predStats.getCount(i));
    }
    sum -= DirichletUtils.logGammaRatio(
      dprior.totalCount() + (condStats == null ? 0 : condStats.totalCount()),
      predStats.totalCount());
    return sum;
  }

  public double logProb(SuffStats stats) {
    return prior.logProb(stats);
  }
  public double logProbObject(Multinomial mult) {
    return prior.logProbObject(mult.getProbs());
  }
  public double crossEntropy(Distrib<Multinomial> _that) {
    MargMultinomial that = (MargMultinomial)_that;
    return this.prior.crossEntropy(that.prior);
  }

  public double expectedLog(int i) { return prior.expectedLog(i); }
  public double[] expectedLog() { return prior.expectedLog(); }
  public int dim() { return prior.dim(); }

  public double expectedLogLikelihood(SuffStats _stats) {
    MultinomialSuffStats stats = (MultinomialSuffStats)_stats;
    double[] counts = stats.getCounts();
    double sum = 0;
    for(int i = 0; i < counts.length; i++)
      sum += counts[i] * prior.expectedLog(i);
    NumUtils.assertIsFinite(sum);
    return sum;
  }

  public DirichletInterface getPrior() { return prior; }

  public MargMultinomial getPosterior(SuffStats stats) {
    Dirichlet dprior = (Dirichlet)prior; // Assume not degenerate
    return new MargMultinomial(new Dirichlet(
      ListUtils.add(dprior.getAlpha(), ((MultinomialSuffStats)stats).getCounts())
    ));
  }

  public MargMultinomial modeSpike() {
    return new MargMultinomial(prior.modeSpike());
  }

  public MargMultinomial perturb(Random random) {
    Dirichlet dprior = (Dirichlet)prior; // Assume not degenerate
    return new MargMultinomial(dprior.perturb(random));
  }
  public MargMultinomial degeneratePerturb(Random random) {
    Dirichlet dprior = (Dirichlet)prior; // Assume not degenerate
    return new MargMultinomial(new DegenerateDirichlet(dprior.sample(random)));
  }

  public Multinomial sampleObject(Random random) {
    return new Multinomial(prior.sampleObject(random));
  }

  public String toString() {
    return String.format("MargMultinomial(%s)", prior);
  }
}
