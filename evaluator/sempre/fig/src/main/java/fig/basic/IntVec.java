package fig.basic;

import java.util.*;

/**
Primitive array that automatically grows.
*/
public class IntVec/*TypeVec*/ implements MemUsage.Instrumented, Iterable<IntVec/*TypeVec*/.Entry> {
  public interface Entry {
    int getIndex();
    int/*type*/ getValue();
    void setValue(int/*type*/ value);
  }

  public IntVec/*TypeVec*/() {
    this.data = new int/*type*/[0];
    this.n = 0;
  }
  public IntVec/*TypeVec*/(int cap) {
    this.data = new int/*type*/[cap];
    this.n = 0;
  }
  public IntVec/*TypeVec*/(int/*type*/[] data, int start, int end) {
    this.n = end-start;
    this.data = new int/*type*/[n];
    for(int i = 0; i < n; i++)
      this.data[i] = data[start+i];
  }

  public IntVec/*TypeVec*/(int/*type*/[] data) {
    this.data = data.clone();
    this.n = data.length;
  }

  public int/*type*/ get(int i) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    return data[i];
  }
  public int/*type*/ get(int i, int/*type*/ defaultValue) {
    if(i >= n) return defaultValue;
    return data[i];
  }
  public int/*type*/ set(int i, int/*type*/ x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] = x;
    return x;
  }
  public int/*type*/ increment(int i, int/*type*/ x) {
    if(i >= n) throw new ArrayIndexOutOfBoundsException();
    data[i] += x;
    return data[i];
  }
  // Set, but grow the array if necessary
  public int/*type*/ setGrow(int i, int/*type*/ x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] = x;
    return x;
  }
  public int/*type*/ incrementGrow(int i, int/*type*/ x) {
    if(i >= n) {
      if(i >= data.length) setCapacity((i+1)*2);
      n = i+1;
    }
    data[i] += x;
    return data[i];
  }
  // Append an element
  public void add(int/*type*/ x) { setGrow(n, x); }

  public void multAll(int/*type*/ d) {
    for(int i = 0; i < n; i++)
      data[i] *= d;
  }

  // Set the capacity of the array
  public void setCapacity(int cap) {
    if(cap < n) throw new ArrayIndexOutOfBoundsException();
    int/*type*/[] newData = new int/*type*/[cap];
    System.arraycopy(data, 0, newData, 0, n);
    data = newData;
  }
  public void trimToSize() { setCapacity(n); }
  public int size() { return n; }

  public int hashCode() {
    int h = n; 
    for(int i = 0; i < n; i++)
      h = h*29 + (Integer/*Type*/.valueOf(data[i]).hashCode());
    return h;
  }
  public boolean equals(Object o) {
    IntVec/*TypeVec*/ v = (IntVec/*TypeVec*/)o;
    if(n != v.n) return false;
    for(int i = 0; i < n; i++)
      if(data[i] != v.data[i]) return false;
    return true;
  }

  public int/*type*/[] getData() { return data; }  // Dangerous

  private int/*type*/[] data;
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
    public int/*type*/ getValue() { return data[index]; }
    public void setValue(int/*type*/ value) { data[index] = value; }
  }
  @Override public Iterator<Entry> iterator() { return new EntryIterator(); }
}
