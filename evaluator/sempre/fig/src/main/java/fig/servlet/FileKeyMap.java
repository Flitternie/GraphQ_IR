package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

// file:key -> value: load the information lazily
public class FileKeyMap {
  private Map<String,String> map;
  private String basePath; // Path of directory

  public FileKeyMap(String basePath) {
    this.basePath = basePath;
    this.map = new LinkedHashMap();
  }

  public void clear() { map.clear(); }

  public String get(String fileKey) {
    String[] tokens = fileKey.split(":", 2);
    if(tokens.length != 2) return null;
    return get(tokens[0], tokens[1]);
  }
  public String get(String file, String key) {
    String fileKey = file+":"+key;
    String value = map.get(fileKey);
    if(value == null) {
      try {
        // Load the file
        for(String line : IOUtils.readLines(new File(basePath, file).toString())) {
          String[] tokens = line.split("\t", 2);
          if(tokens.length == 0) continue;
          map.put(file+":"+tokens[0], tokens.length == 1 ? "" : tokens[1]);
        }
      } catch(IOException e) {
        // Ignore
      }
      value = map.get(fileKey);
    }
    return value;
  }

  // Write out the file
  // Minor note: the recent fields screws up the order
  public boolean put(String fileKey, String value) {
    String[] tokens = fileKey.split(":", 2);
    if(tokens.length != 2) return false;
    return put(tokens[0], tokens[1], value);
  }
  public boolean put(String file, String key, String value) {
    // Read the file first so as to not overwrite new fields
    get(file, key);
    map.put(file+":"+key, value);
    PrintWriter out = IOUtils.openOutEasy(new File(basePath, file));
    if(out == null) return false;
    for(Map.Entry<String,String> e : map.entrySet()) {
      String[] tokens = e.getKey().split(":", 2);
      if(tokens.length != 2) continue;
      if(!tokens[0].equals(file)) continue;
      out.println(tokens[1] + "\t" + e.getValue());
    }
    out.close();
    return true;
  }
}

