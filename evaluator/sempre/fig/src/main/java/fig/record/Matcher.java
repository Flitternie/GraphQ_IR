package fig.record;

public interface Matcher {
  // Whether string s matches given the variable bindings
  // (which may affect how the matcher behaves).
  public boolean matches(String s, VarBindingList bindings);
}
