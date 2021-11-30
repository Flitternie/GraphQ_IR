package fig.basic;

import java.io.Serializable;

// (Object, double); this is mutable
public class ObjectDoublePair<T> implements Serializable, MemUsage.Instrumented {
  private static final long serialVersionUID = 42;

  public ObjectDoublePair() { }
  public ObjectDoublePair(T first, double second) {
    this.first = first;
    this.second = second;
  }

  public String toString() {
    return first + "," + second;
  }

  public T first;
  public double second;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize + MemUsage.doubleSize) +
           MemUsage.getBytes(first);
  }
}
