package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * Specifies the columns of a table.
 * sourcePath: file containing the specification.
 * Each child is either FieldItems or FieldSpecItems.
 * FieldItems are created under specs (newItem),
 * but FieldSpecItems are added in (addItem).
 * 
 * When field items are added, they are copied rather than linked.
 */
public class FieldSpecItem extends Item {
  public FieldSpecItem(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(sourcePath);
  }
  public FieldSpecItem(Item parent, String name, String sourcePath, FieldListMap fields) {
    this(parent, name, null);
    addFields(fields);
  }

  public FieldListMap getMetadataFields() {
    FieldListMap fields = new FieldListMap();
    fields.add("count",       "Number of executions");
    fields.add("description", "One-line description").mutable = true;
    return fields;
  }
  public FieldListMap getItemsFields() {
    return new FieldItem(null, null).getMetadataFields();
  }

  // Populate fields with this specification.
  public void addToFieldListMap(FieldListMap fields) {
    for(Item item : items.values()) {
      if(item instanceof FieldItem)
        fields.add(((FieldItem)item).createField());
      else if(item instanceof FieldSpecItem)
        ((FieldSpecItem)item).addToFieldListMap(fields);
    }
  }
  public FieldListMap createFieldListMap() {
    FieldListMap fields = new FieldListMap();
    addToFieldListMap(fields);
    return fields.sort();
  }

  public void addFields(FieldListMap fields) {
    for(Field field : fields.values()) {
      FieldItem item = (FieldItem)newItem(field.name);
      item.setFromField(field);
      addItem(item);
    }
  }

  protected void addItem(Item item) {
    if(item instanceof FieldItem) { // Make a copy of field items
      Field field = ((FieldItem)item).createField();
      item = newItem(item.name);
      ((FieldItem)item).setFromField(field);
    }
    super.addItem(item);
  }

  protected boolean namesAreIndices() { return false; }
  protected boolean isView() { return true; }
  public Item newItem(String name) { return new FieldItem(this, name); }
}
