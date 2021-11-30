package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * A compound field simply concatenates a bunch of fields together
 * without spaces.
 */
public class CompoundField extends Field {
  private List<Field> fields;

  public CompoundField(String name, String displayName, String gloss,
      List<Field> fields) {
    super(name, displayName, gloss);
    this.fields = fields;
  }

  public Value getValue(Item item) throws MyException {
    // The value just becomes a string.
    StringBuilder buf = new StringBuilder();
    String cmpKey = null;
    for(Field field : fields) {
      Value value = field.getValue(item);
      buf.append(value.value == null ? "" : value.value);
      if(cmpKey == null) cmpKey = value.cmpKey;
    }
    return processValue(new Value(buf.toString(), cmpKey));
  }

  public String toString() { return StrUtils.join(fields); }
}
