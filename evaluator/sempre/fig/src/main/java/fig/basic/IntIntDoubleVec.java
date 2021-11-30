package fig.basic;

import java.util.*;

public class IntIntDoubleVec implements MemUsage.Instrumented, Iterable<IntIntDoubleVec.Entry> {
  private static final int DEFAULT_CAPACITY = 10;
  
  public interface Entry {
    public int getIndex();
    int getFirst();
    int getSecond();
    double getThird();
    void setFirst(int value);
    void setSecond(int value);
    void setThird(double value);
  }

  public IntIntDoubleVec() {
    this(DEFAULT_CAPACITY);
  }
  public IntIntDoubleVec(int cap) {
    this.data1 = new int[cap];
    this.data2 = new int[cap];
    this.data3 = new double[cap];
    this.n = 0;
  }

  public int getFirst(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data1[i];
  }
  public int getSecond(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data2[i];
  }
  public double getThird(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data3[i];
  }
  public void set(int i, int x, int y, double z) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data1[i] = x;
    data2[i] = y;
    data3[i] = z;
  }
  // Set, but grow the array if necessary
  public void setGrow(int i, int x, int y, double z) {
    if(i >= n) {
      if(i >= data1.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data1[i] = x;
    data2[i] = y;
    data3[i] = z;
  }
  // Append an element
  public void add(int x, int y, double z) { setGrow(n, x, y, z); }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    int[] newData1 = new int[cap];
    int[] newData2 = new int[cap];
    double[] newData3 = new double[cap];
    System.arraycopy(data1, 0, newData1, 0, n);
    System.arraycopy(data2, 0, newData2, 0, n);
    System.arraycopy(data3, 0, newData3, 0, n);
    data1 = newData1;
    data2 = newData2;
    data3 = newData3;
  }
  public void trimToSize() { setCapacity(n); }
  public int size() { return n; }

  public int hashCode() {
    int h = n; 
    for(int i = 0; i < n; i++) {
      h = h*29 + (Integer.valueOf(data1[i]).hashCode());
      h = h*29 + (Integer.valueOf(data2[i]).hashCode());
      h = h*29 + (Double.valueOf(data3[i]).hashCode());
    }
    return h;
  }
  public boolean equals(Object o) {
    IntIntDoubleVec v = (IntIntDoubleVec)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++) {
      if (data1[i] != v.data1[i]) return false;
      if (data2[i] != v.data2[i]) return false;
      if (data3[i] != v.data3[i]) return false;
    }
    return true;
  }

  public int[] getFirstData() { return data1; }
  public int[] getSecondData() { return data2; }
  public double[] getThirdData() { return data3; }

  private int[] data1;
  private int[] data2;
  private double[] data3;
  private int n;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize + MemUsage.intSize) +
           MemUsage.getBytes(data1) +
           MemUsage.getBytes(data2) +
           MemUsage.getBytes(data3) +
           MemUsage.getBytes(n);
  }

  private class EntryIterator implements Iterator<Entry>, Entry {
    int index = -1;
    @Override public boolean hasNext() { return index < n - 1; }
    @Override public Entry next() { index++; return this; }
    @Override public void remove() { throw new RuntimeException("Not supported"); }
    @Override public int getIndex() { return index; }
    @Override public int getFirst() { return data1[index]; }
    @Override public int getSecond() { return data2[index]; }
    @Override public double getThird() { return data3[index]; }
    @Override public void setFirst(int value) { data1[index] = value; }
    @Override public void setSecond(int value) { data2[index] = value; }
    @Override public void setThird(double value) { data3[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
