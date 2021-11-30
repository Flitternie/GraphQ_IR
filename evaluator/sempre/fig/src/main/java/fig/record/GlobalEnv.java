package fig.record;

import fig.basic.*;
import java.util.*;

/**
 * An environment.
 * Stores variables which are used in substitution.
 * Stores the current node (like the current directory).
 */
public class GlobalEnv {
  private Map<String, String> varMap;
  private RecordNode rootRecord;
  private LoadFileState loadFileState;

  // Some environment variables
  private int maxResultNodes = Integer.MAX_VALUE;
  private int verboseLevel = 1;
  private int maxLoadSize = 100000; // Maximum size of subtree that we're willing to load at once
  private boolean cleanupMandate = true;

  public GlobalEnv(RecordNode rootRecord) {
    this.varMap = new HashMap<String, String>();
    this.loadFileState = new LoadFileState(this);
    this.rootRecord = rootRecord;
  }

  public RecordNode getRootRecord() { return rootRecord; }

  // Get and set environment variables
  public String getVar(String key) { return varMap.get(key); }
  public String getVar(String key, String defaultValue) { return MapUtils.get(varMap, key, defaultValue); }
  public int getVarInt(String key, int defaultValue) {
    return Utils.parseIntEasy(varMap.get(key), defaultValue);
  }
  public boolean getVarBoolean(String key, boolean defaultValue) {
    return Utils.parseBooleanEasy(varMap.get(key), defaultValue);
  }
  public void putVar(String key, String value) {
    putMap(varMap, key, value);
    setFromVars();
  }
  private static void putMap(Map<String, String> map, String key, String value) {
    if(value == null) map.remove(key); // Remove if null
    else map.put(key, value);
  }

  public void setFromVars() {
    maxResultNodes = getVarInt("maxResultNodes", maxResultNodes);
    verboseLevel = getVarInt("verbose", verboseLevel);
    cleanupMandate = getVarBoolean("cleanup", cleanupMandate);
    maxLoadSize = getVarInt("maxLoadSize", maxLoadSize);
  }
  public int getMaxResultNodes() { return maxResultNodes; }
  public boolean verbose(int level) { return level <= this.verboseLevel; }
  public boolean getCleanupMandate() { return cleanupMandate; }
  public int getMaxLoadSize() { return maxLoadSize; }

  public LoadFileState getLoadFileState() { return loadFileState; }
}
