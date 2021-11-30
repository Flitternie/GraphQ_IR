package fig.basic;

import static fig.basic.LogInfo.*;
import java.io.*;
import java.util.*;

/**
 * Provides a map from strings to doubles.
 * Motivation: provides a specialized data structure for
 * mapping strings to doubles which is both fast and space efficient.
 * Feature 1:
 * You can switch between two representations of the map:
 *   - Sorted list (lookups involve binary search)
 *   - Hash table with linear probing (lookups involve hashing)
 * Feature 2:
 * Sometimes, we want several maps with the same set of keys.
 * If we lock the map, we can share the same keys between several
 * maps, which saves space.
 *
 * Note: in the sorted list, we first sort the keys by
 * hash code, and then for equal hash code, we sort by the string
 * values.  We hope that hash code collisions will be rare enough
 * that we won't have to resort to comparing strings.
 *
 * Typical usage:
 *   - Construct a map using a hash table.
 *   - To save space, switch to a sorted list representation.
 *
 * TODO: support remove operation.
 * TODO: turn the string into a generic.  Don't know how to do this properly.
 *
 * DON'T USE THIS ANYMORE; use TDoubleMap.
 */
@Deprecated public class StringDoubleMap implements Iterable<StringDoubleMap.Entry>, Serializable {
  private static final long serialVersionUID = 42;

  public StringDoubleMap() {
    this(defaultExpectedSize);
  }

  /**
   * expectedSize: expected number of entries we're going to have in the map.
   */
  public StringDoubleMap(int expectedSize) {
    this.mapType = MapType.HASH_TABLE;
    this.locked = false;
    this.num = 0;
    allocate(getCapacity(num, false));
    this.numCollisions = 0;
  }

  // Main operations
  public boolean containsKey(String key) {
    return find(key, false) != -1;
  }
  public double get(String key, double defaultValue) {
    int i = find(key, false);
    return i == -1 ? defaultValue : values[i];
  }
  public double getWithErrorMsg(String key, double defaultValue) {
    int i = find(key, false);
    if(i == -1) errors("%s not in map, using %f", key, defaultValue);
    return i == -1 ? defaultValue : values[i];
  }
  public double getSure(String key) {
    // Throw exception if key doesn't exist.
    int i = find(key, false);
    if(i == -1) throw new RuntimeException("Missing key: " + key);
    return values[i];
  }
  public void put(String key, double value) {
    assert !Double.isNaN(value);
    int i = find(key, true);
    keys[i] = key;
    values[i] = value;
  }
  public void incr(String key, double dValue) {
    int i = find(key, true);
    keys[i] = key;
    if(Double.isNaN(values[i])) values[i] = dValue; // New value
    else values[i] += dValue;
  }
  public void scale(String key, double dValue) {
    int i = find(key, true);
    if(i == -1) return;
    values[i] *= dValue;
  }
  public int size() { return num; }
  public int capacity() { return keys.length; }
  /*public void clear() { // Keep the same capacity
    num = 0;
    for(int i = 0; i < keys.length; i++)
      keys[i] = null;
  }*/
  public void gut() { values = null; } // Save memory

  // Simple operations on values
  // Implement them here for maximum efficiency.
  public double sum() {
    double sum = 0;
    for(int i = 0; i < keys.length; i++)
      if(keys[i] != null)
        sum += values[i];
    return sum;
  }
  public void putAll(double value) {
    for(int i = 0; i < keys.length; i++)
      if(keys[i] != null)
        values[i] = value;
  }
  public void incrAll(double dValue) {
    for(int i = 0; i < keys.length; i++)
      if(keys[i] != null)
        values[i] += dValue;
  }
  public void multAll(double dValue) {
    for(int i = 0; i < keys.length; i++)
      if(keys[i] != null)
        values[i] *= dValue;
  }

  // If keys are locked, we can share the same keys.
  public StringDoubleMap copy() {
    StringDoubleMap newMap = new StringDoubleMap();
    newMap.mapType = mapType;
    newMap.locked = locked;
    newMap.num = num;
    newMap.keys = locked ? keys : (String[])keys.clone(); // Share keys!
    newMap.values = (double[])values.clone();
    return newMap;
  }
  // Return a map with only keys in the set
  public StringDoubleMap restrict(Set<String> set) {
    StringDoubleMap newMap = new StringDoubleMap();
    newMap.mapType = mapType;
    if(mapType == MapType.SORTED_LIST) {
      newMap.allocate(getCapacity(num, false));
      for(int i = 0; i < keys.length; i++) {
        if(set.contains(keys[i])) {
          newMap.keys[newMap.num] = keys[i];
          newMap.values[newMap.num] = values[i];
          newMap.num++;
        }
      }
    }
    else if(mapType == MapType.HASH_TABLE) {
      for(int i = 0; i < keys.length; i++)
        if(keys[i] != null && set.contains(keys[i]))
          newMap.put(keys[i], values[i]);
    }
    newMap.locked = locked;
    return newMap;
  }

