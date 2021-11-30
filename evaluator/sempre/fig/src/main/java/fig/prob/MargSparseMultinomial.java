package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * Sparse version of Dirichlet/Multinomial family based on hash tables.
 */
public class MargSparseMultinomial implements MargDistrib<SparseMultinomial> {
  private SparseDirichletInterface prior;
  
  public MargSparseMultinomial(SparseDirichletInterface prior) { this.prior = prior; }

  public double margLogLikelihood(SuffStats _stats) {
    if(prior instanceof DegenerateSparseDirichlet)
      return expectedLogLikelihood(_stats);

    return predLogLikelihood(SparseMultinomialSuffStats.emptyStats, _stats);
  }

  // return
  //   P(x' \mid \alpha, x) = D(\alpha + x)/D(\alpha + x + x')
  //                        = \Gamma(\sum \alpha_i + x_i) / \Gamma(\sum \alpha_i + x_i + x_i') \times
  //                          \prod_i \Gamma(\alpha_i+x_i+x_i') / \Gamma(\alpha_i+x_i)$
  public double predLogLikelihood(SuffStats _condStats, SuffStats _predStats) {
    SparseMultinomialSuffStats condStats = (SparseMultinomialSuffStats)_condStats;
    SparseMultinomialSuffStats predStats = (SparseMultinomialSuffStats)_predStats;
    SparseDirichlet dprior = (SparseDirichlet)prior;
    double sum = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)predStats) {
      sum += DirichletUtils.logGammaRatio(
        dprior.getConcentration(e.getKey()) + condStats.getCount(e.getKey()),
        e.getValue());
    }
    sum -= DirichletUtils.logGammaRatio(dprior.totalCount() + condStats.totalCount(), predStats.totalCount());
    return sum;
  }

  public MargDistrib getPosterior(SuffStats suffStats) {
    SparseDirichlet dprior = (SparseDirichlet)prior;
    return new MargSparseMultinomial(
      dprior.withExtraCounts((SparseMultinomialSuffStats)suffStats));
  }

  // Compute log probability (use getConcentration)
  public double logProb(SuffStats stats) {
    return prior.logProb(stats);
  }
  public double logProbObject(SparseMultinomial x) {
    return prior.logProbObject(x.getProbs());
  }

  public SparseMultinomial sampleObject(Random random) {
    return new SparseMultinomial(prior.sampleObject(random));
  }

  public double expectedLog(Object key) {
    return prior.expectedLog(key);
  }

  public double crossEntropy(Distrib<SparseMultinomial> distrib) {
    return prior.crossEntropy(((MargSparseMultinomial)distrib).prior);
  }
  public double expectedLogLikelihood(SuffStats _stats) {
    SparseMultinomialSuffStats stats = (SparseMultinomialSuffStats)_stats;
    double sum = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)stats)
      sum += e.getValue() * prior.expectedLog(e.getKey());
    NumUtils.assertIsFinite(sum);
    return sum;
  }

  public MargSparseMultinomial modeSpike() {
    return new MargSparseMultinomial(prior.modeSpike());
  }

  public String toString() { return prior.toString(); }
}
