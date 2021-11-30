package fig.basic;

import java.io.*;
import java.util.*;

// Test MemUsage class and compare with real memory usage.
// Getting a hold of real memory usage is a bit delicate and hacky right now,
// but it's just used as a sanity check.
public class MemUsageTester {
  // When nothing has been allocated, how much memory is being used.
  static long initFreeMemory = -1;
  static long initTotalMemory = -1;

  ////////////////////////////////////////////////////////////
  // Helper methods for allocating data structures.

  interface ObjectFactory {
    public Object newObject();
  }

  static ObjectFactory newDouble() {
    return new ObjectFactory() {
      public Object newObject() { return new Double(12345); }
    };
  }

  static ArrayList l = new ArrayList();
  static ObjectFactory newArrayListSubList() {
    return new ObjectFactory() {
      public Object newObject() { return l.subList(0, 0); }
    };
  }

  static ObjectFactory newSubList() {
    return new ObjectFactory() {
      public Object newObject() { return new SubList(l, 0, 0); }
    };
  }

  static ObjectFactory newIntPair() {
    return new ObjectFactory() {
      public Object newObject() { return new IntPair(); }
    };
  }

  static ObjectFactory newIntBoolPair() {
    return new ObjectFactory() {
      public Object newObject() { return new IntBoolPair(); }
    };
  }

  static ObjectFactory newObjectDoublePair(final ObjectFactory key) {
    return new ObjectFactory() {
      public Object newObject() { return new ObjectDoublePair(key.newObject(), 12345); }
    };
  }

  static ObjectFactory newIntTriple() {
    return new ObjectFactory() {
      public Object newObject() { return new IntTriple(); }
    };
  }

  static ObjectFactory newPair(final ObjectFactory first, final ObjectFactory second) {
    return new ObjectFactory() {
      public Object newObject() {
        return new Pair(first.newObject(), second.newObject());
      }
    };
  }

  static ObjectFactory newLispTree(final int breadth, final int depth) {
    return new ObjectFactory() {
      public Object newObject() {
        return recurse(depth);
      }
      LispTree recurse(int d) {
        if (d == 0) return LispTree.proto.newLeaf("");
        LispTree tree = LispTree.proto.newList();
        for (int i = 0; i < breadth; i++)
          tree.addChild(recurse(d-1));
        return tree;
      }
    };
  }

  static ObjectFactory newIntArray(final int n) {
    return new ObjectFactory() {
      public Object newObject() { return new int[n]; }
    };
  }

  static ObjectFactory newString(final int n) {
    return new ObjectFactory() {
      public Object newObject() {
        StringBuilder buf = new StringBuilder();
        for (int i = 0; i < n; i++)
          buf.append('*');
        return buf.toString();
      }
    };
  }

  static ObjectFactory newArrayList(final int n, final ObjectFactory elem) {
    return new ObjectFactory() {
      public Object newObject() {
        ArrayList l = new ArrayList();
        for (int i = 0; i < n; i++)
          l.add(elem.newObject());
        return l;
      }
    };
  }

  static ObjectFactory newArray(final int n, final ObjectFactory elem) {
    return new ObjectFactory() {
      public Object newObject() {
        Object[] l = new Object[n];
        for (int i = 0; i < n; i++)
          l[i] = elem.newObject();
        return l;
      }
    };
  }

  static ObjectFactory newHashSet(final int n, final ObjectFactory elem) {
    return new ObjectFactory() {
      public Object newObject() {
        HashSet s = new HashSet();
        for (int i = 0; i < n; i++)
          s.add(elem.newObject());
        return s;
      }
    };
  }

  static ObjectFactory newHashMap(final int n, final ObjectFactory key, final ObjectFactory value) {
    return new ObjectFactory() {
      public Object newObject() {
        HashMap m = new HashMap();
        for (int i = 0; i < n; i++)
          m.put(key.newObject(), value.newObject());
        return m;
      }
    };
  }

  static ObjectFactory newLinkedHashMap(final int n, final ObjectFactory key, final ObjectFactory value) {
    return new ObjectFactory() {
      public Object newObject() {
        HashMap m = new LinkedHashMap();
        for (int i = 0; i < n; i++)
          m.put(key.newObject(), value.newObject());
        return m;
      }
    };
  }

  static class C1 implements MemUsage.Instrumented {
    public long getBytes() {
      // For some reason, there is extra overhead.
      return MemUsage.objectSize(0) + 8;
    }
  }

  static class C2 implements MemUsage.Instrumented {
    int[] x = new int[64];
    int[] y = new int[64];
    public long getBytes() {
      return MemUsage.objectSize(MemUsage.pointerSize * 2) +
             MemUsage.getBytes(x) + MemUsage.getBytes(y);
    }
  }

