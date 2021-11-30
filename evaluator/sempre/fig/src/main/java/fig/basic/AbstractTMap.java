package fig.basic;

import static fig.basic.LogInfo.*;
import java.io.*;
import java.util.*;

/**
 * Just a dummy class.
 * TODO: move common functionality here.
 */
public abstract class AbstractTMap<T> implements Serializable, MemUsage.Instrumented {
  protected static final long serialVersionUID = 42;

  public static class Functionality<T> implements Serializable {
    public T[] createArray(int n) { return (T[])(new Object[n]); }
    public T intern(T x) { return x; } // Override to get desired behavior, e.g., interning
  }
  public static class ObjectFunctionality extends Functionality<Object> {
    public Object[] createArray(int n) { return new Object[n]; }
  }
  public static Functionality defaultFunctionality = new Functionality();

  protected static final int growFactor = 2; // How much extra space (times size) to give for the capacity
  protected static final int defaultExpectedSize = 2;
  protected static final double loadFactor = 0.75; // For hash table
  protected enum MapType { SORTED_LIST, HASH_TABLE }

  protected MapType mapType;
  protected boolean locked; // Are the keys locked
  protected int num;
  protected T[] keys;
  protected Functionality<T> keyFunc;
  protected int numCollisions; // For debugging

  // Override to add values.
  public long getBytes() {
    return MemUsage.objectSize(MemUsage.pointerSize * 3 + MemUsage.booleanSize + MemUsage.intSize * 2) + MemUsage.getBytes(keys);
  }
}
