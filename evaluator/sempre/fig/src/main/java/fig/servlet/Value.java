package fig.servlet;

public class Value {
  public Value(String value) {
    this.value = value;
    this.cmpKey = null;
  }
  public Value(String value, String cmpKey) {
    this.value = value;
    this.cmpKey = cmpKey;
  }
  public Value(int value) {
    this.value = ""+value;
    this.cmpKey = ""+value;
  }
  public String toString() { return value; }
  public final String value;
  public final String cmpKey;
}
