package fig.basic;

import java.util.*;

/**
 * Allows measuring precision and recall.
 */
public class EvalResult {
  // True, pred: p = positive, n = negative
  private double pp, pn, np, nn;
  private double count;

  public EvalResult() { }

  public EvalResult(double numTrueAndPred, double numTrue, double numPred) {
    pp = numTrueAndPred;
    pn = numTrue - numTrueAndPred;
    np = numPred - numTrueAndPred;
    nn = 0;
    count = numTrue + numPred - numTrueAndPred;
  }

  // Probability of being positive
  public void add(double trueProb, double predProb) {
    pp += trueProb * predProb;
    pn += trueProb * (1-predProb);
    np += (1-trueProb) * predProb;
    nn += (1-trueProb) * (1-predProb);
    count++;
  }
  public void add(boolean trueVal, boolean predVal) {
    add(trueVal ? 1 : 0, predVal ? 1 : 0);
  }
  public void add(EvalResult r) {
    pp += r.pp;
    pn += r.pn;
    np += r.np;
    nn += r.nn;
    count += r.count;
  }

  public <T> void add(HashSet<T> trueSet, HashSet<T> predSet) {
    for(T x : trueSet)
      add(true, predSet.contains(x));
    for(T x : predSet)
      if(!trueSet.contains(x))
        add(false, true);
  }

  public double precision() { return pp / (pp + np); }
  public double recall() { return pp / (pp + pn); }
  public double falsePos() { return np / (pp + np); }
  public double trueNeg() { return pn / (pp + pn); }
  public double count() { return count; }
  public double numTrue() { return pp+pn; }
  public double numPred() { return pp+np; }

  public double f1() {
    double p = precision(), r = recall();
    return 2 * p * r / (p + r);
  }

  public String toString() {
    return String.format("Precision = %s, recall = %s, F1 = %s (%s)",
        Fmt.D(precision()), Fmt.D(recall()), Fmt.D(f1()), Fmt.D(count()));
  }
}
