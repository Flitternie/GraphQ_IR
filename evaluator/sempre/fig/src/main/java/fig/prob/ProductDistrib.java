package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * Product distribution.
 */
public class ProductDistrib implements Distrib<Object[]> {
  private Distrib[] distribs;

  public ProductDistrib(Distrib[] distribs) {
    this.distribs = distribs;
  }

  public double logProb(Object[] x) {
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += distribs[i].logProbObject(x[i]);
    return sum;
  }
  public double logProb(SuffStats stats) {
    double sum = 0;
    for(int i = 0; i < dim(); i++)
      sum += distribs[i].logProb(((ProductSuffStats)stats).getComponent(i));
    return sum;
  }
  public double logProbObject(Object[] x) { return logProb(x); }

  public Object[] sample(Random random) {
    Object[] x = new Object[dim()];
    for(int i = 0; i < dim(); i++)
      x[i] = distribs[i].sampleObject(random);
    return x;
  }
  public Object[] sampleObject(Random random) { return sample(random); }

  public double crossEntropy(Distrib<Object[]> _that) {
    throw new RuntimeException("unsupported");
  }

  public Distrib getComponent(int i) { return distribs[i]; }
  public int dim() { return distribs.length; }

  public String toString() { return StrUtils.join(distribs); }
}
