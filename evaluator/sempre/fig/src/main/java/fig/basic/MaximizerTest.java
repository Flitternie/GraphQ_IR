package fig.basic;

import java.io.*;
import java.util.*;
import fig.basic.LogInfo;
import fig.basic.Fmt;
import fig.exec.Execution;

/**
 * Optimizes a simple function to demonstrate how to use the Maximizer
 * interface.
 */
public class MaximizerTest {
  public static void main(String[] args) {
    BacktrackingLineSearch.Options btopts = new BacktrackingLineSearch.Options();
    LBFGSMaximizer.Options lopts = new LBFGSMaximizer.Options();
    Execution.init(args, "lsearch", btopts, "lbfgs", lopts);

    //Maximizer maximizer = new GradientMaximizer(btopts);
    Maximizer maximizer = new LBFGSMaximizer(btopts, lopts);

    // For this function, 
    // Function: quadratic funtion with non-isotropic Hessian.
    //   f(x) = -0.5 * sum_i scale_i * (truePoint_i - point_i)^2
    Maximizer.FunctionState state = new Maximizer.FunctionState() {
      // Specifies the function
      final int D = 5; // Dimensionality of the problem
      private double truePoint(int i) { return i+3; }
      private double scale(int i) { return (i+1)*5; }

      // Current point, value, gradient
      private double[] point = new double[D];
      private double value;
      private double[] gradient = new double[D];
      boolean valueValid = false;
      boolean gradientValid = false;

      public double[] point() { return point; }

      public double[] gradient() {
        if (!gradientValid) {
          for(int i = 0; i < D; i++)
            gradient[i] = -scale(i) * (point[i] - truePoint(i));
          gradientValid = true;
        }
        return gradient;
      }

      public double value() {
        if (!valueValid) {
          value = 0;
          for(int i = 0; i < D; i++)
            value -= 0.5 * scale(i) * (point[i] - truePoint(i)) * (point[i] - truePoint(i));
        }
        return value;
      }

      public void invalidate() { valueValid = gradientValid = false; }
    };

    // Optimize!
    for(int iter = 0; ; iter++) {
      LogInfo.logs("iter %d: point = %s, value = %s, gradient = %s", iter,
        Fmt.D(state.point()),
        Fmt.D(state.value()),
        Fmt.D(state.gradient()));
      if(maximizer.takeStep(state)) break;
    }

    Execution.finish();
  }
}
