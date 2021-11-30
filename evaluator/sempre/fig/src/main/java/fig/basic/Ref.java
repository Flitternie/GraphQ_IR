package fig.basic;

// Convenient way to pass by reference
public class Ref<T> implements java.io.Serializable {
  public static final long serialVersionUID = 42L;
  public T value;
  public Ref() { this.value = null; }
  public Ref(T value) { this.value = value; }
  @Override public String toString() { return "Ref(" + value + ")"; }
}
