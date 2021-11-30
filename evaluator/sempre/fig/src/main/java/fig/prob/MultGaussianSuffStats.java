package fig.prob;

import java.util.*;
import java.io.*;

import Jama.Matrix;

public class MultGaussianSuffStats implements SuffStats
{
  private Matrix sum;
  private Matrix outerproducts;
  private int n;
  
  public MultGaussianSuffStats(int numDim) {
    double [] sum = new double[numDim];
    double [][] outerproducts = new double[numDim][numDim];
    n = 0;
    this.sum = new Matrix(sum, sum.length);
    this.outerproducts = new Matrix(outerproducts);
  }
  public MultGaussianSuffStats(double[] x) {
    sum = new Matrix(x, x.length);
    outerproducts = sum.times(sum.transpose());
    n = 1;
  }
  public MultGaussianSuffStats(MultGaussianSuffStats stats) {
    this.sum = stats.sum.copy();
    this.outerproducts = stats.outerproducts.copy();
  }

  public void add(double[] _x) { // Add a data point
    Matrix x = new Matrix(_x, _x.length);
    // TODO : in place for efficiency
    sum = sum.plus(x); 
    outerproducts = outerproducts.plus(x.times(x.transpose()));
    n++;
  }
  public void add(SuffStats _stats) { // Add several data points
    MultGaussianSuffStats stats = (MultGaussianSuffStats)_stats;
    // TODO : in place for efficiency
    sum = sum.plus(stats.sum);
    outerproducts = outerproducts.plus(stats.outerproducts);
    n += stats.n;
  }
  public void sub(double[] _x) { // Remove a data point
    Matrix x = new Matrix(_x, _x.length);
    // TODO : in place for efficiency
    sum = sum.minus(x); 
    outerproducts = outerproducts.minus(x.times(x.transpose()));
    n--;
  }
  public void sub(SuffStats _stats) { // Remove several data points
    MultGaussianSuffStats stats = (MultGaussianSuffStats)_stats;
    // TODO : in place for efficiency
    sum = sum.minus(stats.sum);
    outerproducts = outerproducts.minus(stats.outerproducts);
    n += stats.n;
  }

  public SuffStats reweight(double scale) {
    throw new RuntimeException("unsupported");
  }

  public double[] getSum() 
  {
    double [] result = new double[dim()];
    for (int i = 0; i < dim(); i++)
    {
      result[i] = getSum(i);
    }
    return result;
  }
  public double[][] getOuterProduct() { return outerproducts.getArray(); }
  public Matrix getMtxOuterProduct() { return outerproducts; }
  public double getSum(int i) { return sum.get(i, 0); }
  public Matrix getMtxSum() { return sum; }
  public double getOuterProduct(int i, int j) { return outerproducts.get(i, j); }
  public int numPoints() { return n; }
  public int dim() { return outerproducts.getRowDimension(); }
}
