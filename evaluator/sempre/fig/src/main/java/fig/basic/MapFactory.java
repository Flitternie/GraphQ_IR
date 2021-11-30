package fig.basic;

import java.util.*;
import java.io.Serializable;

/**
 * The MapFactory is a mechanism for specifying what kind of map is to be used
 * by some object.  For example, if you want a Counter which is backed by an
 * IdentityHashMap instead of the defaul HashMap, you can pass in an
 * IdentityHashMapFactory.
 *
 * @author Dan Klein
 */

public abstract class MapFactory<K,V> {
  private static final long serialVersionUID = 5724671156522771657L;
  public static class HashMapFactory<K,V> extends MapFactory<K,V> {
    private static final long serialVersionUID = 5724671156522771657L;
    public Map<K,V> buildMap() {
      return new HashMap<K,V>();
    }
  }

  public static class IdentityHashMapFactory<K,V> extends MapFactory<K,V> {
    private static final long serialVersionUID = 5724671156522771657L;
    public Map<K,V> buildMap() {
      return new IdentityHashMap<K,V>();
    }
  }

  public static class TreeMapFactory<K,V> extends MapFactory<K,V> {
    private static final long serialVersionUID = 5724671156522771657L;
    public Map<K,V> buildMap() {
      return new TreeMap<K,V>();
    }
  }

  public static class WeakHashMapFactory<K,V> extends MapFactory<K,V> {
    private static final long serialVersionUID = 5724671156522771657L;
    public Map<K,V> buildMap() {
      return new WeakHashMap<K,V>();
    }
  }

  public abstract Map<K,V> buildMap();
}

