package fig.prob;

import java.util.*;
import fig.basic.*;

/**
 * See SparseDirichlet and DegenerateSparseDirichlet.
 */
public interface SparseDirichletInterface extends Distrib<TDoubleMap> {
  public int dim();
  public double getConcentration(Object key);
  public double totalCount();
  public double getMean(Object key);
  public double getMode(Object key);
  public double expectedLog(Object key);
  public SparseDirichletInterface modeSpike();
}
