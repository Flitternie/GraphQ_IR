package fig.html;

import java.util.*;

/**
 * Represents an HTML DOM element.  Allows for easy construction (adding
 * attributes and children) just for purposes of serializing to strings.
 */
public class HtmlElement {
  private String tag;
  private LinkedHashMap<String, String> attributes = new LinkedHashMap<String, String>();
  private List<Object> children = new ArrayList<Object>();  // Contains HtmlElements and Strings

  public HtmlElement(String tag) {
    this.tag = tag;
  }

  public HtmlElement attr(String key, Object value) {
    attributes.put(key, value.toString());
    return this;
  }

  // Common attributes
  public HtmlElement id(String value) { return attr("id", value); }
  public HtmlElement cls(String value) { return attr("class", value); }
  public HtmlElement href(String value) { return attr("href", value); }
  public HtmlElement src(String value) { return attr("src", value); }
  public HtmlElement autofocus() { return attr("autofocus", true); }
  public HtmlElement rel(String value) { return attr("rel", value); }
  public HtmlElement type(String value) { return attr("type", value); }
  public HtmlElement size(int n) { return attr("size", n); }
  public HtmlElement name(String name) { return attr("name", name); }
  public HtmlElement value(String value) { return attr("value", value); }
  public HtmlElement action(String value) { return attr("action", value); }
  public HtmlElement style(String value) { return attr("style", value); }
  public HtmlElement nowrap() { return attr("nowrap", true); }

  public HtmlElement child(HtmlElement child) { this.children.add(child); return this; }
  public HtmlElement child(String child) { this.children.add(child); return this; }

  public HtmlElement end() { return this; }

  public String open() {
    StringBuilder out = new StringBuilder();
    out.append("<" + tag);
    for (Map.Entry<String, String> e : attributes.entrySet())
      out.append(" " + e.getKey() + "=\"" + e.getValue() + "\"");
    out.append(">");
    return out.toString();
  }
  public String close() { return "</" + tag + ">"; }

  @Override public String toString() {
    StringBuilder out = new StringBuilder();
    out.append(open());
    if (children.size() > 1) out.append("\n");
    for (Object child : children) {
      if (child == null) continue;
      out.append(child + "\n");
    }
    out.append(close());
    if (children.size() > 1) out.append("\n");
    return out.toString();
  }
}
