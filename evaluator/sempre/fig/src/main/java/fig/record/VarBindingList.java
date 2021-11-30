package fig.record;

/**
 * Variable bindings list.
 * Is a list of (variable, value) pairs.
 * It differs from the global variables in GlobalEnv:
 *  - No mutations.  Adding a binding creates a new list instance.
 *    Perfect for the recursion and creating local scope.
 *    Not expected to be efficient with many bindings.
 *  - Bindings are substituted after the command has parsed,
 *    whereas global variables are macro replacements.
 *    So these binding variables have to respect the syntax.
 *  - Bindings are created by the map function command.
 *
 *  - Currently, strings are only allowed to be either entirely a variable or
 *    not.  FUTURE: allow both, e.g., "hello?x"
 */
public class VarBindingList {
  public static final char varEscapeChar = '?';

  private VarBindingList prev;
  private String var, val;

  private VarBindingList(String var, String val, VarBindingList prev) {
    this.var = var;
    this.val = val;
    this.prev = prev;
  }

  public VarBindingList withNewBinding(String var, String val) {
    return new VarBindingList(var, val, this);
  }

  public String substitute(String s) {
    if(s == null) return null;
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < s.length();) {
      java.util.regex.Matcher m;
      if(s.charAt(i) == '?' &&
          (m = java.util.regex.Pattern.compile("(\\?(\\w+)).*").matcher(s.substring(i))).matches()) {

        String var = m.group(2);
        String val = lookupVar(var);
        if(val == null) val = "?"+var;
        sb.append(val);
        i += m.group(1).length();
      }
      else {
        // Just chug along the string
        sb.append(s.charAt(i));
        i++;
      }
    }
    return sb.toString();
    //if(s != null && s.startsWith("?")) return lookupVar(s.substring(1));
    //return s;
  }

  private String lookupVar(String var) {
    if(this == empty) return null;
    if(this.var.equals(var)) return this.val;
    return prev.lookupVar(var);
  }

  // Can always return true and have correctness, but not efficient.
  // If doesn't contain a variable, then whoever is using this string
  // can preprocess it without waiting for on-the-fly expansion.
  public static boolean containsVar(String s) {
    return s.indexOf('?') != -1;
    //return s != null && s.startsWith("?");
  }

  public static VarBindingList empty = new VarBindingList(null, null, null);
}
