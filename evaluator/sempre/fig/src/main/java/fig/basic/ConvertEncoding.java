package fig.basic;

import fig.exec.*;
import static fig.basic.LogInfo.*;
import java.io.*;
import java.nio.charset.*;

public class ConvertEncoding {
  @Option(gloss="Input file", condReq="listEncodings=false")
    public static String inFile;
  @Option(gloss="Output file", condReq="listEncodings=false")
    public static String outFile;
  @Option(gloss="Input character encoding", condReq="listEncodings=false")
    public static String inEncoding;
  @Option(gloss="Output character encoding")
    public static String outEncoding = "UTF-8";
  @Option(gloss="List possible encodings")
    public static boolean listEncodings = false;
  @Option(gloss="Convert to lowercase")
    public static boolean lowercase = false;
  @Option(gloss="Convert to uppercase")
    public static boolean uppercase = false;
    
  public static void printCharsets() {
    for(Charset charset : Charset.availableCharsets().values())
      log(charset);
  }

  public static String aliasEncoding(String encoding) {
    encoding = encoding.toUpperCase();
    if(encoding.equals("GB")) return "GB2312";
    return encoding;
  }

  // Adapted from IOUtils to handle lowercasing and uppercasing
  // Return number of characters copied
  public static int copy(Reader in, Writer out) throws IOException {
    char[] buf = new char[16384];
    int total = 0, n;
    while((n = in.read(buf)) != -1) {
      if(uppercase)
        for(int i = 0; i < n; i++)
          buf[i] = Character.toUpperCase(buf[i]);
      if(lowercase)
        for(int i = 0; i < n; i++)
          buf[i] = Character.toLowerCase(buf[i]);
      total += n;
      out.write(buf, 0, n);
    }
    out.flush();
    return total;
  }

  public static void convertFile() throws IOException {
    inEncoding = aliasEncoding(inEncoding);
    outEncoding = aliasEncoding(outEncoding);

    logs("Copying %s (%s) => %s (%s)...", inFile, inEncoding, outFile, outEncoding);
    InputStreamReader in = new InputStreamReader(new FileInputStream(inFile), inEncoding);
    OutputStreamWriter out = new OutputStreamWriter(new FileOutputStream(outFile), outEncoding);
    int n = copy(in, out);
    if(n == -1) throw new RuntimeException("Failed to copy");
    logs("Wrote %d characters", n);
    in.close();
    out.close();
  }

  public static void main(String[] args) {
    Execution.init(args, "main", ConvertEncoding.class);
    try {
      if(listEncodings) printCharsets();
      else convertFile();
    } catch(Throwable t) {
      Execution.raiseException(t);
    }
    Execution.finish();
  }
}
