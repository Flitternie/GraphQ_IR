package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * A Dirichlet distribution over multinomial parameters.
 * It efficiently represents a Dirichlet distribution
 * that is uniform over all dimensions (smoothing) plus
 * a sparse counts on some dimensions.
 */
public class SparseDirichlet implements SparseDirichletInterface {
  protected int numDim; // Number of dimensions
  protected double pseudoCount;
  protected TDoubleMap counts;
  protected double totalCount;

  public SparseDirichlet(int numDim, double pseudoCount) {
    this(numDim, pseudoCount, new TDoubleMap());
  }
  public SparseDirichlet(int numDim, double pseudoCount, TDoubleMap counts) {
    this.numDim = numDim;
    this.counts = counts;
    this.pseudoCount = pseudoCount;
    this.totalCount = numDim * pseudoCount + counts.sum();
  }

  public int dim() { return numDim; }

  public double getConcentration(Object key) {
    return pseudoCount + counts.get(key, 0);
  }
  public double getMean(Object key) {
    return getConcentration(key) / totalCount;
  }
  public double getMode(Object key) {
    return getMode(getConcentration(key), pseudoCount, totalCount, numDim);
  }
  public double totalCount() { return totalCount; }

  // Compute log probability (use getConcentration)
  public double logProb(SuffStats stats) {
    throw new RuntimeException("Haven't implemented the sufficient statistics");
  }
  public double logProbObject(TDoubleMap probs) {
    double sum = NumUtils.logGamma(totalCount);
    if(probs.size() != numDim)
      throw new RuntimeException("the probability must have support everywhere");
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)probs) {
      double count = getConcentration(e.getKey());
      sum -= NumUtils.logGamma(count);
      sum += (count-1)*Math.log(e.getValue());
    }
    NumUtils.assertIsFinite(sum);
    return sum;
  }

  public TDoubleMap sampleObject(Random random) {
    // Generate a bunch of Gamma variables and normalize
    TDoubleMap probs = new TDoubleMap();
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)counts)
      probs.put(e.getKey(), Gamma.sample(random, pseudoCount+e.getValue(), 1));
    // We lose sparsity: we just make up names of the
    // dimensions we haven't seen in counts
    if(counts.size() > numDim) throw new RuntimeException("numDim is too small");
    for(int i = counts.size(); i < numDim; i++) {
      String key = "UNOBSERVED"+i;
      if(counts.containsKey(key))
        throw new RuntimeException("Our hacky plan was foiled");
      probs.put(key, Gamma.sample(random, pseudoCount, 1));
    }
    probs.multAll(1.0/probs.sum());
    return probs;
  }

  // Helpful for computing the posterior (see MargSparseMultinomial)
  public SparseDirichlet withExtraCounts(TDoubleMap extraCounts) {
    SparseDirichlet newDistrib = new SparseDirichlet(numDim, pseudoCount);
    newDistrib.counts.incrMap(counts, 1.0);
    newDistrib.counts.incrMap(extraCounts, 1.0);
    newDistrib.totalCount += counts.sum() + extraCounts.sum();
    return newDistrib;
  }

  // Expectations of canonical statistics
  public double expectedLog(Object key) {
    return DirichletUtils.expectedLog(getConcentration(key), totalCount);
  }

  public double crossEntropy(Distrib<TDoubleMap> _that) {
    SparseDirichlet that = (SparseDirichlet)_that;
    // Let q = p_this, p = p_that, \alpha_i be the parameters of p
    // \E_q \log p = \E_q \log Gamma(\sum\alpha_i) +
    //   \sum_i [ (\alpha_i-1) \E_q \log x_i - \log \Gamma(\alpha_i) ]
    double sum = DirichletUtils.thatTotalCountContrib(that.totalCount());
    int numDimHandled = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)counts) {
      double thisCon = this.pseudoCount + e.getValue();
      double thatCon = that.pseudoCount + that.counts.get(e.getKey(), 0);
      sum += DirichletUtils.elementContrib(thisCon, thatCon, this.totalCount());
      numDimHandled++;
    }
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)that.counts) {
      if(this.counts.containsKey(e.getKey())) continue; // Already processed
      double thisCon = this.pseudoCount + this.counts.get(e.getKey(), 0);
      double thatCon = that.pseudoCount + e.getValue();
      sum += DirichletUtils.elementContrib(thisCon, thatCon, this.totalCount());
      numDimHandled++;
    }
    // The rest of the counts are just pseudoCount on both this.counts and that.counts
    if(numDimHandled > numDim) throw new RuntimeException("numDim is too small");
    double thisCon = this.pseudoCount;
    double thatCon = that.pseudoCount;
    sum += (numDim - numDimHandled) *
      DirichletUtils.elementContrib(thisCon, thatCon, this.totalCount());
    return sum;
  }

  public SparseDirichletInterface modeSpike() {
    return new DegenerateSparseDirichlet(this);
  }

  public String toString() {
    return String.format("Dir(numDim=%d,pseudoCount=%.2f,counts=%s)",
      numDim, pseudoCount, MapUtils.topNToString(counts, 20));
  }

  // Safe way of return the mode.
  // The mode when the concentration parameters are all > 1
  // is well-defined, but here, we hack up something when they're not.
  // Assume the concentration parameters are all at least pseudoCount.
  // In Dirichlet, we normalize to get the mode.
  // Here we want to maintain sparsity.
  public static double getMode(double concentration,
      double pseudoCount, double totalCount, int numDim) {
    // HACK: if some concentration parameters are less than one, this can do crazy stuff
    // Values returned for all keys might not constitute a consistent mode
    assert concentration >= pseudoCount : String.format("%f < %f", concentration, pseudoCount);
    assert totalCount >= pseudoCount*numDim;
    // Should be 1, but if pseudoCount < 1, then use that.
    double t = Math.min(pseudoCount, 1);

    // The effect of this is that if all concentration parameters are
    // pseudoCount, then return whatever.
    if(totalCount <= t*numDim) return 0.12345;

    double x = (concentration-t) / (totalCount-t*numDim);
    return NumUtils.bound(x, DistribUtils.margin, 1-DistribUtils.margin);
  }
}
