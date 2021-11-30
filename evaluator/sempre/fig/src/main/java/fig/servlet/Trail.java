package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * A trail is like an absolute path on file systems.
 * It is used to identify an item.
 * There are several differences:
 *  - The items are ordered.
 *  - A view can many child items with the same name,
 *    so the trail must specify which one.
 */
public class Trail {
  public final String[] names;

  public Trail(String s) {
    this.names = StrUtils.split(s, "\t");
  }
  public Trail(List<String> s) {
    this.names = ListUtils.stringToArray(s);
  }

  public String toRepnString() {
    return StrUtils.join(names, "\t");
  }
  public String toDisplayString() {
    return StrUtils.join(names, " | ");
  }
}
