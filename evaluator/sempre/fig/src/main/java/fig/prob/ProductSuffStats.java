package fig.prob;

import java.util.*;
import java.io.*;

public class ProductSuffStats implements SuffStats
{
  private SuffStats[] myStats;
  
  public SuffStats getComponent(int index)
  {
    return myStats[index];
  }
  
  public int size()
  {
    return myStats.length;
  }
  
  public ProductSuffStats(SuffStats[] _suffStats)
  {
    this.myStats = _suffStats;
  }
  
  public void add(SuffStats _suffStats)
  {
    ProductSuffStats prodSuffStats = (ProductSuffStats) _suffStats;
    for (int i = 0; i < myStats.length; i++)
    {
      myStats[i].add(prodSuffStats.myStats[i]);
    }
  }

  public void sub(SuffStats _suffStats)
  {
    ProductSuffStats prodSuffStats = (ProductSuffStats) _suffStats;
    for (int i = 0; i < myStats.length; i++)
    {
      myStats[i].sub(prodSuffStats.myStats[i]);
    }
  }

  public SuffStats reweight(double scale) {
    SuffStats[] stats = new SuffStats[size()];
    for(int i = 0; i < size(); i++)
      stats[i] = myStats[i].reweight(scale);
    return new ProductSuffStats(stats);
  }
}
