package fig.prob;

import java.util.*;
import fig.basic.*;

public class Multinomial implements Distrib<Integer> {
  private double[] probs;

  public Multinomial(double[] probs) { this.probs = probs; }

  public static double logProb(double[] probs, int x) {
    return Math.log(probs[x]);
  }
  public double logProb(int x) { return logProb(probs, x); }
  public double logProb(SuffStats stats) {
    double sum = 0;
    for(int i = 0; i < probs.length; i++)
      sum += ((MultinomialSuffStats)stats).getCount(i) * logProb(i);
    return sum;
  }
  public double logProbObject(Integer x) { return logProb(x); }

  public static int sample(Random random, double[] probs) {
    double v = random.nextDouble();
    double sum = 0;
    for(int i = 0; i < probs.length; i++) {
      sum += probs[i]; 
      if(v < sum) return i;
    }
    throw new RuntimeException(sum + " < " + v);
  }
  public int sample(Random random) { return sample(random, probs); }
  public Integer sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Integer> _that) {
    Multinomial that = (Multinomial)_that;
    double sum = 0;
    for(int i = 0; i < probs.length; i++)
      sum += this.probs[i] * Math.log(that.probs[i]);
    return sum;
  }

  public double[] getProbs() { return probs; }

  public String toString() { return String.format("Multinomial(%s)", Fmt.D(probs)); }
}

