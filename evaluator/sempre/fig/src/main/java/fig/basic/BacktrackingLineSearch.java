package fig.basic;

import java.io.*;
import java.util.*;
import fig.basic.Option;
import fig.basic.ListUtils;
import fig.basic.NumUtils;
import fig.basic.LogInfo;
import fig.basic.Fmt;

/**
 * Used by various Maximizers to search along a particular direction for a good
 * step size that will increase the function value sufficiently.
 */
public class BacktrackingLineSearch {
  public static class Options {
    @Option public double stepSizeDecrFactor = 0.9;
    @Option public double stepSizeIncrFactor = 1.3;
    @Option(gloss="Try to reduce the step size for at most this many times while the objective is not improving") public int maxTries = 100;
    @Option(gloss="Stop optimizing when the L2 norm of gradient drops below this") public double tolerance = 1e-5;
    @Option public double initStepSize = 1;
    @Option public int verbose = 0;

    // For decreasing step-size
    @Option public double stepSizeReductionPower = 0.5;
    @Option(gloss="Just take one step") public boolean simple = false;
  }

  // Current step size: note this is state that's maintained across
  // iterations.
  double stepSize;
  int numSteps;  // For decreasing step size
  Options opts;

  public BacktrackingLineSearch(Options opts) {
    this.opts = opts;
    this.stepSize = opts.initStepSize;
  }

  private String formatDoubleArray(double[] x) {
    return Fmt.D(ListUtils.subArray(x, 0, Math.min(100, x.length)));
  }

  // Very crude search: decrease step size until get improvement
  // Return true if can't reduce and should stop.
  public boolean maximize(Maximizer.FunctionState func, double[] dx) {
    if (!NumUtils.isFinite(dx)) {
      LogInfo.errors("Bad direction");
      return true;
    }
    if (opts.verbose >= 1) LogInfo.begin_track("BacktrackingLineSearch.maximize");

    double[] gradient = func.gradient();
    double l2Norm = NumUtils.l2Norm(gradient);

    if (opts.verbose >= 2) {
      LogInfo.logs("x: %s", formatDoubleArray(func.point()));
      LogInfo.logs("dx: %s", formatDoubleArray(dx));
      LogInfo.logs("gradient: %s", formatDoubleArray(gradient));
      LogInfo.logs("value: %s", Fmt.D(func.value()));
      LogInfo.logs("stepSize: %s", Fmt.D(stepSize));
      LogInfo.logs("gradientNorm: %s", Fmt.D(l2Norm));
    }
    if (l2Norm <= opts.tolerance) {
      if (opts.verbose >= 1) LogInfo.logs("Converged");
      if (opts.verbose >= 1) LogInfo.end_track();
      return true;
    }

    double[] x = func.point();
    double y0 = func.value();
    NumUtils.assertIsFinite(y0);

    // Just simple decreasing step size - just take one step
    if (opts.simple) {
      numSteps++;
      stepSize = opts.initStepSize / Math.pow(numSteps, opts.stepSizeReductionPower);
      ListUtils.incr(x, stepSize, dx);
      func.invalidate();
      if (opts.verbose >= 1) LogInfo.end_track();
      return false;
    }

    double oldStepSize = 0;
    double lasty = Double.NEGATIVE_INFINITY;

    int t;
    for(t = 0; ; t++) {
      // Keep on decreasing the step size while things are getting better
      ListUtils.incr(x, stepSize-oldStepSize, dx);
      if (opts.verbose >= 3) LogInfo.logs("x = %s", formatDoubleArray(x));
      func.invalidate();
      double y = func.value();
      if (opts.verbose >= 3) LogInfo.logs("value = %s (stepSize = %s)", y, stepSize);
      //if (opts.verbose >= 3) LogInfo.logs("y - lasty = %s - %s = %s", y, lasty, y - lasty);

      if (y > lasty && t+1 < opts.maxTries) { // Things are getting better still...
        // Cut the stepSize
        oldStepSize = stepSize;
        stepSize *= opts.stepSizeDecrFactor;
        lasty = y;
        continue;
      }

      // Things are not getting better...
      if (lasty > y0) {  // Last point was good, go there
        ListUtils.incr(x, oldStepSize-stepSize, dx);
        func.invalidate();
        stepSize = oldStepSize * opts.stepSizeIncrFactor; // Increase step size for next time
        if (opts.verbose >= 2) LogInfo.logs("Improvement of %s on reduction %d", Fmt.D(lasty-y0), t);
        if (opts.verbose >= 1) LogInfo.end_track();
        return false;
      }

      // Unable to decrease: give up
      if (opts.verbose >= 1) LogInfo.logs("No improvement after %d reductions, giving up", t+1);
      if (opts.verbose >= 1) LogInfo.end_track();
      return true;
    }
  }
}
