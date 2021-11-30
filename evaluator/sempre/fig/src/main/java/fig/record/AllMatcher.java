package fig.record;

/**
 * Matches all strings.
 */
public class AllMatcher implements Matcher {
  public boolean matches(String s, VarBindingList bindings) { return true; }
  public String toString() { return "*"; }
  public static final AllMatcher matcher = new AllMatcher();
}
