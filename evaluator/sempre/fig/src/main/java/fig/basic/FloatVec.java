package fig.basic;

import java.util.*;

/**
Primitive array that automatically grows.
*/
public class FloatVec implements MemUsage.Instrumented, Iterable<FloatVec.Entry> {
  public interface Entry {
    int getIndex();
    float getValue();
    void setValue(float value);
  }

  public FloatVec() {
    this.data = new float[0];
    this.n = 0;
  }
  public FloatVec(int cap) {
    this.data = new float[cap];
    this.n = 0;
  }
  public FloatVec(float[] data, int start, int end) {
    this.n = end-start;
    this.data = new float[n];
    for(int i = 0; i < n; i++)
      this.data[i] = data[start+i];
  }

  public FloatVec(float[] data) {
    this.data = data.clone();
    this.n = data.length;
  }

  public float get(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data[i];
  }
  public float get(int i, float defaultValue) {
    if(i >= n) return defaultValue;
    return data[i];
  }
  public float set(int i, float x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] = x;
    return x;
  }
  public float increment(int i, float x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] += x;
    return data[i];
  }
  // Set, but grow the array if necessary
  public float setGrow(int i, float x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] = x;
    return x;
  }
  public float incrementGrow(int i, float x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] += x;
    return data[i];
  }
  // Append an element
  public void add(float x) { setGrow(n, x); }

  public void multAll(float d) {
    for(int i = 0; i < n; i++)
      data[i] *= d;
  }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    float[] newData = new float[cap];
    System.arraycopy(data, 0, newData, 0, n);
    data = newData;
  }
  public void trimToSize() { setCapacity(n); }
  public int size() { return n; }

  public int hashCode() {
    int h = n; 
    for(int i = 0; i < n; i++)
      h = h*29 + (Float.valueOf(data[i]).hashCode());
    return h;
  }
  public boolean equals(Object o) {
    FloatVec v = (FloatVec)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++)
      if(data[i] != v.data[i]) return false;
    return true;
  }

  public float[] getData() { return data; }  // Dangerous

  private float[] data;
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
    public float getValue() { return data[index]; }
    public void setValue(float value) { data[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
