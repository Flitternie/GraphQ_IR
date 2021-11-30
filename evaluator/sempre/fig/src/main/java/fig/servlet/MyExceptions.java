package fig.servlet;

import java.io.*;

class NameNotFoundException extends MyException {
  public final Item item;
  public final String name;

  public NameNotFoundException(Item item, String name) {
    super("No child named " + name + " from " + item.getTrail().toDisplayString());
    this.item = item;
    this.name = name;
  }
}

public class MyExceptions {
  public static MyException unsupported =
    new MyException("Operation not supported");
  public static MyException unsupported(String op, Object x) {
    return new MyException("Operation " + op + " not supported for " + x);
  }

  public static MyException TODO() {
    return new MyException("I will fix this later");
  }

  /*public static MyException wrongType(Object o, Class c) {
    return new MyException("Invalid type: wanted type " + c + ", but got " + o + " with type " +
        (o == null ? null : o.getClass()));
  }*/

  /*public static <T> T cast(Object o, Class<T> c) throws MyException {
    try {
      return c.cast(o);
    } catch(ClassCastException e) {
      throw new MyException("Invalid type: wanted type " + c + ", but got " + o + " with type " +
          (o == null ? null : o.getClass()));
    }
  }*/
}
