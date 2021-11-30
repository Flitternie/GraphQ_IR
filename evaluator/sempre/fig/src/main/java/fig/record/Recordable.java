package fig.record;

/**
 * If an object is recordable, we can add it the static record.
 * record() should make calls to Record.add() and so on.
 */
public interface Recordable {
  public void record(Object arg);
}
