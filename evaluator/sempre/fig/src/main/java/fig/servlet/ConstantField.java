package fig.servlet;

public class ConstantField extends Field {
  private Value value;

  public ConstantField(String name, String displayName, String gloss, Object obj) {
    super(name, displayName, gloss);
    this.value = processValue(new Value(obj.toString()));
  }
  public Value getValue(Item item) { return value; }
  public String toString() { return value.value; }
}
