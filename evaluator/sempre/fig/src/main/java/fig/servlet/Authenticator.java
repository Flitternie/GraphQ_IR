package fig.servlet;

import java.io.*;
import javax.servlet.http.*;

public class Authenticator {
  private RootItem rootItem;

  public Authenticator(RootItem rootItem) {
    this.rootItem = rootItem;
  }

  private Cookie getAuthCookie() {
    return new Cookie("word", "bleu");
  }

  // Get permissions: check the sent cookie
  public Permissions getPermissions(HttpServletRequest request) {
    return new Permissions(true, new File("/")); // Allow everything

    /*Cookie gold = getAuthCookie();
    Cookie[] cookies = request.getCookies();
    if(cookies != null) {
      for(Cookie c : cookies) {
        WebState.verboseLogs("Got cookie (" + c.getName() + ", " + c.getValue() + ")");
        if(c.getName().equals(gold.getName()) && c.getValue().equals(gold.getValue()))
          return new Permissions(true, new File("/")); // Allow everything
      }
    }*/
    //return new Permissions(false, null); // No access
    //return new Permissions(false, rootView.getExecViewDB().getExecsDir()); // Allow only access to execs
  }

  // Give permissions: send a cookie
  public boolean givePermissions(String value, HttpServletResponse response) {
    if(getAuthCookie().getValue().equals(value)) {
      response.addCookie(getAuthCookie());
      return true;
    }
    return false;
  }
}
