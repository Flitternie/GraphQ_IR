package fig.prob;

import java.util.*;
import fig.basic.*;

public class DegenerateGamma implements GammaInterface {
  private double value;

  public DegenerateGamma(double value) {
    this.value = value;
  }

  public double logProb(SuffStats stats) { throw Exceptions.unsupported; }
  public double logProbObject(Double x) { throw Exceptions.unsupported; }

  public double getShape() { throw Exceptions.unsupported; }
  public double getRate() { throw Exceptions.unsupported; }

  public double getMean() { return value; }
  public double getMode() { return value; }
  public double getVar() { return 0; }

  public Double sampleObject(Random random) { return value; }
  public double crossEntropy(Distrib<Double> _that) {
    if(_that instanceof DegenerateGamma) return 0;
    Gamma that = (Gamma)_that;
    return that.logProb(value);
  }
  public double expectedLog() { return Math.log(value); }

  public GammaInterface modeSpike() { return this; }

  public String toString() {
    return String.format("DegenerateGamma(%.3f)", value);
  }
}
