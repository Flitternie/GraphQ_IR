package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * A field item's metadata specifies the properties of the field.
 */
public class FieldItem extends Item {
  public FieldItem(Item parent, String name) {
    super(parent, name, null);
    metadataMap.put("numeric", "false");
  }

  public FieldListMap getMetadataFields() {
    FieldListMap fields = new FieldListMap();
    fields.add("displayName", "What is actually displayed").mutable = true;
    fields.add("gloss",       "Description of what the field is.").mutable = true;
    fields.add("data",        "Specifies how to populate the field, separated by spaces; use $ for intrinsic fields.").mutable = true;
    fields.add("numeric",     "Whether this is a numeric (for sorting)").mutable = true;
    fields.add("mutable",     "Whether we can edit this").mutable = true;
    fields.add("multiline",   "When editing, use multiple lines").mutable = true;
    fields.add("hidden",      "Whether to hide the field").mutable = true;
    fields.add("width",       "Width of the column").setMutable(true).numeric = true;
    fields.add("rank",        "Determines order of columns").setMutable(true).numeric = true;
    fields.add("process",     "How to process the value once we're done with it").mutable = true;
    return fields;
  }

  // Use the specified information to create a field.
  public Field createField() {
    if(metadataMap == null) return null;
    String displayName = metadataMap.get("displayName");
    String gloss = metadataMap.get("gloss");
    Object[] objs = ListUtils.toObjectArray(StrUtils.split(metadataMap.get("data")));
    Field field = FieldListMap.parseField(name, displayName, gloss, objs);
    field.numeric = Boolean.parseBoolean(metadataMap.get("numeric"));
    field.mutable = Boolean.parseBoolean(metadataMap.get("mutable"));
    field.multiline = Boolean.parseBoolean(metadataMap.get("multiline"));
    field.hidden = Boolean.parseBoolean(metadataMap.get("hidden"));
    field.width = Utils.parseIntEasy(metadataMap.get("width"), 0);
    field.rank = Utils.parseIntEasy(metadataMap.get("rank"), 1);
    field.processor = new ValueProcessor(metadataMap.get("process"));
    return field;
  }

  // Set information from the given field.
  public void setFromField(Field field) {
    metadataMap.put("displayName", field.displayName);
    metadataMap.put("gloss", field.gloss);
    metadataMap.put("data", field.toString());
    if(field.numeric) metadataMap.put("numeric", "true");
    if(field.mutable) metadataMap.put("mutable", "true");
    if(field.multiline) metadataMap.put("multiline", "true");
    if(field.hidden) metadataMap.put("hidden", "true");
    if(field.width > 0) metadataMap.put("width", ""+field.width);
    metadataMap.put("rank", ""+field.rank);
    if(field.processor != null && !field.processor.isIdentity())
      metadataMap.put("process", field.processor.toString());
  }

  protected boolean isView() { return false; }
  public Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}
