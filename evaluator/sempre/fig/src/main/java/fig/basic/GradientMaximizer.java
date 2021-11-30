package fig.basic;

/**
 * Simple gradient ascent algorithm with backtracking line search.
 */
public class GradientMaximizer extends Maximizer {
  private BacktrackingLineSearch lineSearch;

  public GradientMaximizer(BacktrackingLineSearch.Options btopts) {
    this.lineSearch = new BacktrackingLineSearch(btopts);
  }

  public boolean takeStep(FunctionState func) {
    double[] dx = getDirection(func);
    return lineSearch.maximize(func, dx);
  }

  // Can override if we want to precondition
  protected double[] getDirection(FunctionState func) {
    return func.gradient();
  }
}
