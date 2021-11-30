package fig.servlet;

public interface BasketFactory {
  public BasketItem newBasketItem(Item parent, String name, String sourcePath);
}
