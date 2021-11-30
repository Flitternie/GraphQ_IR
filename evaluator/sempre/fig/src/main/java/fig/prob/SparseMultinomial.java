package fig.prob;

import java.util.*;
import fig.basic.*;

public class SparseMultinomial implements Distrib<Object> {
  private TDoubleMap probs;

  public SparseMultinomial(TDoubleMap probs) { this.probs = probs; }

  public double logProb(Object x) { return Math.log(probs.get(x, 0)); }
  public double logProb(SuffStats _stats) {
    SparseMultinomialSuffStats stats = (SparseMultinomialSuffStats)_stats;
    double sum = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)stats)
      sum += e.getValue() * logProb(e.getKey());
    return sum;
  }
  public double logProbObject(Object x) { return logProb(x); }

  public static Object sample(Random random, TDoubleMap probs) {
    double v = random.nextDouble();
    double sum = 0;
    for(TDoubleMap.Entry e : (Iterable<TDoubleMap.Entry>)probs) {
      sum += e.getValue();
      if(v < sum) return e.getKey();
    }
    throw new RuntimeException(sum + " < " + v);
  }
  public Object sample(Random random) { return sample(random, probs); }
  public Object sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Object> _that) {
    throw new RuntimeException("Not implemented");
  }

  public TDoubleMap getProbs() { return probs; }

  public String toString() {
    return String.format("Multinomial(%s)", MapUtils.topNToString(probs, 30));
  }
}
