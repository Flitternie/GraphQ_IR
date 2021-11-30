package fig.record;

public class RegexMatcher implements Matcher {
  public RegexMatcher(String patternStr) {
    this.patternStr = patternStr;
    if(!VarBindingList.containsVar(patternStr))
      this.pattern = convert(patternStr);
  }
  public boolean matches(String s, VarBindingList bindings) {
    java.util.regex.Pattern pattern = this.pattern;
    if(pattern == null)
      pattern = convert(bindings.substitute(patternStr));
    return pattern.matcher(s).matches();
  }
  public String toString() { return patternStr; }

  private static java.util.regex.Pattern convert(String patternStr) {
    return java.util.regex.Pattern.compile(patternStr);
  }

  private java.util.regex.Pattern pattern;
  private String patternStr;
}
