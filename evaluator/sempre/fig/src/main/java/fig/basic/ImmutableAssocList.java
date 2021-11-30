package fig.basic;

import java.util.*;

/**
 * An immutable single-linked list, which allows for sharing suffixes.
 */
public class ImmutableAssocList<K,V> {
  public K key;
  public V value;
  public ImmutableAssocList<K,V> next;
  private int size;

  private ImmutableAssocList(K key, V value, ImmutableAssocList<K,V> next, int size) {
    this.key = key;
    this.value = value;
    this.next = next;
    this.size = size;
  }

  public boolean isEmpty() { return this == emptyList; }

  public boolean containsKey(K x) {
    if (isEmpty()) return false;
    if (key.equals(x)) return true;
    return next.containsKey(x);
  }

  public V get(K x) {
    if (isEmpty()) return null;
    if (key.equals(x)) return value;
    return next.get(x);
  }

  public int size() { return size; }

  // Returns a list with |value| prepended to |this|.
  // Main operation to construct lists.
  public ImmutableAssocList<K,V> prepend(K key, V value) { return new ImmutableAssocList<K,V>(key, value, this, 1 + size); }

  // Create lists
  public static ImmutableAssocList emptyList = new ImmutableAssocList(null, null, null, 0);
  public static <K,V> ImmutableAssocList<K,V> singletonList(K key, V value) { return new ImmutableAssocList<K,V>(key, value, emptyList, 1); }
}
