package fig.basic;

/**
 * A |Maximizer| is a class that performs iterative gradient-based optimization
 * on a function.
 *
 * Note that this library exposes more of the internals of the optmization
 * procedure compared to other optimizers, which gives the user a bit more
 * control.
 *
 * The |Maximizer| works by iteratively mutating a |FunctionState|, which encapsulates
 *  - domain-specific information about how to compute function values and gradients at various points
 *  - the actual current point, function value at that point, and gradient at that point
 *    (this is slightly unusual, but allows the user to control the memory allocation).
 *
 * To optimize a function, you should implement the FunctionState interface.
 * A typical implementation:
 *  - Store the |point|, |value|, |gradient|, and a |valid| flag denoting whether the
 *    |value| and |gradient| are consistent with |point|.
 *  - invalidate() sets the |valid| to false.
 *  - value(), gradient() should return the |value| and |gradient|, recomputing
 *    them if |valid| is false.
 *
 * The reason that |value| and |gradient| computation is decoupled is that in
 * line search, we need many calls to value() only, so there's no need to
 * compute the gradient in those cases.
 *
 * See MaximizerTest.java for an example of usage.
 */
public abstract class Maximizer {
  public interface FunctionState {
    // The current point (owned by FunctionState but is modified by the optimizer).
    // Contract: the optimizer will mutate the array returned by point().
    public double[] point();

    // Return the function value at the current point, computing it if necessary.
    public double value();

    // Return gradient at the current point, computing it if necessary.
    // Contract: the optimizer will not modify the returned array, and the
    // FunctionState can reuse the same one.
    public double[] gradient();

    // Called after optimizer mutates the current point.
    // When this function is called, make a note to recompute the value and
    // gradient.
    public void invalidate();
  }

  // Input: a FunctionState.
  // Modifies the FunctionState by taking one step.
  // Return whether we've already reached the maximum (up to some tolerance) and should stop.
  public abstract boolean takeStep(FunctionState func);
}
