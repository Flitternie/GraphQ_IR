package fig.prob;

import java.util.*;
import fig.basic.*;

public class DegenerateBeta implements BetaInterface {
  private double value;

  public DegenerateBeta(double value) {
    this.value = value;
  }

  // Compute log probability
  public double logProb(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProbObject(Double x) { throw Exceptions.unsupported; }

  public Double sampleObject(Random random) { return value; }

  public double expectedLog(boolean b) {
    if(b) return Math.log(value);
    else  return Math.log(1-value);
  }

  public double crossEntropy(Distrib<Double> _that) {
    if(_that instanceof DegenerateBeta) return 0;
    Beta that = (Beta)_that;
    return that.logProb(value);
  }

  public double getMean() { return value; }
  public double getMode() { return value; }
  public BetaInterface modeSpike() { return this; }

  public double getAlpha() { return Double.POSITIVE_INFINITY; }
  public double getBeta() { return Double.POSITIVE_INFINITY; }
  public double totalCount() { return Double.POSITIVE_INFINITY; }

  public String toString() {
    return String.format("DegenerateBeta(%.3f)", value);
  }
}
