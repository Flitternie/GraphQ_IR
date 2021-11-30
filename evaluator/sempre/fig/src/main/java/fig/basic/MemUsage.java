package fig.basic;

import java.util.*;
import java.lang.reflect.*;

/**
Simple utility for *approximately* estimating memory usage of objects on Java.
When to use this rather than a memory profiler?  When you want targeted control
over part of your program and you don't want to pay the overhead of the
profiler.

This utility is based on simple calculations (doesn't detect shared objects or
deal with memory alignment), so in a way it provides an upper bound on what the
program reasonably should be implemented (of course, the JVM will do
complicated things that make memory usage hard to compute).

Only use this for tree like structures.  Cycles will make it infinite loop.

Also note that the final memory usage (RES) of the entire process is generally
twice of that reported here due to JVM overhead.

To compute the number of bytes used an object:
  MemUsage.getBytes(object)

To convert this to a user-friendly string:
  MemUsage.getBytesStr(object)

If you create a custom class that is used in a collection (HashMap or
ArrayList), you can make it Instrumented:
  class Foo implements MemUsage.Instrumented {
    int[] a;
    int[] b;
    public long getBytes() {
      return MemUsage.objectSize(MemUsage.pointerSize * 2) +
             MemUsage.getBytes(a) +
             MemUsage.getBytes(b);
    }
  }

Note: sometimes we have to add 8 (e.g., in Pair to make theory match practice).

Further reading:
http://psy-lob-saw.blogspot.com/2013/05/know-thy-java-object-memory-layout.html
http://www.javaworld.com/article/2077408/core-java/sizeof-for-java.html
*/
public class MemUsage {
  public static int alignSize = 8;
  public static int pointerSize = 4;

  public static int booleanSize = 1;
  public static int byteSize = 1;
  public static int charSize = 2;
  public static int intSize = 4;
  public static int shortSize = 4;
  public static int floatSize = 4;
  public static int longSize = 8;
  public static int doubleSize = 8;

  private static int objectOverhead = 8;

  // Implement this interface if you want getBytes() to be called on your object
  // or collections containing your object.
  public interface Instrumented {
    public long getBytes();
  }

  public static String getBytesStr(Object o) {
    return Fmt.bytesToString(getBytes(o));
  }

  // n: number of bytes occupied by the fields of an object.
  // Add object overhead.
  // Return n rounded up to the nearest multiple of |alignSize|.
  public static int objectSize(int n) {
    n += objectOverhead;
    return (n + alignSize - 1) / alignSize * alignSize;
  }

