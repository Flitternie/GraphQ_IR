package fig.servlet;

/**
 * When we load items from disk, and we can't parse a handle,
 * we create one of these objects to preserve the handle.
 * When we save to disk, the handle goes out as it came in.
 */
class InvalidHandleItem extends Item {
  public final String handle;

  public InvalidHandleItem(Item parent, String handle) {
    super(parent, "invalid", null);
    this.handle = handle;
  }

  public String getDescription() { return handle; }
  public boolean isView() { return false; }
  public Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}

