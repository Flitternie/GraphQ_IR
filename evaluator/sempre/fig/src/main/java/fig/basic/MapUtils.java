package fig.basic;

import java.io.*;
import java.util.*;

public class MapUtils {
  // One-level hash maps
  public static <S, T> boolean contains(Map<S, T> map, S key) {
    return map != null && map.containsKey(key);
  }
  public static <S, T> T get(Map<S, T> map, S key, T defaultVal) {
    if (map == null) return defaultVal;
    T val = map.get(key);
    if (val == null) return defaultVal;
    return val;
  }
  public static <S, T> T getMut(Map<S, T> map, S key, T defaultVal) {
    if(!map.containsKey(key)) {
      map.put(key, defaultVal); // Mutate
      return defaultVal;
    }
    return map.get(key);
  }
  public static <S,T> boolean putIfAbsent(Map<S,T> map, S key, T val) {
    if (map.containsKey(key)) return false;
    map.put(key, val);
    return true;
  }
  public static <S, T> void set(Map<S, T> map, S key, T val) {
    map.put(key, val);
  }
  public static <S> void incr(Map<S, Integer> map, S key, int dVal) {
    if(!map.containsKey(key)) map.put(key, dVal);
    else map.put(key, map.get(key) + dVal);
  }
  public static <S> void incr(Map<S, Integer> map, S key) {
    incr(map, key, 1);
  }
  public static <S> void incr(Map<S, Double> map, S key, double dVal) {
    Double val = map.get(key);
    if (val == null) map.put(key, dVal);
    else map.put(key, val + dVal);
  }

  public static <S, T> void print(Map<S, T> map, PrintWriter out) {
    for (Map.Entry<S, T> e : map.entrySet())
      out.println(e.getKey() + "\t" + e.getValue());
  }
  public static <S, T> void printEasy(Map<S, T> map, String path) {
    PrintWriter out = IOUtils.openOutEasy(path);
    if (out == null) return;
    print(map, out);
    out.close();
  }
  public static <S, T> void printHard(Map<S, T> map, String path) {
    PrintWriter out = IOUtils.openOutHard(path);
    print(map, out);
    out.close();
  }

  // Two-level hash maps
  public static <S, T, U> boolean contains(Map<S, Map<T, U>> map, S key1, T key2) {
    if(map == null) return false;
    Map<T, U> m = map.get(key1);
    return m != null && m.containsKey(key2);
  }
  public static <S, T, U> U get(Map<S, Map<T, U>> map, S key1, T key2, U defaultVal) {
    if(map == null || !map.containsKey(key1)) return defaultVal;
    Map<T, U> m = map.get(key1);
    return m == null || !m.containsKey(key2) ? defaultVal : m.get(key2);
  }
  public static <S, T, U> U getMut(Map<S, Map<T, U>> map, S key1, T key2, U defaultVal) {
    Map<T, U> m = map.get(key1);
    if(m == null) {
      map.put(key1, m = new HashMap<T, U>());
      m.put(key2, defaultVal);
      return defaultVal;
    }
    else if(!m.containsKey(key2)) {
      m.put(key2, defaultVal);
      return defaultVal;
    }
    return m.get(key2);
  }
  public static <S, T> void add(Map<S, Set<T>> map, S key1, T key2) {
    Set<T> s = map.get(key1);
    if(s == null) map.put(key1, s = new HashSet<T>());
    s.add(key2);
  }
  public static <S, T, U> void set(Map<S, Map<T, U>> map, S key1, T key2, U val) {
    Map<T, U> m = map.get(key1);
    if(m == null) map.put(key1, m = new HashMap<T, U>());
    m.put(key2, val);
  }
  public static <S, T> void incr(Map<S, Map<T, Integer>> map, S key1, T key2, int dVal) {
    Map<T, Integer> m = map.get(key1);
    if(m == null) {
      map.put(key1, m = new HashMap<T, Integer>());
      m.put(key2, dVal);
    }
    else if(!m.containsKey(key2))
      m.put(key2, dVal);
    else
      m.put(key2, m.get(key2) + dVal);
  }
  public static <S, T> void incr(Map<S, Map<T, Integer>> map, S key1, T key2) {
    incr(map, key1, key2, 1);
  }
  public static <S, T> void incr(Map<S, Map<T, Double>> map, S key1, T key2, double dVal) {
    Map<T, Double> m = map.get(key1);
    if(m == null) {
      map.put(key1, m = new HashMap<T, Double>());
      m.put(key2, dVal);
    }
    else if(!m.containsKey(key2))
      m.put(key2, dVal);
    else
      m.put(key2, m.get(key2) + dVal);
  }

  // Create a list if it doesn't exist
  public static <S, T> List<T> getListMut(Map<S, List<T>> map, S key) {
    List<T> list = map.get(key);
    if(list == null)
      map.put(key, list = new ArrayList());
    return list; 
  }

