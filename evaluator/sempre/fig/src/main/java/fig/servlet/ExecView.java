package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * A view of executions.
 */
public abstract class ExecView extends Item {
  public ExecView(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
  }

  protected FieldListMap getMetadataFields() {
    FieldListMap fields = new FieldListMap();
    fields.add(countField);
    Field f;
    f = fields.add("description", "One-line description");
    if(hasMutableMetadata()) f.mutable = true;
    f = fields.add("note",        "Random comments");
    if(hasMutableMetadata()) { f.mutable = true; f.multiline = true; }
    return fields;
  }

  protected FieldListMap getItemsFields() {
    // Use the default field spec if possible
    DomainItem item = (DomainItem)findAncestorByClass(DomainItem.class);
    if(item != null) {
      Item fieldSpecItem = item.fieldSpecView.getItemEasy("default");
      if(fieldSpecItem != null)
        return ((FieldSpecItem)fieldSpecItem).createFieldListMap();
    }

    return ExecItem.createDefaultFields();
  }

  protected abstract boolean hasMutableMetadata();

  public UpdateQueue getPrioritizedItems(UpdateQueue.Priority priority) {
    // Put the ones that haven't been updated yet first
    UpdateQueue queue = new UpdateQueue();
    for(Item item : items.values()) {
      // Give higher priority to the ones that haven't updated yet
      // and the ones that are still running
      if(item instanceof ExecItem) {
        ExecItem execItem = (ExecItem)item;
        if(execItem.immutable) continue; // Don't update immutable items
        queue.enqueue(item,
          !execItem.hasUpdated || execItem.isRunning() ? priority : priority.next());
      }
      else
        queue.enqueue(item, priority);
    }
    return queue;
  }

  protected String tableType() { return "ExecView"; }
  protected boolean isView() { return true; }
  protected Item newItem(String name) throws MyException {
    return new ExecItem(this, name, new File(sourcePath, name).toString());
  }

  protected ExecViewDB getExecViewDB() { return (ExecViewDB)findAncestorByClass(ExecViewDB.class); }
  protected ExecView getAllExecView() { return getExecViewDB().allExecView; }
}
