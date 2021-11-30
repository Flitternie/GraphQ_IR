package fig.basic;

import java.util.*;

/*
Like ArrayList.SubList, but is immutable and takes up much less space.
*/
public class SubList<T> implements MemUsage.Instrumented {
  public final List<T> list;
  public final int start;
  public final int end;

  public SubList(List<T> list, int start, int end) {
    this.list = list;
    this.start = start;
    this.end = end;
  }

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize + MemUsage.intSize * 2);
  }

  public int size() { return end - start; }
  public T get(int i) { return list.get(start + i); }

  // Performs range check to ensure that we don't go outside sublist
  public T getSafe(int i) {
    if (i < 0 || i >= size())
      throw new IndexOutOfBoundsException("Index: " + i + ", Size: " + size());
    return list.get(start + i);
  }

  public SubList<T> subList(int i, int j) {
    return new SubList(list, start + i, start + j);
  }

  public boolean contains(Object o) {
    int n = end - start;
    for (int i = 0; i < n; i++)
      if (list.get(start + i).equals(o))
        return true;
    return false;
  }

  @Override public boolean equals(Object _that) {
    if (!(_that instanceof SubList)) return false;
    SubList that = (SubList)_that;
    int n = end - start;
    if (n != that.size()) return false;
    for (int i = 0; i < n; i++)
      if (!list.get(start + i).equals(that.get(i)))
        return false;
    return true;
  }

  @Override public int hashCode() {
    // Note: not guaranteed to match List.hashCode.
    int hashCode = 1;
    for (int i = start; i < end; i++)
      hashCode = 31 * hashCode + list.get(i).hashCode();
    return hashCode;
  }

  @Override public String toString() {
    return list.subList(start, end).toString();
  }
}
