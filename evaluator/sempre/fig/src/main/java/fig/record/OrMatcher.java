package fig.record;

import java.util.*;
import fig.basic.*;

// Matches if any of these matchers fire
public class OrMatcher implements Matcher {
  private List<Matcher> matchers;

  public OrMatcher() { matchers = new ArrayList<Matcher>(); }
  public OrMatcher(List<Matcher> matchers) { this.matchers = matchers; }

  public boolean matches(String s, VarBindingList bindings) {
    for(Matcher m : matchers)
      if(m.matches(s, bindings)) return true;
    return false;
  }

  public void addMatcher(Matcher m) { matchers.add(m); }

  public List<Matcher> getMatchers() { return matchers; }
  public String toString() { return "{" + StrUtils.join(matchers, ",") + "}"; }
}
