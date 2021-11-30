package fig.record;

import java.io.*;
import fig.basic.*;

public class LoadFileState {
  private GlobalEnv globalEnv; // For the file loading options

  // Not really an option, but needed when loading
  private ReceiverInterface receiver; // Used to output to while we're loading
  private OffsetReader lastReader; // Cache the last reader

  public LoadFileState(GlobalEnv globalEnv) {
    this.globalEnv = globalEnv;
  }

  public ReceiverInterface getReceiver() { return receiver; }

  // If we called getReader(), can we use the same file?
  public boolean alreadyOpened(File path) { return alreadyOpened(path.toString()); }
  public boolean alreadyOpened(String path) {
    return lastReader != null && lastReader.getPath().equals(path);
  }
  public OffsetReader getReader(File path, int offset) throws IOException {
    return getReader(path.toString(), offset);
  }
  public OffsetReader getReader(String path, int offset) throws IOException {
    if(alreadyOpened(path))
      lastReader.setOffset(offset);
    else
      lastReader = new OffsetReader(path, offset);
    return lastReader;
  }

  // When a command is executed, a local environment is created.
  // At the same time, the file state (which is globally shared across
  // all the path nodes) must update with respect to this temporary object.
  public void init(ReceiverInterface receiver) {
    this.receiver = receiver;
  }
  public void finish() {
    this.receiver = null;
    // Don't want to keep files open too long
    if(lastReader != null) { lastReader.closeEasy(); lastReader = null; }
  }

  public boolean verbose(int level) { return globalEnv.verbose(level); }
  public int getMaxLoadSize() { return globalEnv.getMaxLoadSize(); }
}
