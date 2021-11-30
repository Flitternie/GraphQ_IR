package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * A view of executions based on a source file.
 * An exec view can contain specifications (the first one is used)
 * and other views.
 */
public class GroundedExecView extends ExecView {
  // Whether we have updated yet: hack for addToView in AllExecView
  protected boolean hasUpdated;

  public GroundedExecView(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(sourcePath);
  }

  protected boolean hasMutableMetadata() { return true; }

  protected FieldListMap getItemsFields() {
    // First try to use dynamic fields
    FieldListMap fields = getDynamicFieldListMap();
    if(fields != null) return fields;

    return super.getItemsFields();
  }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    super.update(spec, priority);
    updateChildren(spec, priority.next());
    spec.queue.enqueue(getAllExecView(), priority.next());
    hasUpdated = true;
  }

  // Return just the name (we assume it lives in AllExecView)
  protected String itemToHandle(Item item) throws MyException {
    if(item instanceof ExecItem)
      return item.name;
    return super.itemToHandle(item);
  }
  protected Item handleToItem(String handle) throws MyException {
    if(handle.indexOf('\t') == -1) // Singletons are treated as execution views
      return getAllExecView().getItem(handle);
    return super.handleToItem(handle);
  }
}
