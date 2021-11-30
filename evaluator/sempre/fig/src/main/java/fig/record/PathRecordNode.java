package fig.record;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * In general, load children lazily upon request.
 */
public abstract class PathRecordNode extends FullRecordNode {
  private File path; // Path relative to parent
  protected LoadFileState state; // Specifies how we should load children
  protected long lastLoadedTime; // When was this directory/file last loaded

  public PathRecordNode(LoadFileState state, String key, String value, File path) {
    super(key, value);
    this.state = state;
    this.path = path;
  }
  public PathRecordNode(LoadFileState state, File path) {
    super(path.getName(), null);
    this.state = state;
    this.path = path;
  }

  public File getPath() { return path; }

  // Need to override any operation that involves children
  // to first load the children if out of date
  public List<RecordNode> getChildren()           { if(outOfDate()) loadChildren(); return super.getChildren(); }
  public List<RecordNode> getChildren(String key) { if(outOfDate()) loadChildren(); return super.getChildren(key); }
  public int numChildren()                        { if(outOfDate()) loadChildren(); return super.numChildren(); }
  public int numChildren(String key)              { if(outOfDate()) loadChildren(); return super.numChildren(key); }

  public static PathRecordNode newPathNode(DirRecordNode parent, LoadFileState state, String name) {
    File file;
    if(parent == null) file = new File(name);
    else               file = new File(parent.getPath(), name);
    if(file.isDirectory()) return new DirRecordNode(state, file);
    if(file.isFile())      return new FileRecordNode(state, file);
    return null;
  }

  public void loadChildren() { // Should be overridden
    lastLoadedTime = new Date().getTime();
  }
  public void unloadChildren() {
    clearChildren();
    lastLoadedTime = 0;
  }
  public boolean isChildrenLoaded() { return lastLoadedTime > 0; }

  // Return true if the modified time is more recent than the last loaded time
  public boolean outOfDate() {
    return getPath().lastModified() > lastLoadedTime;
  }
  protected PathRecordNode disableLoading() {
    // Pretend last load time is in far future.
    // Useful for withoutChildren().
    lastLoadedTime = Long.MAX_VALUE;
    return this;
  }
}
