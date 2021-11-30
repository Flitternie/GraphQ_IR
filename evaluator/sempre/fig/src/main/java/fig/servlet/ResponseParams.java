package fig.servlet;

import java.io.*;
import java.util.*;

import fig.basic.*;

/**
 * Just a map from keys to values.
 */
public class ResponseParams extends OrderedStringMap implements ResponseObject {
  public ResponseParams() { }

  public ResponseParams(String msg) {
    this(true, msg);
  }

  public ResponseParams(boolean success, String msg) {
    setSuccess(success);
    if(msg != null) setMsg(msg);
  }

  public ResponseParams(boolean success, String goodMsg, String badMsg) {
    this(success, success ? goodMsg : badMsg);
  }

  public ResponseParams(MyException exception) {
    this(false, exception.getMessage());
    put("exception", true);
    int i = 0;
    for(StackTraceElement el : exception.getStackTrace()) {
      //if(el.getClassName().equals(javax.servlet.http.HttpServlet.class.getName()))
        //break;
      put("stackTrace" + (i++), el);
    }
  }

  public void put(String key, List<String> strings) {
    put(key, StrUtils.join(strings, "\t"));
  }

  // Standard fields
  public ResponseParams setSuccess(boolean success) {
    put("success", success);
    return this;
  }
  public ResponseParams setMsg(String msg) {
    put("msg", msg);
    return this;
  }
  public String getMsg() {
    return get("msg");
  }

  public void dump(WebState state) throws IOException {
    state.setPlainOutput();
    print(state.getWriter());
  }
}
