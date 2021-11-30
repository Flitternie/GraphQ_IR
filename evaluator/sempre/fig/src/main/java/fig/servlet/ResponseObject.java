package fig.servlet;

import java.io.*;
import java.util.*;

import fig.basic.*;

public interface ResponseObject {
  public void dump(WebState state) throws IOException;
}
