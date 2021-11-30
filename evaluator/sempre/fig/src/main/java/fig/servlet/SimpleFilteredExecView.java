package fig.servlet;

import fig.basic.*;

public abstract class SimpleFilteredExecView extends FilteredExecView {
  private String description;
  public SimpleFilteredExecView(Item parent, String name, String description) {
    super(parent, name, null);
    this.description = description;
  }
  protected abstract boolean accept(ExecItem item);
  protected String getDescription() { return description; }
  protected void filterItems(OrderedMap<String,Item> newItems) {
    for(Item item : getAllExecView().items.values()) {
      if(!(item instanceof ExecItem)) continue;
      if(accept((ExecItem)item))
        addItem(newItems, item);
    }
  }
}

