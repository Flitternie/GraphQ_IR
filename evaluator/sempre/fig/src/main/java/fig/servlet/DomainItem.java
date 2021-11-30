package fig.servlet;

import java.io.*;
import java.util.*;
import java.net.*;
import fig.basic.*;

/**
 * A domain encompases one research project, and includes:
 *  - A single set of executions
 *  - A single set of specifications
 *
 * Example:
 * domainDir = /home/eecs/pliang/research/cortex/run/state
 */
public class DomainItem extends Item {
  public FieldSpecView fieldSpecView;
  public ExecViewDB execViewDB;
  // Keep track of the parameters used to create the children (views, etc.)
  // so if they change, we can recreate them
  private String domainDir;

  public DomainItem(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(sourcePath);
  }

  protected boolean isHidden() { return Boolean.parseBoolean(metadataMap.get("isHidden")); }
  public FieldListMap getItemsFields() { return countDescriptionFields; }

  protected void loadFromDisk() throws MyException {
    // Load the file so we can get the domain directory
    super.loadFromDisk();

    // Get new domain dir
    String newDomainDir = metadataMap.get("domainDir");
    if(!Utils.equals(newDomainDir, domainDir) &&
        (newDomainDir != null && new File(newDomainDir).isDirectory())) {
      this.domainDir = newDomainDir;
      ServletLogInfo.logs("New domainDir: " + domainDir);
      this.fieldSpecView = null; // Force reloading
      this.execViewDB = null; // Force reloading
    }

    // Create the views if they need to be created
    if(!StrUtils.isEmpty(domainDir)) {
      if(this.fieldSpecView == null)
        this.fieldSpecView = new FieldSpecView(this, "fieldSpecs",
            new File(domainDir, "fieldSpecs").toString());
      if(this.execViewDB == null)
        this.execViewDB = new ExecViewDB(this, "execs",
            new File(domainDir, "execs").toString(),
            new File(domainDir, "views").toString());
    }

    // If views exist, add them
    if(this.fieldSpecView != null) addItem(this.fieldSpecView);
    if(this.execViewDB != null)    addItem(this.execViewDB);
  }

  public FieldListMap getMetadataFields() {
    FieldListMap fields = new FieldListMap();
    fields.add(mutableDescriptionField);
    fields.add("domainDir",      "Domain directory").mutable = true;
    return fields;
  }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException { // OVERRIDE
    super.update(spec, priority);
    if(this.fieldSpecView != null)
      spec.queue.enqueue(this.fieldSpecView, priority); // We need field specs right away
    updateChildren(spec, priority.next());
  }

  protected Item handleToItem(String handle) throws MyException { return null; }
  protected String itemToHandle(Item item) throws MyException { return null; }

  protected boolean isView() { return true; }
  protected Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}