  // Hard operations
  // Wrapper for operations on maps and sets
  public static <S, T> T getHard(Map<S, T> map, S key) {
    T value = map.get(key);
    if(value == null) throw new RuntimeException("Doesn't contain key: " + key);
    return value;
  }
  public static <S, T> void putHard(Map<S, T> map, S key, T value) {
    if(map.containsKey(key)) throw new RuntimeException("Already contains key; " + key);
    map.put(key, value);
  }
  public static <S, T> T removeHard(Map<S, T> map, S key) {
    T value = map.remove(key);
    if(value == null) throw new RuntimeException("Doesn't contain key");
    return value;
  }
  public static <S> void addHard(Set<S> set, S key) {
    if(set.contains(key)) throw new RuntimeException("Already contains key");
    set.add(key);
  }
  public static <S> void removeHard(Set<S> set, S key) {
    if(!set.remove(key)) throw new RuntimeException("Doesn't contain key");
  }


  public static <S,T> void addToList(Map<S, List<T>> map, S s, T t) {
    List<T> list = map.get(s);
    if (list == null) map.put(s, list = new ArrayList<T>());
    list.add(t);
  }

  public static <S,T> void addToSet(Map<S, Set<T>> map, S s, T t) {
    Set<T> set = map.get(s);
    if (set == null) map.put(s, set = new HashSet<T>());
    set.add(t);
  }

  public static <S,T> void removeFromSet(Map<S, Set<T>> map, S s, T t) {
    Set<T> set = map.get(s);
    if (set != null) set.remove(t);
  }

  public static <S,T> List<T> getList(Map<S, List<T>> map, S s) {
    List<T> list = map.get(s);
    return list == null ? Collections.EMPTY_LIST : list;
  }

  public static <S,T> Set<T> getSet(Map<S, Set<T>> map, S s) {
    Set<T> set = map.get(s);
    return set == null ? Collections.EMPTY_SET : set;
  }

  public static <S> double getDouble(Map<S, Double> map, S s, double defaultValue) {
    Double t = map.get(s);
    return t == null ? defaultValue : t;
  }

  // Print out the top k values a hash table sorted by descending value
  // Should only take O(k \log n) time,
  // but right now the implementation is slow
  public static <T> PriorityQueue<T> toPriorityQueue(Map<T, Double> map) {
    PriorityQueue<T> pq = new PriorityQueue<T>();
    for(Map.Entry<T, Double> e : map.entrySet())
      pq.add(e.getKey(), e.getValue());
    return pq;
  }
  public static <T> PriorityQueue<T> toPriorityQueue(TDoubleMap<T> map) {
    PriorityQueue<T> pq = new PriorityQueue<T>();
    for(TDoubleMap<T>.Entry e : map)
      pq.add(e.getKey(), e.getValue());
    return pq;
  }
  public static <T> String topNToString(TDoubleMap<T> map, int numTop) {
    return topNToString(toPriorityQueue(map), numTop);
  }
  public static <T> String topNToString(Map<T, Double> map, int numTop) {
    return topNToString(toPriorityQueue(map), numTop);
  }
  public static <T> String topNToString(PriorityQueue<T> pq, int numTop) {
    StringBuilder sb = new StringBuilder();
    sb.append('{');
    for(Pair<T, Double> pair : getTopN(pq, numTop)) {
      Object key = pair.getFirst();
      double value = pair.getSecond();
      sb.append(' ');
      sb.append(key);
      sb.append(':');
      sb.append(Fmt.D(value));
    }
    if(pq.size() > numTop)
      sb.append(" ...("+(pq.size()-numTop)+ " more)");
    sb.append(" }");
    return sb.toString();
  }
  // Return a list of the top n elements in the following structures
  public static <T> List<Pair<T, Double>> getTopN(Map<T, Double> map, int n) {
    return getTopN(toPriorityQueue(map), n);
  }
  public static <T> List<Pair<T, Double>> getTopN(TDoubleMap<T> map, int n) {
    return getTopN(toPriorityQueue(map), n);
  }
  public static <T> List<Pair<T, Double>> getTopN(PriorityQueue<T> pq, int n) {
    List<Pair<T, Double>> list = new ArrayList<Pair<T, Double>>();
    for(int i = 0; i < n && pq.hasNext(); i++) {
      double priority = pq.getPriority();
      T element = pq.next();
      list.add(new Pair<T, Double>(element, priority));
    }
		return list;
  }
  
  public static <K,M,V> Map<K,V> compose(Map<K,M> m1, Map<M,V> m2, Map<K,V> mapToFill) {    
    for (Map.Entry<K,M> entry: m1.entrySet()) {
      V val = m2.get(entry.getValue());
      if (val != null)
          mapToFill.put(entry.getKey(), val);
    }
    return mapToFill;
  }
}
