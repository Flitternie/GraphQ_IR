package fig.basic;

import fig.basic.*;
import static fig.basic.LogInfo.*;
import java.io.*;
import java.util.*;

/** Maps (string, string) pairs to doubles.
 * Based on StringDoubleMap.
 * It's useful when the number of second strings for a fixed first string
 * is small.
 * Most of the operations in this class parallel that of StringDoubleMap,
 * but just applied to two keys.  The implementation is essentially dispatching
 * down to StringDoubleMap.
 * Typical usage: conditional probability table.
 */
@Deprecated public class String2DoubleMap implements Iterable<Map.Entry<String, StringDoubleMap>>, Serializable {
  private static final long serialVersionUID = 42;

  // Main operations
  public boolean containsKey(String key1, String key2) {
    StringDoubleMap map = getMap(key1, false);
    return map != null && map.containsKey(key2);
  }
  public double get(String key1, String key2, double defaultValue) {
    StringDoubleMap map = getMap(key1, false);
    return map == null ? defaultValue : map.get(key2, defaultValue);
  }
  public double getWithErrorMsg(String key1, String key2, double defaultValue) {
    StringDoubleMap map = getMap(key1, false);
    if(map == null) errors("(%s, %s) not in map, using %f", key1, key2, defaultValue);
    return map == null ? defaultValue : map.get(key2, defaultValue);
  }
  public double getSure(String key1, String key2) {
    // Throw exception if key doesn't exist.
    StringDoubleMap map = getMap(key1, false);
    if(map == null) throw new RuntimeException("Missing key: " + key1);
    return map.getSure(key2);
  }
  public void put(String key1, StringDoubleMap map) { // Risky
    if(locked)
      throw new RuntimeException("Cannot make new entry for " + key1 + ", because map is locked");
    maps.put(key1, map);
  }
  public void put(String key1, String key2, double value) {
    StringDoubleMap map = getMap(key1, true);
    map.put(key2, value);
  }
  public void incr(String key1, String key2, double dValue) {
    StringDoubleMap map = getMap(key1, true);
    map.incr(key2, dValue);
  }
  public void scale(String key1, String key2, double dValue) {
    StringDoubleMap map = getMap(key1, true);
    map.scale(key2, dValue);
  }
  public int size() { return maps.size(); }
  // Return number of entries
  public int totalSize() {
    int n = 0;
    for(StringDoubleMap map : maps.values())
      n += map.size();
    return n;
  }
  public void gut() {
    for(StringDoubleMap map : maps.values())
      map.gut();
  }

  public Iterator<Map.Entry<String, StringDoubleMap>> iterator() {
    return maps.entrySet().iterator();
  }
  public Set<Map.Entry<String, StringDoubleMap>> entrySet() { return maps.entrySet(); }
  public Set<String> keySet() { return maps.keySet(); }
  public Collection<StringDoubleMap> values() { return maps.values(); }

  public void multAll(double dValue) {
    for(StringDoubleMap map : maps.values())
      map.multAll(dValue);
  }

  // If keys are locked, we can share the same keys.
  public String2DoubleMap copy() {
    return copy(newMap());
  }
  public String2DoubleMap copy(String2DoubleMap newMap) {
    newMap.locked = locked;
    for(Map.Entry<String, StringDoubleMap> e : maps.entrySet())
      newMap.maps.put(e.getKey(), e.getValue().copy());
    return newMap;
  }
  public String2DoubleMap restrict(Set<String> set1, Set<String> set2) {
    return restrict(newMap(), set1, set2);
  }
  public String2DoubleMap restrict(String2DoubleMap newMap, Set<String> set1, Set<String> set2) {
    newMap.locked = locked;
    for(Map.Entry<String, StringDoubleMap> e : maps.entrySet())
      if(set1.contains(e.getKey()))
        newMap.maps.put(e.getKey(), e.getValue().restrict(set2));
    return newMap;
  }
  public String2DoubleMap reverse(String2DoubleMap newMap) { // Return a map with (key2, key1) pairs
    for(Map.Entry<String, StringDoubleMap> e1 : maps.entrySet()) {
      String key1 = e1.getKey();
      StringDoubleMap map = e1.getValue();
      for(StringDoubleMap.Entry e2 : map) {
        String key2 = e2.getKey();
        double value = e2.getValue();
        newMap.put(key2, key1, value);
      }
    }
    return newMap;
  }

  public void lock() {
    for(StringDoubleMap map : maps.values())
      map.lock();
  }
  public void switchToSortedList() {
    for(StringDoubleMap map : maps.values())
      map.switchToSortedList();
  }
  public void switchToHashTable() {
    for(StringDoubleMap map : maps.values())
      map.switchToHashTable();
  }

  protected String2DoubleMap newMap() { return new String2DoubleMap(); }

  ////////////////////////////////////////////////////////////

  public StringDoubleMap getMap(String key1, boolean modify) {
    if(key1 == lastKey) return lastMap;

    StringDoubleMap map = maps.get(key1);
    if(map != null) return map;
    if(modify) {
      if(locked)
        throw new RuntimeException("Cannot make new entry for " + key1 + ", because map is locked");
      maps.put(key1, map = new StringDoubleMap());

      lastKey = key1;
      lastMap = map;
      return map;
    }
    else
      return null;
  }

  ////////////////////////////////////////////////////////////

  private boolean locked;
  private Map<String, StringDoubleMap> maps = new HashMap<String, StringDoubleMap>();
  private String lastKey; // Cache last access
  private StringDoubleMap lastMap; // Cache last access
}
