package fig.record;

public class RecordNodeMatcher {
  public RecordNodeMatcher(Matcher keyMatcher, Matcher valueMatcher) {
    this.keyMatcher = keyMatcher;
    this.valueMatcher = valueMatcher;
  }

  // Return the key required if such a key exists.
  // Otherwise, return null.
  /*public String getReqKey() {
    if(keyMatcher instanceof ExactMatcher)
      return ((ExactMatcher)keyMatcher).getValue();
    return null;
  }*/

  public boolean matches(RecordNode node, VarBindingList bindings) {
    return keyMatcher.matches(node.getKey(), bindings) &&
      valueMatcher.matches(node.getValue(), bindings);
  }

  public boolean matchesAll() {
    return keyMatcher == AllMatcher.matcher &&
           valueMatcher == AllMatcher.matcher;
  }

  public Matcher getKeyMatcher() { return keyMatcher; }
  public Matcher getValueMatcher() { return valueMatcher; }

  public String toString() {
    return keyMatcher + "=" + valueMatcher;
  }

  private Matcher keyMatcher;
  private Matcher valueMatcher;
}
