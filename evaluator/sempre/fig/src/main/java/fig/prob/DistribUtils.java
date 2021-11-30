package fig.prob;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.*;

public class DistribUtils {
  // A default, not necessarily the fastest way, of implementing conditional probabilities
  public static double predLogLikelihood(MargDistrib margDistrib, SuffStats condSuffStats, SuffStats predSuffStats) {
    double oldLogProb = margDistrib.margLogLikelihood(predSuffStats);
    predSuffStats.add(condSuffStats);
    double newLogProb = margDistrib.margLogLikelihood(predSuffStats);
    predSuffStats.sub(condSuffStats);
    return newLogProb - oldLogProb;
  }

  public static double KL(Distrib d1, Distrib d2) {
    return d1.crossEntropy(d1) - d1.crossEntropy(d2);
  }

  // n data points, *total* squared deviation of v (sample deviation)
  /*public static InvGamma varLikelihood(int n, double v) {
    return new InvGamma(n/2.0-1, v/2);
  }*/

  public static <T> void verifyCrossEntropy(Distrib<T> d1, Distrib<T> d2) {
    // Verify that the cross-entropy computation agrees with the Monte
    // Carlo simulation
    Random random = new Random();
    StatFig fig = new StatFig();
    for(int i = 0; i < 100000; i++)
      fig.add(d2.logProbObject(d1.sampleObject(random)));
    double A = d1.crossEntropy(d2);
    double B = fig.mean();
    System.out.println(A + " " + B + " " + (A-B));
  }

  public static void verifyExpectedLogLikelihood(MargDistrib prior, SuffStats stats) {
    verifyExpectedLogLikelihood(prior, stats, 100000);
  }
  public static void verifyExpectedLogLikelihood(MargDistrib prior, SuffStats stats, int numSamples) {
    // Verify that the expected log-likelihood computation agrees with the Monte
    // Carlo simulation.
    Random random = new Random();
    StatFig fig = new StatFig();
    for(int i = 0; i < numSamples; i++) {
      Distrib param = (Distrib)prior.sampleObject(random);
      fig.add(param.logProb(stats));
    }
    double A = prior.expectedLogLikelihood(stats);
    double B = fig.mean();
    System.out.println(A + " " + B + " " + (A-B));
  }

  public static void verifyPassed() {
    // Cross-entropy
    verifyCrossEntropy(new Gaussian(2, 0.3), new Gaussian(8, 1.7));
    verifyCrossEntropy(new Gamma(2, 0.3), new Gamma(8, 1.7));
    verifyCrossEntropy(new Dirichlet(10, 0.3), new Dirichlet(10, 1.7));
    TDoubleMap m1 = new TDoubleMap();
    m1.put("A", 3); m1.put("B", 8); m1.put("C", 0);
    TDoubleMap m2 = new TDoubleMap();
    m2.put("A", 3); m1.put("B", 0); m2.put("C", 1);
    SparseDirichlet d1 = new SparseDirichlet(10, 0.3, m1);
    SparseDirichlet d2 = new SparseDirichlet(10, 1.7, m2);
    verifyCrossEntropy(d1, d2);

    // Expected log-likelihood
    verifyExpectedLogLikelihood(new MargMultinomial(new Dirichlet(5, 1.3)),
      new MultinomialSuffStats(new double[] { 4, 21, 0.3, 2, 4 }));
    TDoubleMap m = new TDoubleMap();
    m.put("A", 3); m.put("B", 8); m.put("C", 4);
    verifyExpectedLogLikelihood(new MargSparseMultinomial(new SparseDirichlet(10, 1.3, m)),
      new SparseMultinomialSuffStats(m));
    verifyExpectedLogLikelihood(new MargMeanGaussian(new Gaussian(0, 1), 1),
      new GaussianSuffStats(0, 0, 1));
    verifyExpectedLogLikelihood(new MargMeanGaussian(new Gaussian(2, 10), 0.7),
      new GaussianSuffStats(2, 10, 0.3), 1000000);
    verifyExpectedLogLikelihood(
      new MargMeanDiagMultGaussian(
        new DiagMultGaussian(new double[] {3,4,-2},
        new double[]{0.7,1.5,4.4}),
        new double[]{1.7,3.5,0.4}),
      new DiagMultGaussianSuffStats(new double[]{1,1,0},
        new double[]{8,4,3}, 0.37), 1000000);

    // Verify mean and expected log
    Random random = new Random();
    Gamma g = new Gamma(2, 0.3);
    StatFig fig = new StatFig();
    for(int i = 0; i < 10000; i++)
      //fig.add(g.sample(random));
      fig.add(Math.log(g.sample(random)));
    //System.out.println(g.getMean() + " " + fig.mean());
    System.out.println(g.expectedLog() + " " + fig.mean());
  }

