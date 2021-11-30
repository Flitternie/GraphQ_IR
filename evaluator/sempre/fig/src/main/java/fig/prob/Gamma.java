package fig.prob;

import java.util.*;
import fig.basic.*;

public class Gamma implements GammaInterface, java.io.Serializable {
  private static final long serialVersionUID = 42;

  private double shape, rate;

  public Gamma(double shape, double rate) {
    this.shape = shape;
    this.rate = rate;
  }

  public double logProb(double x) {
    // P(x|shape,rate) = rate^shape / Gamma(shape) * x^(shape-1) * e^(-rate*x)
    return shape*Math.log(rate) - NumUtils.logGamma(shape) +
      (NumUtils.equals(shape, 1) ? 0 : (shape-1)*Math.log(x)) - rate*x;
  }
  public double logProb(SuffStats stats) { throw new RuntimeException("Not implemented"); }
  public double logProbObject(Double x) { return logProb(x); }

  public double getShape() { return shape; }
  public double getRate() { return rate; }

  public double getMean() { return shape/rate; }
  public double getMode() { return Math.max((shape-1)/rate, DistribUtils.margin); }
  public double getVar() { return shape/(rate*rate); }

  public double sample(Random random) { return sample(random, shape, rate); }
  public static double sample(Random random, double shape, double rate) {
    return SampleUtils.sampleGamma(random, shape, rate);
  }
  public Double sampleObject(Random random) { return sample(random); }
  public double crossEntropy(Distrib<Double> _that) {
    Gamma that = (Gamma)_that;
    double sum = 0;
    sum += that.shape*Math.log(that.rate) - NumUtils.logGamma(that.shape);
    sum += (NumUtils.equals(that.shape, 1) ? 0 : (that.shape-1)*this.expectedLog()) - that.rate*this.getMean();
    return sum;
  }
  public double expectedLog() {
    // Write the Gamma distribution in canonical exponential family form,
    // so log partition function is \log \Gamma(shape) - shape \log rate
    // Take the derivative with respect to the canonical parameter (shape-1)
    // to get the mean of \log x
    return NumUtils.digamma(shape) - Math.log(rate);
  }

  public GammaInterface modeSpike() {
    return new DegenerateGamma(getMode());
  }

  public String toString() {
    return String.format("Gamma(%.3f,%.3f)", shape, rate);
  }
}
