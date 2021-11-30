package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * A field is a function mapping 
 * Mapping names to field lists.
 */
public class FieldListMap extends OrderedMap<String,Field> {
  public FieldListMap() { }
  public FieldListMap(List<Field> fields) {
    for(Field field : fields) add(field);
  }

  public Field add(Field field) {
    String name = field.name;
    if(name.equals("name"))
      throw new RuntimeException("Reserved field name: " + name);
    if(containsKey(field.name))
      throw new RuntimeException("Duplicate field name: " + name);
    put(name, field);
    return field;
  }

  public Field add(String name, String gloss) {
    return add(name, name, gloss);
  }
  public Field add(String name, String displayName, String gloss) {
    return add(name, displayName, gloss, new Object[0]);
  }
  public Field add(String name, String gloss, Object[] objs) {
    return add(parseField(name, name, gloss, objs));
  }
  public Field add(String name, String displayName, String gloss, Object[] objs) {
    return add(parseField(name, displayName, gloss, objs));
  }

  public static Field parseField(String name, String displayName, String gloss, Object[] objs) {
    Field field;
    if(objs.length == 0)
      field = new IntrinsicField(name, displayName, gloss);
    else if(objs.length == 1)
      field = objToField(name, displayName, gloss, objs[0]);
    else {
      List<Field> fields = new ArrayList<Field>();
      for(Object obj : objs) fields.add(objToField(null, null, null, obj));
      field = new CompoundField(name, displayName, gloss, fields);
    }
    return field;
  }

  private static Field objToField(String name, String displayName, String gloss, Object obj) {
    if(obj instanceof String) { // String is either a simple field or just a constant
      String s = (String)obj;
      if(s.startsWith("$"))
        return new IntrinsicField(s.substring(1), displayName, gloss);
      else
        return new ConstantField(name, displayName, gloss, obj);
    }
    else if(obj instanceof Field)
      return (Field)obj;
    else
      return new ConstantField(name, displayName, gloss, obj);
  }

  // Sort the fields by their rank
  public FieldListMap sort() {
    FieldListMap map = new FieldListMap();
    List<Field> fields = new ArrayList();
    for(Field field : values()) fields.add(field);
    Collections.sort(fields);
    for(Field field : fields) map.add(field);
    return map;
  }
}
