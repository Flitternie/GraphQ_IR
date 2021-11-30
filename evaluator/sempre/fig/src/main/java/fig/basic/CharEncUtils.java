package fig.basic;

import java.io.*;

public class CharEncUtils {
  //private static String charEncoding = "ISO-8859-1";
  private static String charEncoding = "UTF-8";

  public static String getCharEncoding() { return charEncoding; }

  public static void setCharEncoding(String charEncoding) {
    if(StrUtils.isEmpty(charEncoding)) return;
    CharEncUtils.charEncoding = charEncoding;
    LogInfo.updateStdStreams();
  }

  public static BufferedReader getReader(InputStream in) throws IOException {
    return new BufferedReader(new InputStreamReader(in, getCharEncoding()));
  }
  public static PrintWriter getWriter(OutputStream out) throws IOException {
    return new PrintWriter(new OutputStreamWriter(out, getCharEncoding()), true);
  }
}
