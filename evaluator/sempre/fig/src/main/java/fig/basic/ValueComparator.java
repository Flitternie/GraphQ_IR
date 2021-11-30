package fig.basic;

import java.util.*;

public class ValueComparator<T, V extends Comparable<? super V>> implements Comparator< Map.Entry<T, V> > {
  public ValueComparator(boolean reverse) {
    this.sign = reverse ? -1 : 1;
  }

  public int compare(Map.Entry<T, V> e1, Map.Entry<T, V> e2) {
    V v1 = e1.getValue();
    V v2 = e2.getValue();
    return sign * v1.compareTo(v2);
  }

  int sign;
}
