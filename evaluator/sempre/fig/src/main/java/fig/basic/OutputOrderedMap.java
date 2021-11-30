package fig.basic;

import java.io.*;
import java.util.*;

/**
 * Keeps
 */
public class OutputOrderedMap<S, T> extends OrderedMap<S, T> {
  private PrintWriter out;

  // Print the items to a file as we add them to the map.
  public OutputOrderedMap(String path) {
    this.out = IOUtils.openOutEasy(path);
  }
  public OutputOrderedMap(File path) {
    this.out = IOUtils.openOutEasy(path);
  }

  public void put(S key, T val) {
    super.put(key, val);

    // Write to disk as we go
    if(out != null) {
      print(out, key, val);
      out.flush();
    }
  }
}