  // For sorting the entries.
  private static class FullEntry implements Comparable<FullEntry> {
    private FullEntry(String key, double value) {
      this.key = key;
      this.value = value;
    }

    public int compareTo(FullEntry e) {
      int h1 = hash(key);
      int h2 = hash(e.key);
      if(h1 != h2) return h1-h2;
      return key.compareTo(e.key);
    }

    private final String key;
    private final double value;
  }

  // Compare by value.
  public class EntryValueComparator implements Comparator<Entry> {
    public int compare(Entry e1, Entry e2) {
      return Double.compare(values[e1.i], values[e2.i]);
    }
  }
  public EntryValueComparator entryValueComparator() { return new EntryValueComparator(); }

  // For iterating.
  public class Entry {
    private Entry(int i) { this.i = i; }

    public String getKey() { return keys[i]; }
    public double getValue() { return values[i]; }
    public void setValue(double newValue) { values[i] = newValue; }

    private final int i;
  }

  public void lock() {
    locked = true;
  }
  public void switchToSortedList() {
    switchMapType(MapType.SORTED_LIST);
  }
  public void switchToHashTable() {
    switchMapType(MapType.HASH_TABLE);
  }

  ////////////////////////////////////////////////////////////

  public class EntrySet extends AbstractSet<Entry> {
    public Iterator<Entry> iterator() { return new EntryIterator(); }
    public int size() { return num; }
    public boolean contains(Object o) { throw new UnsupportedOperationException(); }
    public boolean remove(Object o) { throw new UnsupportedOperationException(); }
    public void clear() { throw new UnsupportedOperationException(); }
  }
  public class KeySet extends AbstractSet<String> {
    public Iterator<String> iterator() { return new KeyIterator(); }
    public int size() { return num; }
    public boolean contains(Object o) { return containsKey((String)o); }
    public boolean remove(Object o) { throw new UnsupportedOperationException(); }
    public void clear() { throw new UnsupportedOperationException(); }
  }
  public class ValueCollection extends AbstractCollection<Double> {
    public Iterator<Double> iterator() { return new ValueIterator(); }
    public int size() { return num; }
    public boolean contains(Object o) { throw new UnsupportedOperationException(); }
    public void clear() { throw new UnsupportedOperationException(); }
  }
  public EntryIterator iterator() { return new EntryIterator(); }
  public EntrySet entrySet() { return new EntrySet(); }
  public KeySet keySet() { return new KeySet(); }
  public ValueCollection values() { return new ValueCollection(); }

  // WARNING: no checks that this iterator is only used when
  // the map is not being structurally changed
  private class EntryIterator extends MapIterator<Entry> {
    public Entry next() { return new Entry(nextIndex()); }
  }
  private class KeyIterator extends MapIterator<String> {
    public String next() { return keys[nextIndex()]; }
  }
  private class ValueIterator extends MapIterator<Double> {
    public Double next() { return values[nextIndex()]; }
  }
  private abstract class MapIterator<E> implements Iterator<E> {
    public MapIterator() {
      if(mapType == MapType.SORTED_LIST) end = size();
      else end = capacity();
      next = -1;
      nextIndex();
    }

    public boolean hasNext() { return next < end; }
    int nextIndex() {
      int curr = next;
      do { next++; } while(next < end && keys[next] == null);
      return curr;
    }
    public void remove() { throw new UnsupportedOperationException(); }

    private int next, end;
  }

  ////////////////////////////////////////////////////////////

  /** How much capacity do we need for this type of map,
   * given that we want n elements.
   * compact: whether we want to save space and don't plan on growing.
   */
  private int getCapacity(int n, boolean compact) {
    int capacity;
    if(mapType == MapType.SORTED_LIST)
      capacity = compact ? n : n*growFactor;
    else if(mapType == MapType.HASH_TABLE)
      capacity = n*growFactor;
    else throw new RuntimeException("Internal bug");
    return Math.max(capacity, 1);
  }

