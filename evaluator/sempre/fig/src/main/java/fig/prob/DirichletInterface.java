package fig.prob;

/**
 * See Dirichlet and DegenerateDirichlet for implementations.
 */
public interface DirichletInterface extends Distrib<double[]> {
  public int dim();
  public double[] getMean();
  public double[] getMode();
  public double[] expectedLog();
  public double expectedLog(int i);
  public double getAlpha(int i);
  public double totalCount();
  public DirichletInterface modeSpike();
}
