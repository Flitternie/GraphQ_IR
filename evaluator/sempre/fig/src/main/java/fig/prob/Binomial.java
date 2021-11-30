package fig.prob;

import java.util.*;
import fig.basic.*;

public class Binomial implements Distrib<Boolean> {
  private double prob;

  public Binomial(double prob) { this.prob = prob; }

  public static double logProb(double prob, boolean x) {
    return x ? Math.log(prob) : Math.log(1-prob);
  }
  public double logProb(boolean x) { return logProb(prob, x); }
  public double logProbObject(Boolean x) { return logProb(x); }
  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }

  public static boolean sample(Random random, double prob) {
    return random.nextDouble() < prob;
  }
  public boolean sample(Random random) { return sample(random, prob); }
  public Boolean sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Boolean> _that) {
    Binomial that = (Binomial)_that;
    return this.prob*Math.log(that.prob) + (1-this.prob)*Math.log(1-that.prob);
  }

  public double getProb() { return prob; }

  public String toString() { return String.format("Binomial(%.3f)", prob); }
}

