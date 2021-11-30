package fig.basic;

import java.io.*;
import java.util.*;
import fig.basic.*;
import fig.exec.*;
import fig.record.*;
import fig.prob.*;
import static fig.basic.LogInfo.*;

/**
 * To handle a large range of numbers without the costly log/exp operations, we
 * implement our own floating point as follows:
 * We represent each non-negative number X as a mantissa part (M) and an
 * exponent part (E) so that X = M * BASE^E and 1/BASE <= X <= BASE.
 * 1/X is represented by 1/M and -E, which still satisifies the properties
 * above.
 */
class BigDouble {
  final static int MIN_E = -10000000;
  final static int MAX_E = +10000000;
  final static int VERY_SMALL_E = -10000;
  final static int VERY_BIG_E = +10000;

  final static int LOG_BASE = 50;
  final static double BASE = Math.exp(LOG_BASE);
  final static double INV_BASE = 1.0/BASE;
  final static double[] INV_BASE_POW = {
    Math.pow(INV_BASE, 0), Math.pow(INV_BASE, 1), Math.pow(INV_BASE, 2),
    Math.pow(INV_BASE, 3), Math.pow(INV_BASE, 4), Math.pow(INV_BASE, 5),
    Math.pow(INV_BASE, 6), Math.pow(INV_BASE, 7), Math.pow(INV_BASE, 8),
  };
  final static int NUM_INV_BASE_POW = INV_BASE_POW.length;
  final static double[] BASE_POW = {
    Math.pow(BASE, 0), Math.pow(BASE, 1), Math.pow(BASE, 2),
    Math.pow(BASE, 3), Math.pow(BASE, 4), Math.pow(BASE, 5),
    Math.pow(BASE, 6), Math.pow(BASE, 7), Math.pow(BASE, 8),
  };
  final static int NUM_BASE_POW = BASE_POW.length;

  public static BigDouble one() { return new BigDouble(1, 0); }
  public static BigDouble zero() { return new BigDouble(1, MIN_E); }
  public static BigDouble invalid() { return new BigDouble(Double.NaN, 0); }

  public boolean isValid() { return Double.isNaN(M); }
  public boolean isZero() { return E == MIN_E; }

  private double M;
  private int E;

  private BigDouble(double M, int E) { this.M = M; this.E = E; }
  private static BigDouble newStandardizedBigDouble(double M, int E) {
    BigDouble d = new BigDouble(M, E);
    d.standarize();
    return d;
  }

  // Set
  public void setLog(double logM) {
    this.E = (int)logM / LOG_BASE;
    this.M = Math.exp(logM - E*LOG_BASE);
  }
  public void set(double M) {
    this.M = M;
    this.E = 0;
    standarize();
  }
  public void setToVerySmall() {
    this.M = 1;
    this.E = VERY_SMALL_E;
  }
  public void setToVeryBig() {
    this.M = 1;
    this.E = VERY_BIG_E;
  }
  public void set(double M, int E) {
    this.M = M;
    this.E = E;
    standarize();
  }
  public void setToZero() {
    this.M = 0;
    this.E = MIN_E;
  }
  public void setToOne() {
    this.M = 1;
    this.E = 0;
  }

  // Mult, div
  public void mult(double M) {
    this.M *= M;
    standarize();
  }
  public void mult(double M, int E) {
    this.M *= M;
    this.E += E;
    standarize();
  }
  public void mult(BigDouble d) {
    this.M *= d.M;
    this.E += d.E;
    standarize();
  }
  public void mult_mult3(BigDouble d1, BigDouble d2, BigDouble d3) {
    mult(d1.M*d2.M*d3.M, d1.E+d2.E+d3.E);
    standarize();
  }
  public static BigDouble mult2(BigDouble d1, BigDouble d2) {
    return newStandardizedBigDouble(d1.M*d2.M, d1.E+d2.E);
  }
  public static BigDouble mult3(BigDouble d1, BigDouble d2, BigDouble d3) {
    return newStandardizedBigDouble(d1.M*d2.M*d3.M, d1.E+d2.E+d3.E);
  }
  public void div(double M) {
    assert M > 0;
    this.M /= M;
    standarize();
  }
  public void div(BigDouble d) {
    assert !d.isZero();
    this.M /= d.M;
    this.E -= d.E;
    standarize();
  }
  public static BigDouble div(BigDouble d1, BigDouble d2) {
    assert !d2.isZero();
    return newStandardizedBigDouble(d1.M/d2.M, d1.E-d2.E);
  }
  public static BigDouble mult2div1(BigDouble d1, BigDouble d2, BigDouble d3) {
    assert !d3.isZero();
    //dbg(d1.M + " " + d2.M + " " + d3.M + " " + (d1.M*d2.M/d3.M));
    //assert !Double.isNaN(d1.M*d2.M);
    //assert !Double.isNaN(d3.M);
    //assert !Double.isNaN(d1.M*d2.M/d3.M) : d1 + " " + d2 + " " + d3 + " " + (d1.M*d2.M/d3.M);
    return newStandardizedBigDouble(d1.M*d2.M/d3.M, d1.E+d2.E-d3.E);
  }
  public static BigDouble mult4div1(BigDouble d1, BigDouble d2, BigDouble d3, BigDouble d4, BigDouble d5) {
    assert !d5.isZero();
    return newStandardizedBigDouble(d1.M*d2.M*d3.M*d4.M/d5.M, d1.E+d2.E+d3.E+d4.E-d5.E);
  }

