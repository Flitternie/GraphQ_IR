package fig.record;

import java.io.*;
import java.util.*;

import fig.basic.*;
import fig.exec.*;
import fig.prob.*;
import fig.record.*;
import static fig.basic.LogInfo.*;

/**
 * Make one pass through a record file and print out
 * only the nodes that match.
 *
 * Doesn't support special directives like .struct, .array, .file.
 */
public class OnlineRecordFilter implements Runnable {
  @Option public static String inPath = "/dev/stdin";
  @Option public static String outPath = "/dev/stdout";
  @Option public ArrayList<String> filterPath = new ArrayList();
  @Option public int depth = Integer.MAX_VALUE;

  // Return whether filter matches the current line
  public boolean matches(String s, String key, String value) {
    String[] tokens = s.split("\t", 2);
    if(key != null && (tokens.length < 1 || !key.equals(tokens[0])))
      return false;
    if(value != null && (tokens.length < 2 || !value.equals(tokens[1])))
      return false;
    return true;
  }

  public void run() {
    // Preprocess filter keys and values
    List<String> filterKeys = new ArrayList();
    List<String> filterValues = new ArrayList();
    for(String filter : filterPath) {
      int i = filter.indexOf('=');
      String key = null, value = null;
           if(i == 0) value = filter;
      else if(i == -1) key = filter;
      else {
        key = filter.substring(0, i);
        value = filter.substring(i+1);
      }
      filterKeys.add(key);
      filterValues.add(value);
    }

    try {
      BufferedReader in = IOUtils.openIn(inPath);
      PrintWriter out = IOUtils.openOut(outPath);
      String line;
      int prevIndent = 0;
      int numMatch = 0; // Number of indent levels that stack matches filter
      while((line = in.readLine()) != null) {
        // Compute indent of this line
        int indent = 0;
        while(indent < line.length() && line.charAt(indent) == '\t')
          indent++;
        if(indent < numMatch) numMatch = indent;

        // Match up until now, try to extend match
        if(numMatch == indent && numMatch < filterPath.size()) {
          String key = filterKeys.get(numMatch);
          String value = filterValues.get(numMatch);
          if(matches(line.substring(indent), key, value))
            numMatch++;
        }
        // Print if match
        if(numMatch == filterPath.size() && indent-numMatch < depth)
          out.println(numMatch == 0 ? line : line.substring(numMatch-1)); 
      }
      in.close();
      out.close();
    } catch(IOException e) {
      throw new RuntimeException(e);
    }
  }

  public static void main(String[] args) {
    Execution.startMainTrack = false;
    Execution.run(args, new OnlineRecordFilter());
  }
}
