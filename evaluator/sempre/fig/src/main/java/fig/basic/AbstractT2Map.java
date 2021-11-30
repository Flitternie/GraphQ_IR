package fig.basic;

import fig.basic.*;
import static fig.basic.LogInfo.*;
import java.io.*;
import java.util.*;

/**
 * Just a dummy template right now.
 * TODO: move functionality in here.
 */
public abstract class AbstractT2Map<S extends Comparable<S>, T extends Comparable<T>> implements MemUsage.Instrumented {
  public abstract void switchToSortedList();
  public abstract void lock();
  public abstract int size();

  protected boolean locked;
  protected AbstractTMap.Functionality<T> keyFunc;

  public long getBytes() {
    return MemUsage.objectSize(MemUsage.booleanSize + MemUsage.pointerSize);
  }
}
