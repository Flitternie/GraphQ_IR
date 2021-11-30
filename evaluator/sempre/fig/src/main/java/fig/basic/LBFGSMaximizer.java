package fig.basic;

import java.io.*;
import java.util.*;
import fig.basic.Option;
import fig.basic.ListUtils;
import fig.basic.NumUtils;
import fig.basic.LogInfo;
import fig.basic.Fmt;

/**
 * Implementation of L-BFGS with backtracking line search.
 * Added robustness for non-convex functions: if the Hessian is non-PSD, then
 * we reset the history.
 */
public class LBFGSMaximizer extends GradientMaximizer {
  public static class Options {
    @Option(gloss="Number of past gradients to keep as an estimate of the Hessian") public int historySize = 5;
  }

  Options opts;
  BacktrackingLineSearch lineSearch;

  // Implicitly store the approximation of the inverse Hessian
  LinkedList<double[]> sHistory; // History of point differences
  LinkedList<double[]> yHistory; // History of gradient differences
  double[] lastx;
  double[] lastg;

  public LBFGSMaximizer(BacktrackingLineSearch.Options btopts, Options opts) {
    super(btopts);
    this.opts = opts;
    this.sHistory = new LinkedList();
    this.yHistory = new LinkedList();
  }

  // Add src1-src2 to history (kick out oldest if necessary to maintain history size)
  public void store(LinkedList<double[]> history, double[] src1, double[] src2) {
    if (opts.historySize == 0) return;
    double[] dest;
    if(history.size() < opts.historySize)
      dest = new double[src1.length];
    else
      dest = history.removeFirst(); // Reuse old vectors
    for(int i = 0; i < dest.length; i++)
      dest[i] = src1[i] - src2[i];
    history.addLast(dest);
  }

  public double[] precondition(double[] g) {
    double[] p = new double[g.length];
    ListUtils.incr(p, -1, g);

    int n = yHistory.size(); // Doesn't include last point
    double[] sy = new double[n]; // s^T y
    double[] alpha = new double[n];

    // Backward pass
    for(int k = n-1; k >= 0; k--) {
      sy[k] = ListUtils.dot(sHistory.get(k), yHistory.get(k));
      if (sy[k] <= 0) {
        //LogInfo.errors("sy[k] = %s > 0 failed, resetting history", sy[k]);
        sHistory.clear();
        yHistory.clear();
        lastx = null;
        lastg = null;
        ListUtils.set(p, 0);
        ListUtils.incr(p, -1, g);
        return p;
      }
      alpha[k] = ListUtils.dot(sHistory.get(k), p) / sy[k];
      //NumUtils.assertIsFinite(alpha[k]);
      ListUtils.incr(p, -alpha[k], yHistory.get(k));
    }
    if(n > 0) {
      ListUtils.multMut(p,
          sy[n-1] / ListUtils.dot(yHistory.get(n-1), yHistory.get(n-1)));
    }

    // Forward pass
    for(int k = 0; k < n; k++) {
      double beta = ListUtils.dot(yHistory.get(k), p) / sy[k];
      ListUtils.incr(p, (alpha[k] - beta), sHistory.get(k));
    }

    //LogInfo.dbgs("g: %s", Fmt.D(g));
    //LogInfo.dbgs("p: %s", Fmt.D(p));
    return p;
  }

  public double[] getDirection(FunctionState func) {
    double[] x = func.point();
    double[] g = func.gradient();
    ListUtils.multMut(g, -1); // Pretend we're minimizing the function
    double[] p = precondition(g); // Use current approximation of inverse Hessian
    if(lastx == null) {
      // First point - just store, inverse Hessian approximation is identity
      lastx = new double[x.length];
      lastg = new double[g.length];
    }
    else {
      store(sHistory, x, lastx); // s_k = x_{k+1} - x_k
      store(yHistory, g, lastg); // y_k = g_{k+1} - g_k
    }
    ListUtils.set(lastx, x);
    ListUtils.set(lastg, g);
    return p;
  }
}
