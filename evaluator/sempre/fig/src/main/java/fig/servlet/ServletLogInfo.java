package fig.servlet;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import fig.basic.*;

/**
 * A global class which logs to using a servlet.
 * Usage: in HttpServlet, call setServlet() and use logs() as usual.
 */
public class ServletLogInfo {
  public static void setServlet(HttpServlet servlet) {
    ServletLogInfo.servlet = servlet;
  }
  public synchronized static void logs(Object arg) {
    if(!loadedNew) {
      servlet.log("NEWLY LOADED JVM");
      loadedNew = true;
    }
    servlet.log("" + arg);
  }
  public synchronized static void logs(String format, Object... args) {
    logs(String.format(format, args));
  }
  public synchronized static void verboseLogs(Object o) {
    if(verbose) logs(o);
  }
  public synchronized static void verboseLogs(String format, Object... args) {
    if(verbose) logs(format, args);
  }

  // Hack: using static variables so we can refer to these from anywhere
  private static HttpServlet servlet;
  private static boolean loadedNew;
  public static boolean verbose, logUpdates;
}
