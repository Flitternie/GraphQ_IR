package fig.prob;

import java.util.*;
import fig.basic.*;

public class DegenerateSparseDirichlet implements SparseDirichletInterface {
  private SparseDirichlet parent;

  public DegenerateSparseDirichlet(SparseDirichlet parent) {
    this.parent = parent;
  }

  public int dim() { return parent.dim(); }

  //public SparseDirichlet getParent() { return parent; }

  public double getMean(Object key) { return parent.getMode(key); }
  public double getMode(Object key) { return parent.getMode(key); }

  public double getConcentration(Object key) { return Double.POSITIVE_INFINITY; }
  public double totalCount() { return Double.POSITIVE_INFINITY; }

  // Expectations of canonical statistics
  public double expectedLog(Object key) { return Math.log(getMode(key)); }

  public TDoubleMap sampleObject(Random random) { throw Exceptions.unsupported; }
  public double logProb(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProbObject(TDoubleMap x) { throw Exceptions.unsupported; }

  public double crossEntropy(Distrib<TDoubleMap> _that) {
    if(_that instanceof DegenerateSparseDirichlet) return 0;
    SparseDirichlet that = (SparseDirichlet)_that;
    // Return that.logProb(this.getMode())
    // But we don't have a getMean() function exactly.
    // Let q = p_this, p = p_that, \alpha_i be the parameters of p
    // \E_q \log p = \E_q \log Gamma(\sum\alpha_i) +
    //   \sum_i [ (\alpha_i-1) \E_q \log x_i - \log \Gamma(\alpha_i) ]
    double sum = NumUtils.logGamma(that.totalCount());
    int numDimHandled = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)parent.counts) {
      double thisCon = this.getMode(e.getKey());
      double thatCon = that.pseudoCount + that.counts.get(e.getKey(), 0);
      sum += (thatCon-1)*Math.log(thisCon) - NumUtils.logGamma(thatCon);
      numDimHandled++;
    }
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)that.counts) {
      if(parent.counts.containsKey(e.getKey())) continue; // Already processed
      double thisCon = this.getMode(e.getKey());
      double thatCon = that.pseudoCount + e.getValue();
      sum += (thatCon-1)*Math.log(thisCon) - NumUtils.logGamma(thatCon);
      numDimHandled++;
    }
    // The rest of the counts are just pseudoCount on both this.counts and that.counts
    if(numDimHandled > parent.numDim) throw new RuntimeException("numDim is too small");
    double thisCon = SparseDirichlet.getMode(parent.pseudoCount, parent.pseudoCount, parent.totalCount(), dim());
    double thatCon = that.pseudoCount;
    sum += (parent.numDim - numDimHandled) *
      ((thatCon-1)*Math.log(thisCon) - NumUtils.logGamma(thatCon));
    NumUtils.assertIsFinite(sum);
    return sum;
  }

  public SparseDirichletInterface modeSpike() { return this; }

  public String toString() { return "Degenerate"+parent; }
}
