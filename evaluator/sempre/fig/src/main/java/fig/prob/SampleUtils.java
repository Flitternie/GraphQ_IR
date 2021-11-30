package fig.prob;

import java.util.*;
import fig.basic.*;

public class SampleUtils {
  public static int[] samplePermutation(Random random, int n) {
    int[] perm = new int[n];
    for(int i = 0; i < n; i++) perm[i] = i;
    for(int i = 0; i < n-1; i++) {
      int j = i+random.nextInt(n-i);
      int tmp = perm[i]; perm[i] = perm[j]; perm[j] = tmp; // Swap
    }
    return perm;
  }

  // Return k of n integers uniformly at random
  public static <T> Pair<List<T>,List<T>> samplePartition(Random random, List<T> items, int k) {
    if (k > items.size()) throw new RuntimeException("Tried to select " + k + " (too many) of " + items.size() + " items");
    List<Integer> perm = new ArrayList<Integer>(items.size());
    for(int i = 0; i < items.size(); i++) perm.add(i);
    for(int i = 0; i < k; i++) {
      int j = i+random.nextInt(items.size()-i);
      int tmp = perm.get(i); perm.set(i, perm.get(j)); perm.set(j, tmp); // Swap
    }
    List<Integer> perm1 = perm.subList(0, k);
    List<Integer> perm2 = perm.subList(k, items.size());
    Collections.sort(perm1);
    Collections.sort(perm2);
    List<T> result1 = new ArrayList<T>();
    for (int i : perm1) result1.add(items.get(i));
    List<T> result2 = new ArrayList<T>();
    for (int i : perm2) result2.add(items.get(i));
    return new Pair(result1, result2);
  }

  public static int sampleMultinomial(Random random, double[] probs) {
    double v = random.nextDouble();
    double sum = 0;
    for(int i = 0; i < probs.length; i++) {
      sum += probs[i]; 
      if(v < sum) return i;
    }
    throw new RuntimeException(sum + " < " + v);
  }

  public static double[] sampleUnitVector(Random random, int n) {
    double[] x = new double[n];
    for(int i = 0; i < n; i++) x[i] = random.nextDouble()-0.5;
    double norm = NumUtils.l2Norm(x);
    for(int i = 0; i < n; i++) x[i] /= norm;
    return x;
  }

  public static double sampleGamma(Random random, double a, double rate) {
    // G. Marsaglia and W.W. Tsang, A simple method for generating gamma
    // variables, ACM Transactions on Mathematical Software, Vol. 26, No. 3,
    // Pages 363-372, September, 2000.
    // http://portal.acm.org/citation.cfm?id=358414
    double boost;
    if(a < 1) {
      // boost using Marsaglia's (1961) method: gam(a) = gam(a+1)*U^(1/a)
      boost = Math.exp(Math.log(random.nextDouble())/a);
      ++a;
    } 
    else {
      boost = 1;
    }

    double d = a-1.0/3, c = 1.0/Math.sqrt(9*d);
    double v;
    while(true) {
      double x;
      do {
        x = sampleGaussian(random);
        v = 1+c*x;
      } while(v <= 0);
      v = v*v*v;
      x = x*x;
      double u = random.nextDouble();
      if((u < 1-.0331*x*x) || (Math.log(u) < 0.5*x + d*(1-v+Math.log(v)))) {
        break;
      }
    }
    return boost*d*v / rate;
  }

  public static double sampleErlang(Random random, int ia, double rate) {
    int j;
    double am,e,s,v1,v2,x,y;

    assert ia >= 1;
    if (ia < 6) {
      x=1.0;
      for (j=1;j<=ia;j++) x *= random.nextDouble();
      x = -Math.log(x);
    } 
    else {
      do {
        do {
          do {
            v1=2.0*random.nextDouble()-1.0;
            v2=2.0*random.nextDouble()-1.0;
          } while (v1*v1+v2*v2 > 1.0);
          y=v2/v1;
          am=ia-1;
          s=Math.sqrt(2.0*am+1.0);
          x=s*y+am;
        } while (x <= 0.0);
        e=(1.0+y*y)*Math.exp(am*Math.log(x/am)-s*y);
      } while (random.nextDouble() > e);
    }
    return x / rate;
  }

  // Return Gaussian(0, 1)
  public static double sampleGaussian(Random random) {
    // Use the Box-Muller Transformation
    // if x_1 and x_2 are independent uniform [0, 1],
    // then sqrt(-2 ln x_1) * cos(2*pi*x_2) is Gaussian with mean 0 and variance 1
    double x1 = random.nextDouble(), x2 = random.nextDouble();
    double z = Math.sqrt(-2*Math.log(x1))*Math.cos(2*Math.PI*x2);
    return z;
  }

  // Copied from numerical recipes 
  private static double oldm = -1, g, sq, alxm;
  public static double samplePoisson(Random random, double rate) {
    double xm = rate;
    double em, t, y;

    if (xm < 12.0) {
      if (xm != oldm) {
        oldm=xm;
        g=Math.exp(-xm);
      }
      em = -1;
      t=1.0;
      do {
        em += 1.0;
        t *= random.nextDouble();
      } while (t > g);
    } 
    else {
      if (xm != oldm) {
        oldm=xm;
        sq=Math.sqrt(2.0*xm);
        alxm=Math.log(xm);
        g=xm*alxm-NumUtils.logGamma(xm+1.0);
      }
      do 
      {
        do 
        {
          y=Math.tan(Math.PI*random.nextDouble());
          em=sq*y+xm;
        } while (em < 0.0);
        em=Math.floor(em);
        t=0.9*(1.0+y*y)*Math.exp(em*alxm-NumUtils.logGamma(em+1.0)-g);
      } while (random.nextDouble() > t);
    }
    return (int)em;
  }

