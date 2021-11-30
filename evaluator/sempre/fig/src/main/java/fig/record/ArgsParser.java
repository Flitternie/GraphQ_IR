package fig.record;

import java.util.*;
import fig.basic.*;

/**
 * Parses the arguments of a function.
 * Usage:
 * Create an instance with args, the list of arguments that are passed to the
 * function.  Optionally, if these arguments are named (of the form var=val),
 * then we call setNames().  This creates prevalues, which correspond to the
 * names, but might contain unsubstituted values.
 */
public class ArgsParser {
  private char varEscapeChar; // Escape character for a variable
  private String[] names, prevalues, values;
  private List<String> args;

  public ArgsParser(char varEscapeChar, List<String> args) {
    this.varEscapeChar = varEscapeChar;
    this.args = args;
  }
  public ArgsParser setNames(String... names) {
    // Optimization
    // Assume that the argument names don't change, so don't need to recompute
    // After all, there is only one instance of ArgsParser for every
    // instantiation of a command.
    if(this.names != null) return this;

    this.names = names;
    // Set the prevalues (may contain substitutions)
    this.prevalues = new String[names.length];
    for(int i = 0; i < args.size(); i++) {
      List<String> kv = StrUtils.splitIgnoreEscaped(args.get(i), "=");
      if(kv.size() == 0)
        prevalues[i] = "";
      else if(kv.size() == 1) // Just a regular argument
        prevalues[i] = kv.get(0);
      else // Of the form key = value
        prevalues[getArgIndex(kv.get(0))] = kv.get(1);
    }

    return this;
  }

  private int getArgIndex(String name) {
    for(int i = 0; i < names.length; i++)
      if(names[i].equals(name)) return i;
    throw new RuntimeException("Unknown name: " + name);
  }

  public void parse(VarBindingList bindings) {
    if(this.names == null)
      values = ListUtils.stringToArray(args);
    else
      values = (String[])prevalues.clone();
    for(int i = 0; i < values.length; i++) {
      // Substitute with variable bindings
      values[i] = bindings.substitute(values[i]);
      values[i] = unescape(values[i]);
    }
  }

  // Replace \<char> with <char> except when <char> = exceptChar
  public static String unescape(String s, char exceptChar) {
    if(s == null) return null;
    StringBuilder buf = new StringBuilder();
    boolean escape = false;
    for(int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if(escape) { buf.append(c); escape = false; }
      else {
        // Going to escape the next character
        if(c == '\\' && !(i+1 < s.length() && s.charAt(i+1) == exceptChar))
          escape = true;
        else // Normal character
          buf.append(c);
      }
    }
    return buf.toString();
  }
  public static String unescape(String s) { return unescape(s, (char)0); }

  public int size() { return values.length; }

  public RuntimeException badArg(int i) {
    return new RuntimeException(String.format(
      "Bad index: %d, names = %s", i, StrUtils.join(names)));
  }

  public String get(int i, String defValue) { return values[i] == null ? defValue : values[i]; }
  public String get(String var, String defValue) { return get(getArgIndex(var), defValue); }
  public int getInt(int i, int defValue) { return Utils.parseIntEasy(get(i, null), defValue); }
  public int getInt(String var, int defValue) { return getInt(getArgIndex(var), defValue); }
  public boolean getBoolean(int i, boolean defValue) { return Utils.parseBooleanEasy(get(i, null), defValue); }
  public boolean getBoolean(String var, boolean defValue) { return getBoolean(getArgIndex(var), defValue); }
  public double getDouble(int i, double defValue) { return Utils.parseDoubleEasy(get(i, null), defValue); }
  public double getDouble(String var, double defValue) { return getDouble(getArgIndex(var), defValue); }

  public String getHard(int i) { if(values[i] == null) throw badArg(i); return values[i]; }
  public String getHard(String var) { return getHard(getArgIndex(var)); }
  public int getIntHard(int i) { return Utils.parseIntHard(get(i, null)); }
  public int getIntHard(String var) { return getIntHard(getArgIndex(var)); }
  public boolean getBooleanHard(int i) { return Utils.parseBooleanHard(get(i, null)); }
  public boolean getBooleanHard(String var) { return getBooleanHard(getArgIndex(var)); }
  public double getDoubleHard(int i) { return Utils.parseDoubleHard(get(i, null)); }
  public double getDoubleHard(String var) { return getDoubleHard(getArgIndex(var)); }
}
