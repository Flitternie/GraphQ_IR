package fig.servlet;

public class MyException extends Exception {
  private static final long serialVersionUID = 42;
  public MyException() { }
  public MyException(String msg) { super(msg); }
}
