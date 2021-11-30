package fig.servlet;

import fig.basic.*;

/**
 * Contains a list of all the domains.
 * sourcePath = directory with all the domain files.
 */
public class DomainView extends Item {
  public DomainView(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    IOUtils.createNewDirIfNotExistsEasy(sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(fileSourcePath());
  }

  public FieldListMap getItemsFields() {
    return new DomainItem(null, null, null).getMetadataFields();
  }

  protected String fileSourcePath() { return null; } // Not loading from file
  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    updateItemsFromDir(-1, FileUtils.TraverseSpec.matchExt("index"), true);
    updateChildren(spec, priority.next());
  }

  protected String getDescription() {
    return "A domain contains all the information for a research project.";
  }

  protected boolean isView() { return true; }
  protected Item newItem(String name) throws MyException {
    return new DomainItem(this, name, childNameToIndexSourcePath(name));
  }
  protected Pair<String,Boolean> getDefaultSortSpec() { return new Pair("name", false); }
}
