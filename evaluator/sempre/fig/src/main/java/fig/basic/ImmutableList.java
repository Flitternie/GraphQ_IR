package fig.basic;

import java.util.*;

/**
 * An immutable single-linked list, which allows for sharing suffixes.
 */
public class ImmutableList<T> {
  public T value;
  public ImmutableList<T> next;
  private int size;

  private ImmutableList(T value, ImmutableList<T> next, int size) {
    this.value = value;
    this.next = next;
    this.size = size;
  }

  public boolean isEmpty() { return this == emptyList; }

  public boolean contains(T x) {
    if (isEmpty()) return false;
    if (value.equals(x)) return true;
    return next.contains(x);
  }

  public int size() { return size; }

  // Returns a list with |value| prepended to |this|.
  // Main operation to construct lists.
  public ImmutableList<T> prepend(T value) { return new ImmutableList(value, this, 1 + size); }

  // Create lists
  public static ImmutableList emptyList = new ImmutableList(null, null, 0);
  public static <T> ImmutableList<T> singletonList(T value) { return new ImmutableList<T>(value, emptyList, 1); }

  @Override public String toString() { return toString(" "); }
  public String toString(String delim) {
    StringBuilder buf = new StringBuilder();
    for(ImmutableList<T> it = this; it != emptyList; it = it.next) {
      if (buf.length() > 0) buf.append(delim);
      buf.append(it.value);
    }
    return buf.toString();
  }
}
