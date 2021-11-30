package fig.servlet;

import fig.basic.*;

/**
 * A view of arbitrary items, usually temporary.
 * For example, the clipboard is a basket.
 * FUTURE: have baskets be attached to a session and be stored just in memory.
 */
public class BasketItem extends Item {
  public BasketItem(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(sourcePath);
  }

  protected FieldListMap getMetadataFields() {
    return countMutableDescriptionFields;
  }
  protected FieldListMap getItemsFields() {
    return new FieldListMap(ListUtils.newList(trailField));
  }

  protected boolean namesAreIndices() { return true; }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    updateItemsFromFile(spec);
    updateChildren(spec, priority.next());
  }

  protected boolean isView() { return true; }
  protected Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}