  /**
   * From numerical recipes
   * http://www.fizyka.umk.pl/nrbook/c7-3.pdf
   * Returns as a floating-point number an integer value that is a random
   * deviate drawn from a binomial distribution of n trials each of probability
   * pp, using ran1(idum) as a source of uniform random deviates.
   */
  private static int nold=(-1);
  private static double pold=(-1.0),pc,plog,pclog,en,oldg;
  public static int sampleBinomial(Random random, int n, double pp) {
    int j;
    double am,em,g,angle,p,bnl,sq,t,y;
    p=(pp <= 0.5 ? pp : 1.0-pp);
    /* The binomial distribution is invariant under changing pp to 1-pp, if we
     * also change the answer to n minus itself; we’ll remember to do this
     * below. */

    am=n*p; // This is the mean of the deviate to be produced.
    if (n < 25) {
      // Use the direct method while n is not too large.
      bnl=0.0;
      for (j=1;j<=n;j++) if (random.nextDouble() < p) ++bnl;
    }
    else if (am < 1.0) {
      // If fewer than one event is expected out of 25 or more trials, then the
      // distribution is quite accurately Poisson. Use direct Poisson method.
      g=Math.exp(-am); t=1.0;
      for (j=0;j<=n;j++) { t *= random.nextDouble(); if (t < g) break; }
      bnl=(j <= n ? j : n);
    }
    else {
      // Use the rejection method.
      if (n != nold) {
        // If n has changed, then compute useful quantities.
        en=n; oldg=NumUtils.logGamma(en+1.0); nold=n;
      }
      if (p != pold) {
        // If p has changed, then compute useful quantities.
        pc=1.0-p; plog=Math.log(p); pclog=Math.log(pc); pold=p;
      }
      sq=Math.sqrt(2.0*am*pc);
      // The following code should by now seem familiar: rejection method with a Lorentzian comparison function.
      do {
        do { angle=Math.PI*random.nextDouble(); y=Math.tan(angle); em=sq*y+am; } while (em < 0.0 || em >= (en+1.0));
        // Reject. Trick for integer-valued distribution.
        em=Math.floor(em);
        t=1.2*sq*(1.0+y*y)*Math.exp(oldg-NumUtils.logGamma(em+1.0)-NumUtils.logGamma(en-em+1.0)+em*plog+(en-em)*pclog);
      } while (random.nextDouble() > t);
      // Reject. This happens about 1.5 times per deviate, on average.
      bnl=em; 
    }
    if (p != pp) bnl=n-bnl; // Remember to undo the symmetry transformation.
    return (int)bnl;
  }

  public static int[] sampleMultinomialNaive(Random random, int n, double[] probs) {
    int K = probs.length;
    int[] counts = new int[K];
    double massRemaining = 1.0;
    for (int i = 0; i < K-1; i++) {
      counts[i] = sampleBinomial(random, n, probs[i]/massRemaining);
      n -= counts[i];
      massRemaining -= probs[i];
    }
    counts[K-1] = n;
    return counts;
  }

  static class MultinomialSampler {
    Random random;
    double[] accumProbs;
    int[] counts;
    // Put n objects over items i,..,j-1
    private void sample(int n, int i, int j) {
      assert i < j : i + " " + j;
      if (i+1 == j) { counts[i] = n; return; }
      int k = (i+j)/2;
      double prob = (accumProbs[k]-accumProbs[i]) / (accumProbs[j]-accumProbs[i]);
      int m = sampleBinomial(random, n, prob);
      sample(m, i, k);
      sample(n-m, k, j);
    }
  }
  public static int[] sampleMultinomial(Random random, int n, double[] probs) {
    int K = probs.length;
    MultinomialSampler sampler = new MultinomialSampler();
    sampler.random = random;
    sampler.accumProbs = new double[K+1];
    for (int i = 0; i < K; i++)
      sampler.accumProbs[i+1] = sampler.accumProbs[i] + probs[i];
    sampler.counts = new int[K];
    sampler.sample(n, 0, K);
    return sampler.counts;
  }

  public static void main(String[] args) {
    Random random = new Random(1);
    /*StatFig fig = new StatFig();
    for(int i = 0; i < 100000; i++)
      //fig.add(sampleBinomial(random, 1000, 0.02));*/
    double[] probs = new double[] { 0.2, 0.7, 0.08, 0.02 };
    int K = probs.length;
    StatFig[] figs = new StatFig[K];
    for(int a = 0; a < K; a++) figs[a] = new StatFig();
    for(int i = 0; i < 100000; i++) {
      int[] counts = sampleMultinomial(random, 1000, probs);
      for(int a = 0; a < K; a++) figs[a].add(counts[a]);
    }
    for(int a = 0; a < K; a++) System.out.println(a +" ("+probs[a]+"): " + figs[a]);
  }
}