  /**
   * Convert the map to the given type.
   */
  private void switchMapType(MapType newMapType) {
    assert !locked;

    //System.out.println("switchMapType(" + newMapType + ", " + compact + ")");

    // Save old keys and values, allocate space
    String[] oldKeys = keys;
    double[] oldValues = values;
    mapType = newMapType;
    allocate(getCapacity(num, true));
    numCollisions = 0;

    if(newMapType == MapType.SORTED_LIST) {
      // Sort the keys
      FullEntry[] entries = new FullEntry[num];
      for(int i = 0, j = 0; i < oldKeys.length; i++)
        if(oldKeys[i] != null)
          entries[j++] = new FullEntry(oldKeys[i], oldValues[i]);
      Arrays.sort(entries);

      // Populate the sorted list
      for(int i = 0; i < num; i++) {
        keys[i] = entries[i].key;
        values[i] = entries[i].value;
      }
    }
    else if(mapType == MapType.HASH_TABLE) {
      // Populate the hash table
      num = 0;
      for(int i = 0; i < oldKeys.length; i++) {
        if(oldKeys[i] != null)
          put(oldKeys[i], oldValues[i]);
      }
    }
  }

  /**
   * Return the first index i for which the target key is less than or equal to
   * key i (00001111).  Should insert target key at position i.
   * If target is larger than all of the elements, return size().
   */
  private int binarySearch(String targetKey) {
    int targetHash = hash(targetKey);
    int l = 0, u = num;
    while(l < u) {
      //System.out.println(l);
      int m = (l+u) >> 1;
      int keyHash = hash(keys[m]);
      if(targetHash < keyHash || (targetHash == keyHash && targetKey.compareTo(keys[m]) <= 0))
        u = m;
      else
        l = m+1;
    }
    return l;
  }

  // Modified hash (taken from HashMap.java).
  private static int hash(String x) {
    int h = x.hashCode();
    h += ~(h << 9);
    h ^=  (h >>> 14);
    h +=  (h << 4);
    h ^=  (h >>> 10);
    if(h < 0) h = -h; // New
    return h;
  }

  /**
   * Modify is whether to make room for the new key if it doesn't exist.
   * If a new entry is created, the value at that position will be Double.NaN.
   */
  private int find(String key, boolean modify) {
    //System.out.println("find " + key + " " + modify + " " + mapType + " " + capacity());

    if(mapType == MapType.SORTED_LIST) {
      // Binary search
      int i = binarySearch(key);
      if(i < num && keys[i] != null && key.equals(keys[i])) return i;
      if(modify) {
        if(locked)
          throw new RuntimeException("Cannot make new entry for " + key + ", because map is locked");

        if(num == capacity())
          changeSortedListCapacity(getCapacity(num+1, false));

        // Shift everything forward
        for(int j = num; j > i; j--) {
          keys[j] = keys[j-1];
          values[j] = values[j-1];
        }
        num++;
        values[i] = Double.NaN;
        return i;
      }
      else
        return -1;
    }
    else if(mapType == MapType.HASH_TABLE) {
      int capacity = capacity();
      int keyHash = hash(key);
      int i = keyHash % capacity;
      if(i < 0) i = -i; // Arbitrary transformation

      // Make sure big enough
      if(modify && num > loadFactor*capacity) {
        if(locked)
          throw new RuntimeException("Cannot make new entry for " + key + ", because map is locked");

        switchMapType(MapType.HASH_TABLE);
        return find(key, modify);
      }

      //System.out.println("!!! " + keyHash + " " + capacity);
      while(keys[i] != null && !keys[i].equals(key)) { // Collision
        i++;
        numCollisions++;
        if(i == capacity) i = 0;
      }
      if(keys[i] != null) { // Found
        assert key.equals(keys[i]);
        return i;
      }
      if(modify) { // Not found
        num++;
        values[i] = Double.NaN;
        return i;
      }
      else
        return -1;
    }
    else
      throw new RuntimeException("Internal bug: " + mapType);
  }

  private void allocate(int n) {
    keys = new String[n];
    values = new double[n];
  }

  // Resize the sorted list to the new capacity.
  private void changeSortedListCapacity(int newCapacity) {
    assert mapType == MapType.SORTED_LIST;
    assert newCapacity >= num;
    String[] oldKeys = keys;
    double[] oldValues = values;
    allocate(newCapacity);
    System.arraycopy(oldKeys, 0, keys, 0, num);
    System.arraycopy(oldValues, 0, values, 0, num);
  }

  // Check consistency of data structure.
  private void repCheck() {
    assert capacity() > 0;
    if(mapType == MapType.SORTED_LIST) {
      assert num <= capacity();
      for(int i = 1; i < num; i++) { // Make sure keys are sorted.
        int h1 = hash(keys[i-1]);
        int h2 = hash(keys[i]);
        assert h1 <= h2;
        if(h1 == h2)
          assert keys[i-1].compareTo(keys[i]) < 0;
      }
    }
  }

  private void debugDump() {
    System.out.println("--------------------");
    System.out.println("mapType = " + mapType);
    System.out.println("locked = " + locked);
    System.out.println("size/capacity = " + size() + "/" + capacity());
    System.out.println("numCollisions = " + numCollisions);
    /*for(int i = 0; i < keys.length; i++) {
      System.out.printf("[%d] %s (%d) => %f\n", i, keys[i], (keys[i] == null ? 0 : keys[i].hashCode()), values[i]);
    }*/
  }

