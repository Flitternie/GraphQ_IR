package fig.prob;

import java.util.*;
import java.io.*;

import Jama.Matrix;

public class NormalInverseWishartDistrib implements Distrib<NormalInverseWishart>
{
  // hyperparameters for the prior on the covariance matrices
  private double nu; // degrees of freedom
  private Matrix delta; // n by n mtx
  
  // hyperparameters for the prior on the means
  private Matrix scriptV; // n by 1 vector, the expected mean
  private double kappa; // for which we have kappa pseudo-observations

  // TODO: offer constructors from cholesky-decomposed parameters?... why? maybe not needed
 
  public NormalInverseWishartDistrib(double kappa, Matrix scriptV, double nu, Matrix delta) 
  {
    if (kappa <= 0)
    {
      throw new RuntimeException("kappa " + kappa + " should be > 0");
    }
    if (nu <= delta.getColumnDimension() + 1)
    {
      throw new RuntimeException("nu " + nu + " should be > d + 1, d = " + delta.getColumnDimension());
    }
    this.nu = nu;
    this.delta = delta;
    this.scriptV = scriptV;
    this.kappa = kappa;
  }
  public NormalInverseWishartDistrib(double kappa, double [] scriptV, double nu, double [][] delta)
  {
    this(kappa, new Matrix(scriptV, scriptV.length), nu, new Matrix(delta));
  }

  /**
   * Unnormalized log prob
   * 
   * WARNING: CURRENTLY ASSUMES THE PROVIDED COVAR IS THE IDENTITY!!!!!
   * 
   * See Erik Sudderth thesis
   * 
   * @param mean
   * @param covar
   * @return
   */
  public double unNormalizedLogProb(double[] mean, double[][] covar)
  {
    Matrix mu = new Matrix(mean, mean.length);
    Matrix lambda = new Matrix(covar);
    // TODO : use a Cholesky decomposition instead... why? maybe not needed
    // 1 - normalizer  TODO : cache me
    //  Note that we are so sloppy with inverses here because with the current 
    // code, only identity matrices are considered
    assert isIdentity(lambda);
    double determinant = 1.0; //lambda.det();
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! see above
    double exponent = -((nu + dim()) / 2.0 + 1.0); // sign problems fixed
    // not actually the whole normalization...
    double normalizer = exponent * Math.log(determinant); // log (determinant ^ exponent)
    // 2 - main piece
    // Note that we are so sloppy with inverses here because with the current 
    // code, only identity matrices are considered
    Matrix inverse = lambda; //lambda.inverse();
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! see above
    double t1 = -0.5 * delta.times(inverse).trace();
    double t2 = -kappa/2.0 * norm(inverse, mu.minus(scriptV));
    return normalizer + t1 + t2;
  }

  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(NormalInverseWishart x) {
    throw new RuntimeException("Not supported right now");
  }
  public NormalInverseWishart sampleObject(Random random) {
    throw new RuntimeException("Not supported right now");
  }
  public double crossEntropy(Distrib<NormalInverseWishart> _that) {
    throw new RuntimeException("Not supported");
  }
  
  private boolean isIdentity(Matrix lambda)
  {
    for (int i = 0; i < lambda.getRowDimension(); i++)
    {
      for (int j = 0; j < lambda.getColumnDimension(); j++)
      {
        if (i == j)
        {
          if (lambda.get(i, j) != 1.0)
          {
            return false;
          }
        }
        else if (lambda.get(i, j) != 0.0)
        {
          return false; 
        }
      }
    }
    return true;
  }
  /**
   * Compute the norm of a vector according to the inner product space with
   * the provided kernel
   * @param kernel
   * @param vector
   * @return
   */
  public static double norm(Matrix kernel, Matrix vector)
  {
    assert kernel.getColumnDimension() == kernel.getRowDimension();
    assert kernel.getColumnDimension() == vector.getRowDimension();
    assert vector.getColumnDimension() == 1;
    Matrix result = vector.transpose().times(kernel).times(vector);
    assert result.getColumnDimension() == 1;
    assert result.getRowDimension() == 1;
    return result.get(0, 0);
  }
  public Matrix expectedVariance()
  {
    double coefficient = nu / (nu - dim() - 1);
    return delta.times(coefficient);
  }
  public int dim()
  {
    return delta.getColumnDimension();
  }
  public Matrix getDelta()
  {
    return delta;
  }
  public double getKappa()
  {
    return kappa;
  }
  public double getNu()
  {
    return nu;
  }
  public Matrix getScriptV()
  {
    return scriptV;
  }
  @Override
  public String toString()
  {
    return "NIW(nu=" + nu + ", kappa=" + kappa + ")"; 
  }
}
