package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * A filtered view executions, the executions that are in all.
 */
public abstract class FilteredExecView extends ExecView {
  public FilteredExecView(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
  }

  protected boolean hasMutableMetadata() { return false; }

  protected abstract String getDescription(); // OVERRIDE
  protected abstract void filterItems(OrderedMap<String,Item> newItems); // OVERRIDE

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    OrderedMap<String,Item> newItems = new OrderedMap<String,Item>();
    filterItems(newItems);
    items = newItems; // Fast switch!

    updateChildren(spec, priority.next());

    // Refresh this so we know which exec views are new,
    // but this is expensive because we have to scan the entire directory,
    // so it's not high priority.
    spec.queue.enqueue(getAllExecView(), priority.next());
  }

  protected Pair<String, Boolean> getDefaultSortSpec() {
    return new Pair<String,Boolean>("date", true);
  }
}
