package fig.prob;

import fig.basic.*;
import java.util.*;
import java.io.*;

/**
 * A product distribution.
 */
public class MargProductDistrib implements MargDistrib<ProductDistrib> {
  public MargDistrib[] distribs;
  public MargProductDistrib(MargDistrib[] distribs) {
    this.distribs = distribs;
  }
  public double margLogLikelihood(SuffStats _stats)
  {
    ProductSuffStats stats = (ProductSuffStats) _stats;
    double logLikelihood = 0.0;
    for (int i = 0; i < dim(); i++)
    {
      MargDistrib currentMarg = distribs[i];
      SuffStats currentStats = stats.getComponent(i);
      logLikelihood = logLikelihood + currentMarg.margLogLikelihood(currentStats);
    }
    return logLikelihood;
  }

  public double predLogLikelihood(SuffStats _condStats, SuffStats _predStats)
  {
    ProductSuffStats condStats = (ProductSuffStats) _condStats;
    ProductSuffStats predStats = (ProductSuffStats) _predStats;
    double logLikelihood = 0.0;
    for (int i = 0; i < dim(); i++)
    {
      MargDistrib currentMarg = distribs[i];
      logLikelihood = logLikelihood 
        + currentMarg.predLogLikelihood(condStats.getComponent(i), predStats.getComponent(i));
    }
    return logLikelihood;
  }

  public double logProb(SuffStats stats) {
    throw Exceptions.unimplemented;
  }
  public double logProbObject(ProductDistrib pd) {
    throw Exceptions.unimplemented;
  }
  public double crossEntropy(Distrib<ProductDistrib> _that) {
    throw Exceptions.unimplemented;
  }
  public double expectedLogLikelihood(SuffStats stats) {
    throw Exceptions.unimplemented;
  }

  public ProductDistrib sampleObject(Random random) {
    Distrib[] distribs = new Distrib[dim()];
    for(int i = 0; i < dim(); i++)
      distribs[i] = (Distrib)distribs[i].sampleObject(random);
    return new ProductDistrib(distribs);
  }

  public MargProductDistrib getPosterior(SuffStats stats) {
    MargDistrib[] postDistribs = new MargDistrib[dim()];
    for(int i = 0; i < dim(); i++)
      postDistribs[i] = distribs[i].getPosterior(stats);
    return new MargProductDistrib(postDistribs);
  }

  public int dim() { return distribs.length; }

  public String toString() { return StrUtils.join(distribs, " x "); }
}
