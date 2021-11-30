package fig.basic;

import java.util.*;

public class SetUtils {
  // Return whether |set1| and |set2| have a non-empty intersection.
  public static <T> boolean intersects(Set<T> set1, Set<T> set2) {
    if (set1.size() > set2.size()) return intersects(set2, set1);
    for (T x : set1)
      if (set2.contains(x))
        return true;
    return false;
  }
}
