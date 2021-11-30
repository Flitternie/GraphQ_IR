package fig.servlet;

import fig.basic.*;
import java.util.*;
import java.text.*;
import java.io.*;

/**
 * Substitutes the value of a field based on some replacements.
 */
public class ValueProcessor {
  static interface Processor {
    public String process(String s);
  }
  static class ReplaceProcessor implements Processor {
    private final String a, b;
    private final boolean global;
    public ReplaceProcessor(String a, String b, boolean global) {
      this.a = a; this.b = b;
      this.global = global;
    }
    public String process(String s) {
      if(s == null) return null;
      if(global) return s.replaceAll(a, b);
      else return s.replaceFirst(a, b);
    }
    public String toString() { return String.format("s/%s/%s/%s", a, b, global?"g":""); }
  }
  static class TruncateStringFormatProcessor implements Processor {
    public TruncateStringFormatProcessor(int max) { this.max = max; }
    public String process(String s) {
      if (s.length() <= max) return s;
      return "<a title=\""+s+"\">"+s.substring(0, max)+"...</a>";
    }
    public String toString() { return "TRUNCATE:"+max; }
    private int max;
  }
  static class DoubleFormatProcessor implements Processor {
    public DoubleFormatProcessor(int max) { this.max = max; }
    public String process(String s) {
      String[] tokens = s.split(";");
      List<String> newTokens = new ArrayList<String>();
      for (String token : tokens) {
        double x = Utils.parseDoubleEasy(token);
        if(Double.isNaN(x)) newTokens.add(token);
        else if (max == 0) newTokens.add(Math.round(x)+"");
        else newTokens.add(NumUtils.round(x, max)+"");
      }
      return StrUtils.join(newTokens, ";");
    }
    public String toString() { return "DOUBLE:"+max; }
    private int max;
  }
  static class DateFormatProcessor implements Processor {
    private static final DateFormat standardDateFormat =
          new SimpleDateFormat("EEE MMM dd kk:mm:ss zzz yyyy");

    public String process(String s) {
      try {
        Date d = standardDateFormat.parse(s);
        return Fmt.formatEasyDateTime(d.getTime());
      } catch(ParseException e) {
        return s;
      }
    }
    public String toString() { return "DATE"; }
  }
  static class BytesFormatProcessor implements Processor {
    public String process(String s) {
      try {
        return Fmt.bytesToString(Long.parseLong(s));
      } catch(NumberFormatException e) {
        return s;
      }
    }
  }


  private List<Processor> processors;

  // s is either STRING:<value> or STRING
  private int getInt(String s, int defaultValue) {
    int i = s.indexOf(':');
    if (i == -1) return defaultValue;
    return Integer.parseInt(s.substring(i+1));
  }

  // Tabs separate 
  // Format: s/true/EM\ts/false/var
  public ValueProcessor(String description) {
    this.processors = new ArrayList();
    if(description == null) return;
    for(String subStr : StrUtils.split(description, "\t")) {
      if(subStr.startsWith("DOUBLE"))
        processors.add(new DoubleFormatProcessor(getInt(subStr, 3)));
      else if(subStr.startsWith("TRUNCATE:"))
        processors.add(new TruncateStringFormatProcessor(getInt(subStr, 10)));
      else if(subStr.equals("DATE"))
        processors.add(new DateFormatProcessor());
      else if(subStr.equals("BYTES"))
        processors.add(new BytesFormatProcessor());
      else {
        // Replace: s/a/b/g
        subStr = subStr.replaceAll("\\\\/", "__SLASH__"); // Don't break on escaped slashes
        String[] tokens = StrUtils.split(subStr, "/");
        for (int i = 0; i < tokens.length; i++)
          tokens[i] = tokens[i].replaceAll("__SLASH__", "/");
        if(tokens.length == 0 || !tokens[0].equals("s")) continue;
        if(tokens.length == 2) tokens = new String[] {tokens[0], tokens[1], "", ""};
        if(tokens.length == 3) tokens = new String[] {tokens[0], tokens[1], tokens[2], ""};
        if(tokens.length != 4) continue;
        processors.add(new ReplaceProcessor(tokens[1], tokens[2], tokens[3].equals("g")));
      }
    }
  }

  public String process(String s) {
    if(s == null) return null;
    for(Processor processor : processors)
      s = processor.process(s);
    return s;
  }

  public boolean isIdentity() { return processors.size() == 0; }
  public String toString() { return StrUtils.join(processors, "\t"); }
}