  static ObjectFactory newC1() {
    return new ObjectFactory() {
      public Object newObject() { return new C1(); }
    };
  }

  static ObjectFactory newC2() {
    return new ObjectFactory() {
      public Object newObject() { return new C2(); }
    };
  }

  ////////////////////////////////////////////////////////////

  static void run(String description, Object o) {
    if (o instanceof ObjectFactory)
      o = ((ObjectFactory)o).newObject();
    gc();
    if (o == null) {
      //System.out.println(Runtime.getRuntime().freeMemory() + " " + Runtime.getRuntime().totalMemory());
      initFreeMemory = Runtime.getRuntime().freeMemory();
      initTotalMemory = Runtime.getRuntime().totalMemory();
    }
    long actual = (Runtime.getRuntime().totalMemory() - initTotalMemory) -
                  (Runtime.getRuntime().freeMemory() - initFreeMemory);
    long predicted = MemUsage.getBytes(o);
    double error = Math.abs(1.0 * (predicted - actual) / Math.max(actual, 1));
    System.out.println(description + ": " +
                       "predicted: " + predicted + " (" + Fmt.bytesToString(predicted) +"); " +
                       "actual: " + actual + " (" + Fmt.bytesToString(actual) + "); " + 
                       "error: " + error + (error > 0.1 ? " (BIG ERROR)" : ""));
  }

  static void gc() { System.gc(); }

  public static void main(String[] args) {
    // Important: calibrate.
    run("null", null); gc();
    run("null", null); gc();

    // Generally have to run things separately, or else measurements won't be accurate.
    for (String arg : args) {
      int i = Integer.parseInt(arg);

      if (i == 0) {
        run("boolean[]", new boolean[10000000]); gc();
        run("byte[]", new byte[10000000]); gc();
        run("char[]", new char[10000000]); gc();
        run("int[]", new int[10000000]); gc();
        run("long[]", new long[10000000]); gc();
        run("Object[]", new Object[10000000]); gc();
        run("Object[]", newArray(100000, newIntArray(2))); gc();
        run("int[][]", new int[1000][10000]); gc();
        run("int[][0]", new int[1000000][0]); gc();
        run("int[][1]", new int[1000000][1]); gc();
        run("int[][2]", new int[1000000][2]); gc();
        run("int[][3]", new int[1000000][3]); gc();
        run("int[][4]", new int[1000000][4]); gc();
        run("int[][][]", new int[100][100][100]); gc();
      } else if (i == 1) {
        run("String", newString(1000000)); gc();  // Not accurate
        run("String", newString(10000000)); gc();
        run("String", newArray(10000, newString(10))); gc();
        run("String", newArray(1000, newString(100))); gc();
      } else if (i == 2) {
        run("ArrayList", new ArrayList(10000000)); gc();
        run("ArrayList", newArrayList(10000, newIntArray(2))); gc();
        run("ArrayList", newArrayList(100000, newIntArray(2))); gc();
        run("ArrayList", newArrayList(1000000, newIntArray(2))); gc();
      } else if (i == 3) {
        run("HashMap", new HashMap(1000000)); gc();
        run("HashMap", newHashMap(1000, newIntArray(2), newIntArray(2))); gc();
        run("HashMap", newHashMap(10000, newIntArray(2), newIntArray(2))); gc();
        run("HashMap", newHashMap(100000, newIntArray(2), newIntArray(2))); gc();
        run("HashSet", newHashSet(1000, newIntArray(2))); gc();
        run("HashSet", newHashSet(10000, newIntArray(2))); gc();
        run("LinkedHashMap", newLinkedHashMap(10000, newIntArray(2), newIntArray(2))); gc();
        run("HashMap[]", newArray(10000, newHashMap(2, newIntArray(2), newIntArray(2)))); gc();
      } else if (i == 4) {
        run("C1", newArray(100000, newC1())); gc();
        run("C2", newArray(100000, newC2())); gc();
        run("IntPair", newArray(100000, newIntPair())); gc();
        run("IntBoolPair", newArray(100000, newIntBoolPair())); gc();
        run("IntTriple", newArray(100000, newIntTriple())); gc();
        run("Pair", newArray(100000, newPair(newIntArray(2), newIntArray(2)))); gc();
        run("Pair", newArray(100000, newPair(newIntArray(2), newDouble()))); gc();
        run("ObjectDoublePair", newArray(100000, newObjectDoublePair(newIntArray(2)))); gc();
        run("LispTree", newArray(100000, newLispTree(2, 2))); gc();
        run("ArrayList.SubList", newArray(100000, newArrayListSubList())); gc();
        run("SubList", newArray(100000, newSubList())); gc();
      } else if (i == -1) {
        try { System.in.read(); }
        catch (IOException e) { }
      }
    }
  }
}
