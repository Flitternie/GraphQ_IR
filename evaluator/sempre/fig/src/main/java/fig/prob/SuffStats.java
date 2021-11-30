package fig.prob;

/**
 * Represents all the information about a set of data points that the
 * likelihood model needs in order to evaluate the likelihood of the data.
 */
public interface SuffStats {
  public void add(SuffStats suffStats);
  public void sub(SuffStats suffStats);
  public SuffStats reweight(double scale);
}
