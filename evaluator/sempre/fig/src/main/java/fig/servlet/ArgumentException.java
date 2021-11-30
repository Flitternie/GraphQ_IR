package fig.servlet;

import java.io.*;

public class ArgumentException extends MyException {
  private static final long serialVersionUID = 42;
  public ArgumentException(String msg) { super(msg); }
  public static ArgumentException missing(String key) { return new ArgumentException("Missing " + key); }
}
