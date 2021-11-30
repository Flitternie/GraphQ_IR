package fig.html;

/**
 * Useful methods for constructing HTML elements.
 */
public class HtmlUtils {
  public HtmlElement elem(String tag) {
    return new HtmlElement(tag);
  }

  public HtmlElement html() { return elem("html"); }
  public HtmlElement title(String value) { return elem("title").child(value); }
  public HtmlElement link() { return elem("link"); }
  public HtmlElement script() { return elem("script"); }
  public HtmlElement head() { return elem("head"); }
  public HtmlElement body() { return elem("body"); }
  public HtmlElement span() { return elem("span"); }
  public HtmlElement span(String value) { return elem("span").child(value); }
  public HtmlElement span(HtmlElement value) { return elem("span").child(value); }
  public HtmlElement div() { return elem("div"); }
  public HtmlElement table() { return elem("table"); }
  public HtmlElement tr() { return elem("tr"); }
  public HtmlElement td(String value) { return elem("td").child(value); }
  public HtmlElement td(HtmlElement value) { return elem("td").child(value); }
  public HtmlElement h1() { return elem("h1"); }
  public HtmlElement a() { return elem("a"); }
  public HtmlElement form() { return elem("form"); }
  public HtmlElement input() { return elem("input"); }
  public HtmlElement text(String value) { return input().type("text").value(value); }
  public HtmlElement button(String value) { return input().type("submit").value(value); }
  public HtmlElement ul() { return elem("ul"); }
  public HtmlElement ol() { return elem("ol"); }
  public HtmlElement li() { return elem("li"); }
  public HtmlElement img() { return elem("img"); }
  public HtmlElement b(String value) { return elem("b").child(value); }
}
