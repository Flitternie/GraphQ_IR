package fig.servlet;

import java.io.*;
import java.util.*;

import fig.basic.*;
import fig.html.*;

public class ResponseElement implements ResponseObject {
  public ResponseElement(HtmlElement element) {
    this.element = element;
  }

  public void dump(WebState state) throws IOException {
    state.setHtmlOutput();
    state.getWriter().println(element.toString());
  }

  private HtmlElement element;
}