  /**
   * Format: mapType, num, (key, value) pairs
   */
  private void writeObject(ObjectOutputStream out) throws IOException {
    out.writeObject(mapType);
    out.writeInt(num);
    for(Entry e : this) {
      out.writeObject(e.getKey());
      out.writeDouble(e.getValue());
    }
  }
  private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    this.mapType = (MapType)in.readObject();
    this.num = 0;
    this.locked = false;

    int n = in.readInt();
    allocate(getCapacity(n, true));

    for(int i = 0; i < n; i++) {
      String key = ((String)in.readObject()).intern();
      double value = in.readDouble();
      if(mapType == MapType.SORTED_LIST) {
        // Assume keys and values serialized in sorted order
        keys[num] = key;
        values[num] = value;
        num++;
      }
      else if(mapType == MapType.HASH_TABLE) {
        put(key, value);
      }
    }
  }

  ////////////////////////////////////////////////////////////

  private static final int growFactor = 2; // How much extra space (times size) to give for the capacity
  private static final int defaultExpectedSize = 0;
  private static final double loadFactor = 0.75; // For hash table
  private enum MapType { SORTED_LIST, HASH_TABLE }

  private MapType mapType;
  private boolean locked; // Are the keys locked
  private int num;
  private String[] keys;
  private double[] values;
  private int numCollisions; // For debugging

  ////////////////////////////////////////////////////////////

  static void check(Set<Integer> set, StringDoubleMap map) {
    for(int x : set) {
      double value = map.getSure(""+x);
      assert value == 1.0*x;
    }
    for(StringDoubleMap.Entry e : map) {
      int x = Integer.parseInt(e.getKey());
      assert set.contains(x);
      assert e.getValue() == 1.0*x;
    }
  }
  static StringDoubleMap test(int n, int range) {
    // Generate random data
    Random rand = new Random();
    Set<Integer> set = new HashSet<Integer>();
    for(int i = 0; i < n; i++)
      set.add(rand.nextInt(range));

    // Make the map
    StringDoubleMap map = new StringDoubleMap(0);
    //map.switchToSortedList();
    for(int x : set) {
      map.put(""+x, 1.0*x);
    }

    //System.out.println("here");
    check(set, map);
    map.switchToSortedList();
    check(set, map);
    map.switchToHashTable();
    check(set, map);

    map.lock();
    for(int x : set)
      map.put(""+x, 1.0*x);

    assert set.size() == map.size();
    return map;
  }

  public static void main(String[] args) throws Exception {
    // Test
    int T = 200;
    int n = 10000;
    if(args[0].equals("ser")) {
      StringDoubleMap map = test(10000, 10000);
      map.locked = false; // Cheat
      map.switchToSortedList();

      ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("map"));
      out.writeObject(map);
      out.close();

      ObjectInputStream in = new ObjectInputStream(new FileInputStream("map"));
      StringDoubleMap map2 = (StringDoubleMap)in.readObject();
      in.close();

      assert map.size() == map2.size();
      for(StringDoubleMap.Entry e : map) {
        assert map2.getSure(e.getKey()) == e.getValue();
      }
    }
    else if(args[0].equals("test")) {
      for(int i = 0; ; i++) {
        System.out.println("test " + i);
        test(10000, 10000);
      }
    }
    else if(args[0].equals("sdm")) {
      StringDoubleMap map = new StringDoubleMap();

      for(int q = 0; q < T; q++) {
        //System.out.println(q);
        for(int i = 0; i < n; i++) {
          //if(q > 0) System.out.println("put " + i);
          map.put(i+"key"+i, i+q);
          //map.debugDump();
          //if(q == 1 && i == 1000)
            //map.switchToHashTable();
        }
        if(q == 0) {
          map.switchToSortedList();
          //map.repCheck();
          //map.lock();
          map.debugDump();
        }
      }
    }
    else {
      HashMap<String, Double> omap = new HashMap<String, Double>();
      for(int q = 0; q < T; q++) {
        for(int i = 0; i < n; i++) {
          omap.put(i+"key"+i, 1.0+i+q);
        }
      }
    }

    /*map.switchToSortedList();
    map.debugDump();

    map.switchToHashTable();
    map.debugDump();

    map.switchToSortedList();
    map.debugDump();

    for(Entry e : map)
      System.out.println(e.getKey() + " => " + e.getValue());*/
  }

  public TDoubleMap toTDoubleMap() {
    TDoubleMap map = new TDoubleMap();
    for(int i = 0; i < keys.length; i++)
      if(keys[i] != null)
        map.put(keys[i], values[i]);
    return map;
  }
}
