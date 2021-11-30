package fig.prob;

/**
 * See Beta and DegenerateBeta for implementations.
 */
public interface BetaInterface extends Distrib<Double> {
  public double expectedLog(boolean b);
  public double getAlpha();
  public double getBeta();
  public double getMean();
  public double getMode();
  public double totalCount();
  public BetaInterface modeSpike();
}
