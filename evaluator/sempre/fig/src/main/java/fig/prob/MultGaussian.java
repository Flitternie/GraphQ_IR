package fig.prob;

import java.util.*;
import java.io.*;

import Jama.CholeskyDecomposition;
import Jama.Matrix;

public class MultGaussian implements Distrib<double[]>
{
  private Matrix mean;
  private Matrix covar;

  public MultGaussian(double[] mean, double[][] covar) {
    this.mean = new Matrix(mean, mean.length);
    this.covar = new Matrix(covar);
  }

  /**
   * To compute the logProb from the suff stats:
   * Expand the bilinear forms (x_i - mean)^T covar^-1 (x_i - mean), and
   * note that the terms (\sum_i x_i^T) covar^-1 (\sum_i x_i) are equal to 
   * aggregatePtwiseProduct(outerproduct sufficient stats, covar^-1)
   * @param stats
   * @return
   */
  public double logProb(SuffStats _stats) {
    MultGaussianSuffStats stats = (MultGaussianSuffStats)_stats;
    // TODO: cache the normalizer
    double normalizer = 0.5 * Gaussian.LOG_INV_SQRT_2_PI * stats.dim() - covar.det() * 0.5;
    // TODO : cache this (not that important for now, always id)
    Matrix inv = covar.inverse();
    // t1, t2, t3 and t4 are the terms obtained by expanding the bilinear form
    double t1 = aggregatePtwiseProduct(stats.getMtxOuterProduct(), inv);
    // TODO : cache this
    double t2 = mean.transpose().times(inv).times(mean).get(0, 0) * stats.numPoints();
    // TODO : do some of this in place
    double t3 = - stats.getMtxSum().transpose().times(inv).times(mean).get(0, 0);
    double t4 = - mean.transpose().times(inv).times(stats.getMtxSum()).get(0, 0);
    return (normalizer - 0.5 * (t1 + t2 + t3 + t4));
  }
  public double logProbObject(double[] x) {
    return logProb(new MultGaussianSuffStats(x));
  }
  
  private CholeskyDecomposition chol = null;
  private CholeskyDecomposition getChol()
  {
    if (chol != null)
    {
      return chol;
    }
    chol = covar.chol();
    return chol;
  }
  
  public double [] sample(Random random)
  {
    Matrix L = getChol().getL();
    // start with a vector of iid std normals
    Matrix stdNormal = new Matrix(dim(), 1);
    for (int i = 0; i < dim(); i++)
    {
      stdNormal.set(i, 0, SampleUtils.sampleGaussian(random));
    }
    Matrix result = L.times(stdNormal);
    result.plusEquals(mean);
    return result.getColumnPackedCopy();
  }
  public double[] sampleObject(Random random) { return sample(random); }
 
  public double crossEntropy(Distrib<double[]> _that) {
    throw new RuntimeException("unsupported");
  }

  public static void main(String [] args)
  {
    double [] mean = {1.0, 2.0};
    double [][] covar = new double[2][2];
    covar[0][0] = 1.0;
    covar[1][1] = 4.0;
    covar[0][1] = 1.0;
    covar[1][0] = 1.0;
    MultGaussian g = new MultGaussian(mean, covar);
    Random random = new Random();
    for (int i = 0; i < 10000; i++)
    {
      System.out.println(Arrays.toString(g.sample(random)));
    }
  }
  
  /**
   * Given matrices m1 = (a_{i,j}) and m2 = (b_{i,j}) computes
   * \sum_i \sum_j a_{i,j} * b{i,j}
   * @param m1
   * @param m2
   * @return
   */
  public static double aggregatePtwiseProduct(Matrix m1, Matrix m2)
  {
    assert m1.getRowDimension() == m2.getRowDimension();
    assert m1.getColumnDimension() == m2. getColumnDimension();
    double sum = 0.0;
    for (int i = 0; i < m1.getRowDimension(); i++)
    {
      for (int j = 0; j < m1.getColumnDimension(); j++)
      {
        sum = sum + m1.get(i, j) * m2.get(i, j);
      }
    }
    return sum;
  }

  public int dim() { return covar.getRowDimension(); }
  
  private static MultGaussian stdNormal = null;
  /**
   * 
   * @param n The dimensionality
   * @return
   */
  public static MultGaussian getStdNormal(int n)
  {
    if (stdNormal != null && stdNormal.dim() == n)
    {
      return stdNormal;
    }
    stdNormal = new MultGaussian(getZeroVector(n), getIdentityMtx(n));
    return stdNormal;
  }
  private static double [] zeroVector;
  public static double [] getZeroVector(int n)
  {
    if (zeroVector != null && zeroVector.length == n)
    {
      return zeroVector;
    }
    zeroVector = new double[n];
    for (int i = 0; i < n; i++)
    {
      zeroVector[i] = 0.0;
    }
    return zeroVector;
  }
  private static double [][] identityMtx;
  public static double [][] getIdentityMtx(int n)
  {
    if (identityMtx != null && identityMtx.length == n)
    {
      return identityMtx;
    }
    identityMtx = new double[n][n];
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        if (i != j)
        {
          identityMtx[i][j] = 0.0;
        }
        else
        {
          identityMtx[i][j] = 1.0;
        }
      }
    }
    return identityMtx;
  }

public double[] getMean()
{
	return mean.getArray()[0];
}

public double[][] getCovar()
{
	return covar.getArray();
}

public Matrix getCovarMatrix()
{
	return covar;
}
}
