package fig.servlet;

import java.io.*;
import java.util.*;

/**
 * A field is a function mapping items to values.
 * Corresponds to a column in a table.
 *
 * Derived fields should call processValue.
 */
public abstract class Field implements Comparable {
  public String name; // The actual name (must be unique)
  public String displayName; // A (short) name that is displayed
  public String gloss; // A description
  public boolean numeric, mutable, multiline; // Formatting
  public boolean hidden;
  public int width; // Column width
  public int rank; // Smaller ranks are displayed first
  public ValueProcessor processor; // What to do with the value after

  public Field(String name, String displayName, String gloss) {
    this.name = name;
    this.displayName = displayName;
    this.gloss = gloss;
  }

  public abstract Value getValue(Item item) throws MyException;

  public void changeValue(Item item, String newValue) throws MyException {
    throw MyExceptions.unsupported("changeValue", "field " + name);
  }

  public Value processValue(Value value) {
    return processor == null ? value :
      new Value(processor.process(value.value), value.cmpKey);
  }

  public Field setMutable(boolean mutable) { this.mutable = mutable; return this; }
  public Field setNumeric(boolean numeric) { this.numeric = numeric; return this; }

  public int compareTo(Object o) {
    Field f = (Field)o;
    if(this.rank < f.rank) return -1;
    if(this.rank > f.rank) return +1;
    return 0;
  }
}
