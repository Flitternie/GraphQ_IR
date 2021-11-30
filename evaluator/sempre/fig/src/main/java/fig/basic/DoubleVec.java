package fig.basic;

import java.util.*;

/**
Primitive array that automatically grows.
*/
public class DoubleVec implements MemUsage.Instrumented, Iterable<DoubleVec.Entry> {
  public interface Entry {
    int getIndex();
    double getValue();
    void setValue(double value);
  }

  public DoubleVec() {
    this.data = new double[0];
    this.n = 0;
  }
  public DoubleVec(int cap) {
    this.data = new double[cap];
    this.n = 0;
  }
  public DoubleVec(double[] data, int start, int end) {
    this.n = end-start;
    this.data = new double[n];
    for(int i = 0; i < n; i++)
      this.data[i] = data[start+i];
  }

  public DoubleVec(double[] data) {
    this.data = data.clone();
    this.n = data.length;
  }

  public double get(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data[i];
  }
  public double get(int i, double defaultValue) {
    if(i >= n) return defaultValue;
    return data[i];
  }
  public double set(int i, double x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] = x;
    return x;
  }
  public double increment(int i, double x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] += x;
    return data[i];
  }
  // Set, but grow the array if necessary
  public double setGrow(int i, double x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] = x;
    return x;
  }
  public double incrementGrow(int i, double x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] += x;
    return data[i];
  }
  // Append an element
  public void add(double x) { setGrow(n, x); }

  public void multAll(double d) {
    for(int i = 0; i < n; i++)
      data[i] *= d;
  }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    double[] newData = new double[cap];
    System.arraycopy(data, 0, newData, 0, n);
    data = newData;
  }
  public void trimToSize() { setCapacity(n); }
  public int size() { return n; }

  public int hashCode() {
    int h = n; 
    for(int i = 0; i < n; i++)
      h = h*29 + (Double.valueOf(data[i]).hashCode());
    return h;
  }
  public boolean equals(Object o) {
    DoubleVec v = (DoubleVec)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++)
      if(data[i] != v.data[i]) return false;
    return true;
  }

  public double[] getData() { return data; }  // Dangerous

  private double[] data;
  private int n;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize + MemUsage.intSize) +
           MemUsage.getBytes(data) +
           MemUsage.getBytes(n);
  }

  private class EntryIterator implements Iterator<Entry>, Entry {
    int index = -1;
    @Override public boolean hasNext() { return index < n - 1; }
    @Override public Entry next() { index++; return this; }
    @Override public void remove() { throw new RuntimeException("Not supported"); }
    public int getIndex() { return index; }
    public double getValue() { return data[index]; }
    public void setValue(double value) { data[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
