package fig.servlet;

import java.io.*;
import java.util.*;

import fig.basic.*;

public class ResponseStream implements ResponseObject {
  public ResponseStream(InputStream rawData) {
    this.rawData = rawData;
  }

  public void dump(WebState state) throws IOException {
    IOUtils.copy(rawData, state.getOutputStream());
  }

  private InputStream rawData;
}