  // To avoid infinities where the log probability blows up,
  // we will return a value (close to 0 or 1 in the Beta case)
  public static final double margin = 1e-8;

  public static void main(String[] args) {
    LogInfo.init();

    /*MargSparseMultinomial m = new MargSparseMultinomial(
      new SparseDirichlet(2, 1));
    System.out.println(m.expectedLogLikelihood(SparseMultinomialSuffStats.singleton("x")));
    Beta b;
    b = new Beta(1, 1); System.out.println(b.expectedLog(false));
    b = new Beta(2, 2); System.out.println(b.crossEntropy(b));
    b = new Beta(20, 20); System.out.println(b.crossEntropy(b));*/

    LogInfo.msPerLine = 0;

    //SparseDirichlet d = new SparseDirichlet(2, 0.001);
    //logs(d.expectedLog("F"));
    //logs(Math.log(Math.exp(d.expectedLog("F"))));

    DirichletInterface d1 = new Dirichlet(new double[] { 1+10000, 1, 1+1, 1 });
    DirichletInterface d2 = new Dirichlet(new double[] { 1+50000, 1, 1+5, 1 });

    logs(Math.exp(d1.expectedLog(2)) + " " + Math.exp(d1.expectedLog(3)));
    logs(Math.exp(d2.expectedLog(2)) + " " + Math.exp(d2.expectedLog(3)));

    d1 = d1.modeSpike();
    d2 = d2.modeSpike();

    logs(Math.exp(d1.expectedLog(2)) + " " + Math.exp(d1.expectedLog(3)));
    logs(Math.exp(d2.expectedLog(2)) + " " + Math.exp(d2.expectedLog(3)));
    
    /*Dirichlet d = new Dirichlet(new double[] { 0.1, 0.1, 1 });
    int N = 100;
    for(int i = 0; i < N; i++) {
      double x = (double)(i+1)/(N+1);
      for(int j = 0; j < N; j++) {
        double y = (double)(j+1)/(N+1);
        logs("point\t%f %f %f", x, y, d.logProb(new double[] { x, y, 1-x-y }));
      }
    }*/

    //Dirichlet d = new Dirichlet(new double[] { 0.1, 0.1, 1, 0.1 });
    //Dirichlet d = new Dirichlet(new double[] { 1, 1, 5, 1 });

    /*logs(StrUtils.join(d.getMean()));
    logs(StrUtils.join(d.getMode()));
    logs(StrUtils.join(ListUtils.expMut(d.expectedLog())));*/

    /*TDoubleMap a = TDoubleMap.newMap('a', 1, 'b', 4);
    SparseMultinomialSuffStats x = new SparseMultinomialSuffStats(
      TDoubleMap.newMap('a', 2, 'c', 1));
    MargSparseMultinomial m =
      new MargSparseMultinomial(new SparseDirichlet(10, 1, a));
    MargSparseMultinomial m2 = m.modeSpike();
    System.out.println(Math.exp(m2.margLogLikelihood(x)));
    System.out.println(Math.exp(m2.expectedLogLikelihood(x)));
    System.out.println(KL(m2, m));*/

    // Cross entropy
    // expected log likelihood
    // marg log likelihood

    /*System.out.println(Math.exp(b.expectedLog(true)));
    System.out.println(b.getMean());
    TDoubleMap c = new TDoubleMap();
    //c.put("a", 0.641);
    c.put("a", 1.641);
    c.put("b", 1);
    //SparseDirichlet d = new SparseDirichlet(2, 1, c);
    SparseDirichlet d = new SparseDirichlet(2, 0, c);
    d = d.modeSpike();
    System.out.println(Math.exp(d.expectedLog("a")));
    System.out.println(d.getMean("a"));
    System.out.println(Math.exp(d.expectedLog("b")));
    System.out.println(d.getMean("b"));*/
  }
}
