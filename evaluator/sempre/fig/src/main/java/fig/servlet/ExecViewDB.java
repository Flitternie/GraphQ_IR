package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * Contains two default execution views: all and orphaned.
 */
public class ExecViewDB extends Item {
  // Whether we have updated yet: hack for addToView in AllExecView
  protected boolean hasUpdated;

  public final AllExecView allExecView;
  public final FilteredExecView orphanedExecView;
  public final FilteredExecView runningExecView;

  public ExecViewDB(Item parent, String name, String execsPath, String viewsPath) {
    super(parent, name, viewsPath);
    IOUtils.createNewDirIfNotExistsEasy(sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(fileSourcePath());

    addItem(this.allExecView = new AllExecView(this, "(all)", execsPath));
    addItem(this.orphanedExecView = new FilteredExecView(this, "(orphaned)", execsPath) {
      protected String getDescription() { return "Orphaned executions: those not in any execution view"; }
      protected void filterItems(OrderedMap<String,Item> newItems) {
        ExecViewDB execViewDB = getExecViewDB();
        ExecView allExecView = execViewDB.allExecView;

        // Find items that are in some GroundedExecView
        Set<Item> hitItems = new HashSet<Item>();
        for(Item execView : execViewDB.items.values())
          if(execView instanceof GroundedExecView)
            for(Item item : execView.items.values())
              hitItems.add(item);
        
        // Add the exec items that are not hit
        // Unless it contains an addToView file, in which case we add it to
        // the corresponding view and delete the file
        for(Item item : allExecView.items.values()) {
          // Add items that are not contained in any view
          if(!hitItems.contains(item))
            addItem(newItems, item);
        }
      }
    });

    addItem(this.runningExecView =
      new SimpleFilteredExecView(this, "(running)", "Running executions") {
        protected boolean accept(ExecItem item) { return item.isRunning(); }
    });
  }

  public FieldListMap getItemsFields() {
    return new GroundedExecView(null, null, null).getMetadataFields();
  }

  protected String getDescription() {
    return "Executions are the experiments.";
  }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    updateItemsFromFile(spec,
        ListUtils.newList(allExecView),
        ListUtils.newList(orphanedExecView, runningExecView));
    updateChildren(spec, priority.next());
    hasUpdated = true;
  }

  protected boolean isView() { return true; }
  protected Item newItem(String name) {
    return new GroundedExecView(this, name, childNameToIndexSourcePath(name));
  }
  protected String itemToHandle(Item item) throws MyException {
    if(item == allExecView ||
       item == orphanedExecView ||
       item == runningExecView)
      return null;
    return super.itemToHandle(item);
  }
}
