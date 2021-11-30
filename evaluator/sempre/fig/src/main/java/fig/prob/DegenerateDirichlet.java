package fig.prob;

import java.util.*;
import fig.basic.*;

/*
 * IMPORTANT: override all the Dirichlet functions.
 * This should really be not a subclass, but
 * there should be a Dirichlet
 * should be an interface with a degenerate and a non-degenerate
 * implementation.
 * FUTURE: do this.
 */
public class DegenerateDirichlet implements DirichletInterface {
  private double[] value; // Degenerate at this value

  public DegenerateDirichlet(double[] value) {
    this.value = value;
  }

  public double[] getMean() { return value; }
  public double[] getMode() { return value; }
  //public double[] getValue() { return value; }
  public double getAlpha(int i) { return Double.POSITIVE_INFINITY; }
  public double totalCount() { return Double.POSITIVE_INFINITY; }

  // Compute log probability
  public double logProb(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProbObject(double[] x) { throw Exceptions.unsupported; }
  public double[] sampleObject(Random random) { return value; }

  public double crossEntropy(Distrib<double[]> _that) {
    if(_that instanceof DegenerateDirichlet) return 0;
    Dirichlet that = (Dirichlet)_that;
    return that.logProb(value);
  }
  public double expectedLog(int i) { return Math.log(value[i]); }
  public double[] expectedLog() {
    double[] result = new double[dim()];
    for(int i = 0; i < dim(); i++)
      result[i] = expectedLog(i);
    return result;
  }

  public DirichletInterface modeSpike() { return this; }

  public int dim() { return value.length; }

  public String toString() {
   return String.format("DegenerateDirichlet(%s)", Fmt.D(value));
  }
}