  public static long getBytes(Object o) {
    if (o == null) return 0;
    if ("".equals(o)) return 0;

    // Primitives
    if (o instanceof Boolean) return objectSize(booleanSize);
    if (o instanceof Byte) return objectSize(byteSize);
    if (o instanceof Character) return objectSize(charSize);
    if (o instanceof Integer) return objectSize(intSize);
    if (o instanceof Short) return objectSize(shortSize);
    if (o instanceof Float) return objectSize(floatSize);
    if (o instanceof Long) return objectSize(longSize);
    if (o instanceof Double) return objectSize(doubleSize);

    // Primitive arrays
    if (o instanceof boolean[]) return getArraySize(((boolean[])o).length, booleanSize);
    if (o instanceof byte[]) return getArraySize(((byte[])o).length, byteSize);
    if (o instanceof char[]) return getArraySize(((char[])o).length, charSize);
    if (o instanceof int[]) return getArraySize(((int[])o).length, intSize);
    if (o instanceof short[]) return getArraySize(((short[])o).length, shortSize);
    if (o instanceof float[]) return getArraySize(((float[])o).length, floatSize);
    if (o instanceof long[]) return getArraySize(((long[])o).length, longSize);
    if (o instanceof double[]) return getArraySize(((double[])o).length, doubleSize);
    if (o instanceof Object[]) {
      Object[] l = (Object[])o;
      long sum = getArraySize(l.length, pointerSize);
      for (Object x : l) sum += getBytes(x);  // Recurse on contents
      return sum;
    }

    //System.out.println("getBytes: " + o.getClass());

    // This is not reliable because strings sometimes share the underlying char
    // array.
    if (o instanceof String)
      return 28 + 2 * ((String)o).length();  // Determined empirically

    if (o instanceof ArrayList) {
      ArrayList l = (ArrayList)o;
      return 36 + getBytes(getArrayListData(l));
    }

    if (o instanceof LinkedHashMap) {
      HashMap m = (HashMap)o;
      Object[] l = getHashMapData(m);
      // Hack: Add space for header
      return 45 + getBytes(l) + l.length * 12;
    }

    if (o instanceof HashMap) {
      HashMap m = (HashMap)o;
      return 45 + getBytes(getHashMapData(m));
    }

    if (o instanceof HashSet) {
      HashSet s = (HashSet)o;
      return 45 + getBytes(getHashSetData(s));
    }

    if (o instanceof Map.Entry) {
      // pointers to key, value, next, hash
      return objectSize(pointerSize * 4) +
             24 +  // Hack to make numbers agree more empirically, but not perfect
             getBytes(((Map.Entry)o).getKey()) +
             getBytes(((Map.Entry)o).getValue());
    }

    if (o instanceof Instrumented)
      return ((Instrumented)o).getBytes();

    if (o.getClass() == Object.class)
      return objectSize(0);

    if (o.getClass() == sublistClass)
      return objectSize(MemUsage.pointerSize + MemUsage.intSize * 3) + 16;

    throw new RuntimeException("Unhandled: " + o.getClass());
  }
  private static Class sublistClass = new ArrayList().subList(0, 0).getClass();

  ////////////////////////////////////////////////////////////
  // Helper methods.

  // Hack: to get ArrayList.elementData
  private static Field arrayListDataField;
  private static <T> T[] getArrayListData(ArrayList<T> l) {
    if (arrayListDataField == null) {
      try {
        arrayListDataField = ArrayList.class.getDeclaredField("elementData");
        arrayListDataField.setAccessible(true);
      } catch (Exception e) {
        throw new ExceptionInInitializerError(e);
      }
    }
    try {
      return (T[])arrayListDataField.get(l);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  // Hack: to get HashMap.table
  private static Field hashMapDataField;
  private static <S, T> Map.Entry<S, T>[] getHashMapData(HashMap<S, T> m) {
    if (hashMapDataField == null) {
      try {
        hashMapDataField = HashMap.class.getDeclaredField("table");
        hashMapDataField.setAccessible(true);
      } catch (Exception e) {
        throw new ExceptionInInitializerError(e);
      }
    }
    try {
      return (Map.Entry<S, T>[])hashMapDataField.get(m);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  // Hack: to get HashSet.map
  private static Field hashSetDataField;
  private static <T,U> HashMap<T,U> getHashSetData(HashSet<T> m) {
    if (hashSetDataField == null) {
      try {
        hashSetDataField = HashSet.class.getDeclaredField("map");
        hashSetDataField.setAccessible(true);
      } catch (Exception e) {
        throw new ExceptionInInitializerError(e);
      }
    }
    try {
      return (HashMap<T, U>)hashSetDataField.get(m);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  // Hack: to get LinkedHashMap.map
  private static Field linkedHashMapDataField;
  private static <S, T> HashMap<S, T> getLinkedHashMapData(LinkedHashMap<S, T> m) {
    if (linkedHashMapDataField == null) {
      try {
        linkedHashMapDataField = LinkedHashMap.class.getDeclaredField("map");
        linkedHashMapDataField.setAccessible(true);
      } catch (Exception e) {
        throw new ExceptionInInitializerError(e);
      }
    }
    try {
      return (HashMap<S, T>)linkedHashMapDataField.get(m);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  private static long getArraySize(int n, int size) {
    // Store the length of an array (4) + extra (4)
    return objectSize(n * size + 4 + 4);
  }
}
