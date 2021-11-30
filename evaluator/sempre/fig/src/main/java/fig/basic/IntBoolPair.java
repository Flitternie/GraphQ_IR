package fig.basic;

import java.io.Serializable;

// Stores (int, bool); mutable.
public class IntBoolPair implements Serializable, MemUsage.Instrumented {
  private static final long serialVersionUID = 42;

  public IntBoolPair() { }
  public IntBoolPair(int first, boolean second) {
    this.first = first;
    this.second = second;
  }

  public String toString() {
    return first + "," + second;
  }

	public int hashCode() { return 29*first + (second ? 1 : 0); }
  public boolean equals(Object o) {
    IntBoolPair p = (IntBoolPair)o;
    return first == p.first && second == p.second;
  }

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.intSize + MemUsage.booleanSize) + 8;
  }

  public int first;
  public boolean second;
}