  // Incr
  public void incr_mult3(BigDouble d1, BigDouble d2, BigDouble d3) {
    incr(d1.M*d2.M*d3.M, d1.E+d2.E+d3.E);
  }
  public void incr_mult2div1(BigDouble d1, BigDouble d2, BigDouble d3) {
    assert !d3.isZero();
    incr(d1.M*d2.M/d3.M, d1.E+d2.E-d3.E);
  }
  public void incr(double M, int E) {
    if(E < this.E) {
      if(this.E-E < NUM_INV_BASE_POW)
        this.M = this.M + M*INV_BASE_POW[this.E-E];
      // Otherwise, too small to matter
    }
    else if(E > this.E) {
      if(E-this.E < NUM_INV_BASE_POW)
        this.M = this.M*INV_BASE_POW[E-this.E] + M;
      else
        this.M = M;
      this.E = E;
    }
    else
      this.M += M;
    standarize();
  }

  // Update max
  public void updateMax_mult3(BigDouble d1, BigDouble d2, BigDouble d3) {
    updateMax(d1.M*d2.M*d3.M, d1.E+d2.E+d3.E);
  }
  public boolean updateMax(double M, int E) {
    double oldM = this.M;
    double oldE = this.E;
    if(E < this.E) {
      if(this.E-E < NUM_INV_BASE_POW)
        this.M = Math.max(this.M, M*INV_BASE_POW[this.E-E]);
      // Otherwise, too small to matter
    }
    else if(E > this.E) {
      if(E-this.E < NUM_INV_BASE_POW)
        this.M = Math.max(this.M*INV_BASE_POW[E-this.E], M);
      else
        this.M = M;
      this.E = E;
    }
    else
      this.M = Math.max(this.M, M);
    boolean changed = (oldM != this.M || oldE != this.E);
    standarize();
    return changed;
  }
  public boolean updateMax(BigDouble d) { return updateMax(d.M, d.E); }

  // Key function that prevents overflow
  private void standarize() {
    assert M >= 0 : "Mantissa M = " + M + " < 0; log M = " + Math.log(M);
    // Shouldn't have negative numbers but sometimes numerical issues cause things
    // to dip a bit below zero; be forgiving
    /*if(M < 0) {
      error(M + " < 0");
      setToZero();
    }*/
    assert !Double.isInfinite(M);
    /*if(Double.isInfinite(M)) // Sketchy?
      setToVeryBig();
    else*/ if(M == 0)
      setToZero();
    else {
      while(M > BASE) { M *= INV_BASE; E++; }
      while(M < INV_BASE) { M *= BASE; E--; }
    }
  }

  public static BigDouble fromDouble(double M) { return newStandardizedBigDouble(M, 0); }
  public static BigDouble fromLogDouble(double logM) {
    int E = (int)(logM / LOG_BASE);
    double M = Math.exp(logM - E*LOG_BASE);
    return newStandardizedBigDouble(M, E);
  }
  public double toDouble() {
    if(E < 0) {
      if(-E < NUM_INV_BASE_POW)
        return M * INV_BASE_POW[-E];
      else
        return 0; // Too small
    }
    else if(E > 0) {
      if(E < NUM_BASE_POW)
        return M * BASE_POW[E];
      else
        throw Exceptions.bad; // Too big
    }
    else
      return M;
  }
  public double toLogDouble() { return Math.log(M) + E*LOG_BASE; }

  public static int normalizeAndSample(Random random, BigDouble[] weights) {
    int n = weights.length;
    int maxE = MIN_E; // Find maximum exponent
    for(int i = 0; i < n; i++)
      maxE = Math.max(maxE, weights[i].E);
    double[] probs = new double[n];
    for(int i = 0; i < n; i++) {
      if(maxE-weights[i].E < NUM_INV_BASE_POW)
        probs[i] = weights[i].M * INV_BASE_POW[maxE-weights[i].E];
      else
        probs[i] = 0; // Too small to matter
    }
    NumUtils.normalize(probs);
    return SampleUtils.sampleMultinomial(random, probs);
  }

  public static int argmax(BigDouble[] weights) {
    BigDouble max = BigDouble.zero();
    int maxi = -1;
    for(int i = 0; i < weights.length; i++) {
      if(max.updateMax(weights[i]))
        maxi = i;
    }
    return maxi;
  }

  public String toString() { return String.format("%s,%d", Fmt.D(M), E); }
}
