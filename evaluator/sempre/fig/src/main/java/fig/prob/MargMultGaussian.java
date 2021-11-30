package fig.prob;

import java.util.*;
import java.io.*;
import fig.basic.*;

import Jama.Matrix;

public class MargMultGaussian implements MargDistrib<NormalInverseWishart>
{
  private NormalInverseWishartDistrib meanVarDistrib; // prior over mean and covar matrix
  
  public MargMultGaussian(NormalInverseWishartDistrib prior)
  {
    this.meanVarDistrib = prior;
  }
  
  //\log p(stats) (marginalizing out parameters)
  public double margLogLikelihood(SuffStats stats)
  {
    // Compute using Bayes rule, a = (0, 1)
    double sum = 0; 
    sum += meanVarDistrib.unNormalizedLogProb(MultGaussian.getZeroVector(dim()), MultGaussian.getIdentityMtx(dim())); // p(theta = a)
    sum += MultGaussian.getStdNormal(dim()).logProb((MultGaussianSuffStats)stats); // p(x | theta = a)
    sum -= getPosterior((MultGaussianSuffStats)stats).meanVarDistrib.unNormalizedLogProb(MultGaussian.getZeroVector(dim()), MultGaussian.getIdentityMtx(dim())); // p(theta = a | x)
    return sum;
  }
  //\log p(predStats | condStats) (marginalizing out parameters)
  public double predLogLikelihood(SuffStats condStats, SuffStats predStats)
  {
    return getPosterior((MultGaussianSuffStats)condStats).margLogLikelihood(predStats);
  }
  
  /**
   * See Erik Sudderth thesis, p.44
   * @param observation
   * @return
   */
  public MargMultGaussian getPosterior(SuffStats stats)
  {
    MultGaussianSuffStats observation = (MultGaussianSuffStats)stats;
    Matrix sumObs = new Matrix(observation.getSum(), observation.dim());
    Matrix outerProducts = new Matrix(observation.getOuterProduct());
    double kappaPrime = meanVarDistrib.getKappa() + observation.numPoints();
    double nuPrime = meanVarDistrib.getNu() + observation.numPoints(); 
    // TODO : do these operation in place for efficiency
    Matrix scriptVPrime = (meanVarDistrib.getScriptV().times(meanVarDistrib.getKappa()).plus(sumObs)).times(1.0/kappaPrime);
    // delta prime now
    Matrix t1 = meanVarDistrib.getDelta().times(meanVarDistrib.getNu());
    // TODO : cache this term
    Matrix t2 = meanVarDistrib.getScriptV().times(meanVarDistrib.getScriptV().transpose()).times(meanVarDistrib.getKappa());
    Matrix t3 = scriptVPrime.times(scriptVPrime.transpose()).times(kappaPrime);
    Matrix deltaPrime = (t1.plus(t2).minus(t3).plus(outerProducts)).times(1.0/nuPrime); // GOD ! bug found plus --> minus!
    return new MargMultGaussian(new NormalInverseWishartDistrib(kappaPrime, scriptVPrime, nuPrime, deltaPrime));
  }
  
  public double logProb(SuffStats stats) {
    throw Exceptions.unimplemented;
  }
  public double logProbObject(NormalInverseWishart distrib) {
    throw Exceptions.unimplemented;
  }
  public double crossEntropy(Distrib<NormalInverseWishart> distrib) {
    throw Exceptions.unimplemented;
  }
  public double expectedLogLikelihood(SuffStats stats) {
    throw Exceptions.unimplemented;
  }

  public NormalInverseWishart sampleObject(Random random) {
    return meanVarDistrib.sampleObject(random);
  }

  public int dim()
  {
    return meanVarDistrib.dim();
  }

  public static void main(String [] args)
  {
    // prior
    double nu = 4.0;
    Matrix scriptV = new Matrix(1, 1); scriptV.set(0, 0, 5.0);
    Matrix delta = new Matrix(1, 1); delta.set(0, 0, 1.0);
    double kappa = 1.0;
    NormalInverseWishartDistrib prior = 
      new NormalInverseWishartDistrib(kappa, scriptV, nu, delta);
    // observations: a list of 10 normal(0, 5)
    double [] mean = {30.0};
    double [][] variance = {{1.0}};
    MultGaussian g = new MultGaussian(mean, variance);
    MultGaussianSuffStats observations =
      new MultGaussianSuffStats(1);
    Random random = new Random();
    for (int i = 0; i < 10000; i++)
    {
      observations.add(g.sample(random));
    }
    /*double offset = 50.0;
    double [] obs1 = {-1.0 + offset};
    double [] obs2 = {1.0 + offset};
    observations.add(obs1); observations.add(obs2);*/
    // update posterior
    MargMultGaussian margGaussian = new MargMultGaussian(prior);
    MargMultGaussian posterior = margGaussian.getPosterior(observations);
    System.out.println(posterior.meanVarDistrib.expectedVariance().get(0, 0));
  }
}
