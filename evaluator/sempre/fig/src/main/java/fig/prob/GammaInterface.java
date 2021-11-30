package fig.prob;

public interface GammaInterface extends Distrib<Double> {
  public double getShape();
  public double getRate();
  public double getMean();
  public double getMode();
  public double expectedLog();
  public GammaInterface modeSpike();
}
