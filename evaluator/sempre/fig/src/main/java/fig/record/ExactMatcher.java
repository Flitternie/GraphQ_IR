package fig.record;

public class ExactMatcher implements Matcher {
  private String value;

  public ExactMatcher(String value) { this.value = value; }
  public boolean matches(String s, VarBindingList bindings) {
    return s != null && s.equals(bindings.substitute(value));
  }
  public String toString() { return value; }
}
