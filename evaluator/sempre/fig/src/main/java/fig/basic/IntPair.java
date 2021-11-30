package fig.basic;

import java.io.Serializable;

// (int, int) this is mutable
public class IntPair implements Serializable, MemUsage.Instrumented {
  private static final long serialVersionUID = 42;

  public IntPair() { }
  public IntPair(int first, int second) {
    this.first = first;
    this.second = second;
  }

  public String toString() {
    return first + "," + second;
  }

	public int hashCode() { return 29*first + second; }
  public boolean equals(Object o) {
    IntPair p = (IntPair)o;
    return first == p.first && second == p.second;
  }

  public int first;
  public int second;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.intSize * 2) +
           8; // Unexplained
  }
}
