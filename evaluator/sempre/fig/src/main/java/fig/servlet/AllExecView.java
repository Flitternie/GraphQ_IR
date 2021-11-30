package fig.servlet;

import java.io.*;
import fig.basic.*;

/**
 * A view of all executions.
 */
public class AllExecView extends ExecView {
  public AllExecView(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
  }

  protected Value getIntrinsicFieldValue(String fieldName) throws MyException {
    if(fieldName.equals("description")) return new Value("All executions");
    return super.getIntrinsicFieldValue(fieldName);
  }

  protected boolean hasMutableMetadata() { return false; }

  protected String fileSourcePath() { return null; }
  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    // Only consider directories that end with .exec
    // Don't descend into anything that contains .exec (e.g., *.exec.purged* directories)
    FileUtils.TraverseSpec tspec = new FileUtils.TraverseSpec(
      new FilenameFilterBank.Compose(new FilenameFilterBank.Regex(".*\\.exec", true), FilenameFilterBank.onlyDir()),
      new FilenameFilterBank.Compose(new FilenameFilterBank.Regex(".*\\.exec.*", false), FilenameFilterBank.onlyDir()));
    updateItemsFromDir(-1, tspec, false);

    // - For the exec items with an addToView file (one view per line)
    // add the exec item to that view
    // - Also, add to ready views if auto queuing is on
    ExecViewDB execViewDB = getExecViewDB();
    for(Item _item : items.values()) {
      if(!(_item instanceof ExecItem)) continue; // Shouldn't happen
      ExecItem item = (ExecItem)_item;

      // See if there is a addToView file, and try getting the view
      // Create it if it doesn't exist
      File path = new File(item.sourcePath, "addToView");
      for(String viewName : IOUtils.readLinesEasy(path.toString())) {
        // Creating new views doesn't quite work
        boolean isNew = execViewDB.getItemEasy(viewName) == null;
        GroundedExecView view = (GroundedExecView)execViewDB.getItemOrNewAdd(viewName); // Get the view
        if (isNew && execViewDB.hasUpdated) {
          ServletLogInfo.logs("Creating new view %s", view);
          execViewDB.saveToDisk();
        }

        // Important!  Only call if we have already loaded
        // the view, otherwise we're going to overwrite the file,
        // which would be very bad.
        if(view.hasUpdated && !view.containsItem(item)) {
          ServletLogInfo.logs("Adding %s to view %s", item, view);
          view.addItem(item); // Add it to that view
          view.saveToDisk();
          path.delete(); // Delete the file once we've added
        }
      }
    }

    updateChildren(spec, priority.next());
  }

  protected Pair<String,Boolean> getDefaultSortSpec() {
    return new Pair<String,Boolean>("date", true);
  }
}
