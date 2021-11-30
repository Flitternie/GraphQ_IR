package fig.prob;

import java.util.*;
import java.io.*;

import Jama.Matrix;

/**
 * Distribution over real vectors.
 */
public class NormalInverseWishart implements Distrib<double[]>
{
  private double[] mean;
  private Matrix covar;

  public NormalInverseWishart(double[] mean, Matrix covar) {
    this.mean = mean;
    this.covar = covar;
  }

  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(double[] x) {
    throw new RuntimeException("Not supported");
  }
  public double[] sampleObject(Random random) {
    throw new RuntimeException("Not supported");
  }
  public double crossEntropy(Distrib<double[]> _that) {
    throw new RuntimeException("Not supported");
  }
}
