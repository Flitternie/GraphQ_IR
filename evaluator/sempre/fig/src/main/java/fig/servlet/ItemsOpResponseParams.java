package fig.servlet;

import java.util.*;

public class ItemsOpResponseParams extends ResponseParams {
  public ItemsOpResponseParams(String op) { this.op = op; }

  public void setSuccess(String item, String msg) {
    successItems.add(item);
    put("msg." + item, msg);
  }

  public void setFailed(String item, String msg) {
    failedItems.add(item);
    put("msg." + item, msg);
  }

  public ResponseParams finish() {
    put("success", ""+(failedItems.size() == 0));
    if(successItems.size() > 0) put("successItems", successItems);
    if(failedItems.size() > 0)  put("failedItems", failedItems);
    setMsg("Operation " + op + " on " + (successItems.size()+failedItems.size()) + " items");
    return this;
  }

  private List<String> successItems = new ArrayList<String>();
  private List<String> failedItems = new ArrayList<String>();
  private String op;
}
