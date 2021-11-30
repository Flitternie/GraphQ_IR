package fig.prob;

import java.util.*;
import fig.basic.*;

public class InvGamma implements Distrib<Double> {
  private double shape, rate;

  public InvGamma(double shape, double rate) {
    this.shape = shape;
    this.rate = rate;
  }

  public double logProb(double x) {
    // P(x|shape,rate) = shape^rate / Gamma(shape) * x^(-shape-1) * e^(-rate/x)
    return rate*Math.log(shape) - NumUtils.logGamma(shape) +
      (-shape-1)*Math.log(x) - rate/x;
  }
  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(Double x) { return logProb(x); }

  public double getShape() { return shape; }
  public double getScale() { return rate; }

  public double getMean() { return rate/(shape-1); }
  public double getVar() { return rate*rate / ((shape-1)*(shape-1)*(shape-2)); }

  public double sample(Random random) { return sample(random, shape, rate); }
  public static double sample(Random random, double shape, double rate) {
    return 1.0/SampleUtils.sampleGamma(random, shape, rate);
  }
  public Double sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Double> _that) {
    throw new RuntimeException("Not implemented");
  }

  public String toString() {
    return String.format("InvGamma(%.3f,%.3f)", shape, rate);
  }
}
