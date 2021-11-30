package fig.basic;

import java.util.*;

public class StringIntVec implements MemUsage.Instrumented, Iterable<StringIntVec.Entry> {
  private static final int DEFAULT_CAPACITY = 10;
  
  public interface Entry {
    public int getIndex();
    String getFirst();
    int getSecond();
    void setFirst(String value);
    void setSecond(int value);
  }

  public StringIntVec() {
    this(DEFAULT_CAPACITY);
  }
  public StringIntVec(int cap) {
    this.data1 = new String[cap];
    this.data2 = new int[cap];
    this.n = 0;
  }

  public String getFirst(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data1[i];
  }
  public int getSecond(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data2[i];
  }
  public void set(int i, String x, int y) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data1[i] = x;
    data2[i] = y;
  }
  // Set, but grow the array if necessary
  public void setGrow(int i, String x, int y) {
    if(i >= n) {
      if(i >= data1.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data1[i] = x;
    data2[i] = y;
  }
  // Append an element
  public void add(String x, int y) { setGrow(n, x, y); }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    String[] newData1 = new String[cap];
    int[] newData2 = new int[cap];
    System.arraycopy(data1, 0, newData1, 0, n);
    System.arraycopy(data2, 0, newData2, 0, n);
    data1 = newData1;
    data2 = newData2;
  }
  public void trimToSize() { setCapacity(n); }
  public int size() { return n; }

  public int hashCode() {
    int h = n; 
    for(int i = 0; i < n; i++) {
      h = h*29 + (String.valueOf(data1[i]).hashCode());
      h = h*29 + (Integer.valueOf(data2[i]).hashCode());
    }
    return h;
  }
  public boolean equals(Object o) {
    StringIntVec v = (StringIntVec)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++) {
      if (data1[i] != v.data1[i]) return false;
      if (data2[i] != v.data2[i]) return false;
    }
    return true;
  }

  public String[] getFirstData() { return data1; }
  public int[] getSecondData() { return data2; }

  private String[] data1;
  private int[] data2;
  private int n;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize + MemUsage.intSize) +
           MemUsage.getBytes(data1) +
           MemUsage.getBytes(data2) +
           MemUsage.getBytes(n);
  }

  private class EntryIterator implements Iterator<Entry>, Entry {
    int index = -1;
    @Override public boolean hasNext() { return index < n - 1; }
    @Override public Entry next() { index++; return this; }
    @Override public void remove() { throw new RuntimeException("Not supported"); }
    @Override public int getIndex() { return index; }
    @Override public String getFirst() { return data1[index]; }
    @Override public int getSecond() { return data2[index]; }
    @Override public void setFirst(String value) { data1[index] = value; }
    @Override public void setSecond(int value) { data2[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
