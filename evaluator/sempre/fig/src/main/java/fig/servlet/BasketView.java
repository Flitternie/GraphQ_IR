package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

/**
 * A list of baskets.
 */
public class BasketView extends Item {
  public static final BasketFactory defaultBasketFactory = new BasketFactory() {
    public BasketItem newBasketItem(Item parent, String name, String sourcePath) {
      return new BasketItem(parent, name, sourcePath);
    }
  };

  private BasketFactory factory;
  public final BasketItem clipboardBasket;

  protected String getDescription() {
    return "A scratch area" + (clipboardBasket != null ? " (includes clipboard)" : "") + ".";
  }

  public BasketView(Item parent, String name, String sourcePath, BasketFactory factory, boolean includeClipboard) {
    super(parent, name, sourcePath);
    this.factory = factory;
    IOUtils.createNewDirIfNotExistsEasy(sourcePath);
    IOUtils.createNewFileIfNotExistsEasy(fileSourcePath());
    if(includeClipboard)
      addItem(this.clipboardBasket = (BasketItem)newItem("clipboard"));
    else
      this.clipboardBasket = null;
  }
  public BasketView(Item parent, String name, String sourcePath, boolean includeClipboard) {
    this(parent, name, sourcePath, defaultBasketFactory, includeClipboard);
  }

  public FieldListMap getItemsFields() {
    return factory.newBasketItem(null, null, null).getMetadataFields();
  }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    updateItemsFromFile(spec,
        clipboardBasket != null ? Collections.singletonList(clipboardBasket) : Collections.EMPTY_LIST,
        Collections.EMPTY_LIST);
    updateChildren(spec, priority.next());
  }

  protected boolean isView() { return true; }
  protected Item newItem(String name) {
    return factory.newBasketItem(this, name, childNameToIndexSourcePath(name));
  }
  protected String itemToHandle(Item item) throws MyException {
    if(item == clipboardBasket) return null;
    return super.itemToHandle(item);
  }
}
