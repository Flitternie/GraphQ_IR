package fig.prob;

import java.util.*;
import fig.basic.*;
import static fig.basic.LogInfo.*;

public class DirichletUtils {
  // \E \log p_i = i-th partial derivative of the partition function
  public static double expectedLog(double count, double totalCount) {
    double x = NumUtils.digamma(count) - NumUtils.digamma(totalCount);
    if(!NumUtils.isFinite(x))
      throw Exceptions.bad("count=%f, totalCount=%f", count, totalCount);
    return x;
  }

  // For computing cross-entropy for Beta/Dirichlet distributions
  // \E_{p_this} \log p_that
  public static double thatTotalCountContrib(double thatTotalCount) {
    return NumUtils.logGamma(thatTotalCount);
  }
  public static double elementContrib(double thisCount, double thatCount,
      double thisTotalCount) {
    return (thatCount-1)*expectedLog(thisCount, thisTotalCount) -
      NumUtils.logGamma(thatCount);
  }

  // Return $\Gamma(a+n)/\Gamma(a)$
  public static double logGammaRatio(double a, double n) {
    if(n == 1) return Math.log(a);
    return NumUtils.logGamma(a+n) - NumUtils.logGamma(a);
  }

  // For variational learning, we need a log of exp \E log operations,
  // which can be expensive.
  // Note that that function boils down to basically computing exp(digamma),
  // which has a very simple shape.
  // The function converges to x-0.5 as x increases,
  // so we can cache the values from [0, fastExpMaxRange)
  private static double fastExpMaxRange = 100;
  private static double[] fastExpDigammaBuckets;
  public static double fastExpDigamma(double count) { // if count == 0, return 0
    assert count >= 0 : count;
    if(count >= fastExpMaxRange) return count - 0.5;
    if(fastExpDigammaBuckets == null) {
      // Compute the lookup table
      fastExpDigammaBuckets = new double[1000000];
      for(int i = 1; i < fastExpDigammaBuckets.length; i++) {
        double icount = fastExpMaxRange*i/fastExpDigammaBuckets.length;
        fastExpDigammaBuckets[i] = Math.exp(NumUtils.digamma(icount));
      }
    }
    // Could make it accurate by interpolating, but it doesn't matter
    // Warning: we are sometimes rounding things to exactly 0 when they shouldn't be
    int i = (int)(fastExpDigammaBuckets.length*count/fastExpMaxRange+0.5);
    if(i >= fastExpDigammaBuckets.length) i = fastExpDigammaBuckets.length-1;
    return fastExpDigammaBuckets[i];
  }
  public static double[] fastExpExpectedLog(double[] counts) {
    int n = counts.length;
    double[] scores = new double[n];
    double normalizer = fastExpDigamma(ListUtils.sum(counts));
    for(int i = 0; i < n; i++)
      scores[i] = fastExpDigamma(counts[i]) / normalizer;
    return scores;
  }
  // In place do it in place (like normalize())
  public static boolean fastExpExpectedLogMut(double[] counts) {
    int n = counts.length;
    double normalizer = fastExpDigamma(ListUtils.sum(counts));
    if(normalizer == 0) return false;
    for(int i = 0; i < n; i++)
      counts[i] = fastExpDigamma(counts[i]) / normalizer;
    return true;
  }

  public static double[] expExpectedLog(double[] counts) {
    int n = counts.length;
    double[] scores = new double[n];
    double normalizer = Math.exp(NumUtils.digamma(ListUtils.sum(counts)));
    for(int i = 0; i < n; i++)
      scores[i] = Math.exp(NumUtils.digamma(counts[i])) / normalizer;
    return scores;
  }

  public static void main(String[] args) {
    /*for(double x = 0.0003; x < 1000; x += 0.1) {
      System.out.println(x + " " + (fastExpDigamma(x)-Math.exp(NumUtils.digamma(x))));
    }*/

    /*double beta = 7;
    double count1 = 50;
    double count2 = 40;
    double theta = 0.25;
    System.out.println(-beta*NumUtils.digamma(beta*theta) + beta*count1);
    System.out.println(-beta*NumUtils.digamma(beta*theta) + beta*count2);*/
    double[] counts = new double[] { 3, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0 };
    double alpha = 1.0; ///counts.length;
    double[] prior = ListUtils.newDouble(counts.length, alpha);

    System.out.println(counts.length);
    double[] hack = expExpectedLog(ListUtils.add(counts, prior));
    System.out.println(Fmt.D(hack));
    System.out.println("sum = " + ListUtils.sum(hack));
    System.out.println("norm = " + Fmt.D(norm(hack)));
    System.out.println("MLE = " + Fmt.D(norm(counts)));
  }
  static double[] norm(double[] x) {
    x = (double[])x.clone();
    NumUtils.normalize(x);
    return x;
  }
}
