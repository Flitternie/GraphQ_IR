package fig.servlet;

import fig.basic.*;

/**
 * Note that a divider's description is not saved until its parent is saved.
 */
public class DividerItem extends Item {
  public static final String dividerStr = "<hr color=\"darkblue\">";
  public String description;

  public DividerItem(Item parent, String name, String description) {
    super(parent, name, null);
    this.description = description;
  }

  protected Value getIntrinsicFieldValue(String fieldName) throws MyException {
    return new Value(description);
  }
  protected void changeIntrinsicFieldValue(String fieldName, String value) throws MyException {
    description = value;
  }

  protected FieldListMap getMetadataFields() {
    return new FieldListMap(ListUtils.newList(mutableDescriptionField));
  }

  protected boolean isView() { return false; }
  protected Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}
