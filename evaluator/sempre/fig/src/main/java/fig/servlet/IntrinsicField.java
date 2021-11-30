package fig.servlet;

import java.io.*;
import java.util.*;

/**
 * Intrinsic fields: contact item.
 */
public class IntrinsicField extends Field {
  public IntrinsicField(String name, String gloss) {
    this(name, name, gloss);
  }
  public IntrinsicField(String name, String displayName, String gloss) {
    super(name, displayName, gloss);
  }
  public Value getValue(Item item) throws MyException {
    return processValue(item.getIntrinsicFieldValue(name));
  }
  public void changeValue(Item item, String newValue) throws MyException {
    item.changeIntrinsicFieldValue(name, newValue);
  }

  public String toString() { return "$"+name; }
}
