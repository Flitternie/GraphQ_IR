package fig.servlet;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import fig.basic.*;
import fig.html.*;

public class WebState {
  public WebState(HttpServletRequest request, HttpServletResponse response) throws IOException {
    this.request = request;
    this.response = response;
    this.session = request.getSession(true);
    this.params = new RequestParams(request);
    ServletLogInfo.verboseLogs("============================================================");
  }

  public OutputStream getOutputStream() throws IOException {
    return response.getOutputStream();
  }
  public PrintWriter getWriter() throws IOException {
    return response.getWriter();
  }

  // Set content-type.
  public void setRawOutput() {
  }
  public void setPlainOutput() {
    response.setContentType("text/plain; charset=" + CharEncUtils.getCharEncoding());
  }
  public void setHtmlOutput() {
    response.setContentType("text/html; charset=" + CharEncUtils.getCharEncoding());
  }

  // Input/output.
  public void initOutput() throws IOException {
    setHtmlOutput();
    this.out = getWriter();
  }
  public void endOutput() {
    out.close();
  }

  public PrintWriter out;  // Output to the response.
  public RequestParams params;
  public HttpServletRequest request;
  public HttpServletResponse response;
  public HttpSession session;
}
