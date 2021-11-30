package fig.basic;

import java.util.*;

public class IntIntIntVec/*TypeVec*/ implements MemUsage.Instrumented, Iterable<IntIntIntVec/*TypeVec*/.Entry> {
  private static final int DEFAULT_CAPACITY = 10;
  
  public interface Entry {
    public int getIndex();
    int/*type1*/ getFirst();
    int/*type2*/ getSecond();
    int/*type3*/ getThird();
    void setFirst(int/*type1*/ value);
    void setSecond(int/*type2*/ value);
    void setThird(int/*type3*/ value);
  }

  public IntIntIntVec/*TypeVec*/() {
    this(DEFAULT_CAPACITY);
  }
  public IntIntIntVec/*TypeVec*/(int cap) {
    this.data1 = new int/*type1*/[cap];
    this.data2 = new int/*type2*/[cap];
    this.data3 = new int/*type3*/[cap];
    this.n = 0;
  }

  public int/*type1*/ getFirst(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data1[i];
  }
  public int/*type2*/ getSecond(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data2[i];
  }
  public int/*type3*/ getThird(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data3[i];
  }
  public void set(int i, int/*type1*/ x, int/*type2*/ y, int/*type3*/ z) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data1[i] = x;
    data2[i] = y;
    data3[i] = z;
  }
  // Set, but grow the array if necessary
  public void setGrow(int i, int/*type1*/ x, int/*type2*/ y, int/*type3*/ z) {
    if(i >= n) {
      if(i >= data1.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data1[i] = x;
    data2[i] = y;
    data3[i] = z;
  }
  // Append an element
  public void add(int/*type1*/ x, int/*type2*/ y, int/*type3*/ z) { setGrow(n, x, y, z); }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    int/*type1*/[] newData1 = new int/*type1*/[cap];
    int/*type2*/[] newData2 = new int/*type2*/[cap];
    int/*type3*/[] newData3 = new int/*type3*/[cap];
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
      h = h*29 + (Integer/*Type1*/.valueOf(data1[i]).hashCode());
      h = h*29 + (Integer/*Type2*/.valueOf(data2[i]).hashCode());
      h = h*29 + (Integer/*Type3*/.valueOf(data3[i]).hashCode());
    }
    return h;
  }
  public boolean equals(Object o) {
    IntIntIntVec/*TypeVec*/ v = (IntIntIntVec/*TypeVec*/)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++) {
      if (data1[i] != v.data1[i]) return false;
      if (data2[i] != v.data2[i]) return false;
      if (data3[i] != v.data3[i]) return false;
    }
    return true;
  }

  public int/*type1*/[] getFirstData() { return data1; }
  public int/*type2*/[] getSecondData() { return data2; }
  public int/*type3*/[] getThirdData() { return data3; }

  private int/*type1*/[] data1;
  private int/*type2*/[] data2;
  private int/*type3*/[] data3;
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
    @Override public int/*type1*/ getFirst() { return data1[index]; }
    @Override public int/*type2*/ getSecond() { return data2[index]; }
    @Override public int/*type3*/ getThird() { return data3[index]; }
    @Override public void setFirst(int/*type1*/ value) { data1[index] = value; }
    @Override public void setSecond(int/*type2*/ value) { data2[index] = value; }
    @Override public void setThird(int/*type3*/ value) { data3[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
