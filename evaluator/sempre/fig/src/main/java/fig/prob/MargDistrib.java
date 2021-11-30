package fig.prob;

import java.util.*;

/**
 * A probability distribution over parameters of some data model.
 * Specifies both the prior over parameters and the likelihood model:
 *   p(parameters) p(data | parameters)
 * Assume tractability, so we can integrate out parameters.
 * The data will be represented by sufficient statistics,
 * which can summarize many data points.
 */
public interface MargDistrib<T extends Distrib> extends Distrib<T> {
  // Compute the marginalized log-likelihood (marginalizing out parameters).
  // \log p(stats)
  public double margLogLikelihood(SuffStats stats);

  // Compute the predictive log-likelihood (marginalizing out parameters).
  // \log p(predStats | condStats) 
  public double predLogLikelihood(SuffStats condStats, SuffStats predStats);

  // Return posterior over parameters: p(parameters | stats)
  public MargDistrib getPosterior(SuffStats stats);

  // Compute the expected log-likelihood, expectation with respect
  // to this distribution over parameters.
  // \E \log p(stats; parameters)
  public double expectedLogLikelihood(SuffStats stats);
}
