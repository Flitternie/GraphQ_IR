package fig.servlet;

import java.io.*;
import java.util.*;
import fig.html.*;
import fig.basic.*;

/**
 * An item is the single primitive unit of data.
 * Items are arranged in a tree-like DAG
 * (there is one root and each item has a primary parent).
 *
 * An item contains
 *  - Metadata information: a mapping from field to value.
 *  - Children items: an ordered list;
 *    Each child is identified by a unique name.
 *
 * Each item is identified by uniquely by a trail (a list of names).
 *
 * Most items are supported by a source file or directory.
 * which contains metadata information and also the list of (child) items.
 * In the file, the child items are specified by not names or trails but a
 * handle.  It is up to particular item to decide now to convert a handle
 * into an item.  At any point in time, the version on disk is the most updated
 * version.  So when a change is made via the web, we need to save it to disk
 * immediately and hope the version on disk hasn't changed.
 *
 * An item has the following functionality:
 *  - handleOperation: processes a request (typically from a browser);
 *    Some standard operations:
 *     - getMetadataTable(name)
 *     - saveMetadata
 *     - copyItem(destTrail)
 *    - childOp(childOp, childItem(s)): dispatch to children
 *    - saveItems(): a general way to implement removing and ordering items.
 *
 * Metadata:
 * An item contains an intrinsic field -> value mapping,
 *  which is used to supplement the fields.
 *
 * An item could be hidden
 * (not displayed in items but accessible via a trail)
 * or dead
 * (to be deleted at one's convenience).
 *
 * Updating (this is no longer accurate):
 * Only the update() function is allowed to read from the disk,
 * and then even so, it should do a constant amount of work (no recursive reads).
 * The idea is that one request will result in exactly one update();
 * The rest will be queued.
 */
public abstract class Item {
  // Some default fields that we can use.
  public static final Field trailField =
    new IntrinsicField("trail","Unique list of names that identifies the item");
  public static final Field countField =
    new IntrinsicField("count", "#", "Number of child items");
  public static final Field descriptionField =
    new IntrinsicField("description", "Description of this item.");
  public static final Field mutableDescriptionField =
    new IntrinsicField("description", "Description of this item.").setMutable(true);
  public static final FieldListMap countDescriptionFields =
    new FieldListMap(ListUtils.newList(countField, descriptionField));
  public static final FieldListMap countMutableDescriptionFields =
    new FieldListMap(ListUtils.newList(countField, mutableDescriptionField));

  protected final Item parent;
  protected final String name; // Name that parent uses to identify me
  public final String sourcePath; // Where to load my data
  protected Map<String,String> metadataMap; // Data
  protected OrderedMap<String,Item> items; // Data

  // Whether this item has been sent by parent to the client.
  // If not, then View.saveItems will not accidentally kill this item.
  // This is a (very) crude form of version control.
  protected boolean parentHasSentMe;

  // When we want to purge an item, it could be referenced from all over,
  // and we don't know where, so we mark it as dead,
  // so whoever references it will ignore it.
  protected boolean isDead;

  private static HtmlUtils H = new HtmlUtils();

  public Item(Item parent, String name, String sourcePath) {
    this.parent = parent;
    this.name = name;
    this.sourcePath = sourcePath;
    this.metadataMap = new LinkedHashMap();
    this.items = new OrderedMap();
  }

  protected boolean isRoot() { return parent == null; }

  // If children are based on index source paths
  protected String childNameToIndexSourcePath(String name) {
    return new File(sourcePath, name+".index").toString();
  }

  // Get the global identifier that can be used to identify this item,
  // but bear in mind that the name might change
  protected Trail getTrail() {
    // Follow parent until we hit the root
    List<String> names = new ArrayList();
    for(Item item = this; !item.isRoot(); item = item.parent)
      names.add(item.name);
    Collections.reverse(names);
    return new Trail(names);
  }

  protected Item getRoot() {
    Item item = this;
    while(!item.isRoot()) item = item.parent;
    return item;
  }

  // Access child items
  protected Item getItem(String name) throws MyException {
    Item item = items.get(name);
    if(item == null) throw new NameNotFoundException(this, name);
    return item;
  }
  protected Item getItemEasy(String name) { return items.get(name); }
  protected Item getItemOrNew(String name) throws MyException {
    // Get the item; return a new one if it doesn't exist
    Item item = getItemEasy(name);
    if(item == null) item = newItem(name);
    return item;
  }
  public Item getItemOrNewAdd(String name) throws MyException {
    // Get the item; return a new one AND add it if it doesn't exist
    Item item = getItemEasy(name);
    if(item == null) addItem(item = newItem(name));
    return item;
  }

  public Item trailToItem(Trail trail) throws MyException {
    Item item = getRoot();
    // Walk the item tree using the names in the trail
    for(String name : trail.names)
      item = item.getItem(name);
    return item;
  }

  // Add to items
  protected void addItem(Item item) { // OVERRIDE
    addItem(items, item);
  }
  protected synchronized void addItem(OrderedMap<String, Item> items, Item item) {
    if(item.isDead) return; // Skip dead items
    items.put(itemToNewName(items, item), item);
  }

  protected boolean isHidden() { return false; } // OVERRIDE
  protected String getDescription() { return metadataMap.get("description"); } // OVERRIDE

  protected Value getIntrinsicFieldValue(String fieldName) throws MyException { // OVERRIDE
    if(fieldName.equals("trail"))       return new Value(getTrail().toDisplayString());
    if(fieldName.equals("count"))       return new Value(items.size());
    if(fieldName.equals("description")) return new Value(getDescription());
    return new Value(metadataMap.get(fieldName));
  }
  protected void changeIntrinsicFieldValue(String fieldName, String value) throws MyException {
    metadataMap.put(fieldName, value);
    // Find the lowest non-embedded parent, and call save on it
    Item item = this;
    while(item != null && item.isEmbedded()) item = item.parent;
    item.saveToDisk();
  }

  protected FieldListMap getMetadataFields() { // OVERRIDE
    FieldListMap fields = new FieldListMap();
    fields.add(trailField);
    for(Map.Entry<String,String> e : metadataMap.entrySet())
      fields.add(e.getKey(), e.getKey(), e.getValue());
    if(!fields.containsKey("description"))
      fields.add(descriptionField);
    return fields;
  }
  protected FieldListMap getItemsFields() { // OVERRIDE
    return countDescriptionFields;
  }
  protected FieldListMap getDynamicFieldListMap() {
    // Find the first fields specification item if it exists
    FieldSpecItem fieldSpecItem = null;
    for(Item item : items.values()) {
      if(item instanceof FieldSpecItem) {
        fieldSpecItem = (FieldSpecItem)item;
        break;
      }
    }
    return (fieldSpecItem != null) ? fieldSpecItem.createFieldListMap() : null;
  }

  protected HtmlElement getMetadataTable() throws MyException {
    // Create the table
    FieldListMap fields = getMetadataFields();
    HtmlElement table = H.table();
    table.attr("trail", getTrail().toRepnString());
    if(isView()) table.attr("isView", true);

    // Create header (empty)
    HtmlElement header = H.tr();
    header.child(H.td(""));
    header.child(H.td(""));
    table.child(header);

    for(Field field : fields.values()) {
      HtmlElement row = H.tr();
      row.attr("itemName", field.name);
      row.attr("gloss", field.gloss);
      row.child(H.td(field.displayName).nowrap());
      row.child(H.td(fieldToCell(field, field.getValue(this).value)).nowrap());
      table.child(row);
    }

    return table;
  }

  // Helper function for populating a html cell with the value
  // The field provides some formatting information.
  protected HtmlElement fieldToCell(Field field, Object value) {
    HtmlElement cell = H.td(value+"");
    if(field.numeric) {
      cell.attr("numeric", true);
      cell.attr("justify", "right");
    }
    if(field.mutable)
      cell.attr("mutable", true);
    if(field.multiline)
      cell.attr("multiline", true);
    return cell;
  }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException { // OVERRIDE
    loadFromDisk();
  }

  // If we want immediate results: should be called only when we need to display a table
  protected void updateMeNow(UpdateSpec spec) throws MyException {
    update(spec, UpdateQueue.Priority.HIGH);
  }

  protected HtmlElement getItemsTable() throws MyException {
    // Create the table
    FieldListMap fields = getItemsFields();
    HtmlElement table = H.table();
    if(isView()) table.attr("isView", true);

    // Create header
    HtmlElement header = H.tr();
    HtmlElement cell = H.td("name"); // Name field
    cell.attr("fieldName", "name");
    cell.attr("gloss", "Name");
    header.child(cell);
    for(Field field : fields.values()) { // Rest of the fields
      if(field.hidden) continue;
      cell = fieldToCell(field, field.displayName);
      cell.attr("fieldName", field.name);
      cell.attr("gloss", field.gloss);
      cell.nowrap();
      header.child(cell);
    }
    table.child(header);

    // Sort spec
    Pair<String, Boolean> sortSpec = getDefaultSortSpec();
    Field sortField = null;
    boolean sortByName = false;
    boolean reverse = false;
    if(sortSpec != null) {
      sortByName = "name".equals(sortSpec.getFirst());
      sortField = fields.get(sortSpec.getFirst());
      reverse = sortSpec.getSecond();
    }

    // Get rows
    List<Entry> entries = new ArrayList<Entry>();
    for(String name : items.keys()) {
      Item item = items.get(name);
      // Don't display hidden or dead items
      if(item.isHidden() || item.isDead) continue;
      Comparable cmpKey = null;
      if(sortByName)
        cmpKey = name;
      else if(sortField != null) {
        Value value = sortField.getValue(item);
        String s = value.cmpKey == null ? value.value : value.cmpKey;
        if(sortField.numeric)
          cmpKey = Utils.parseDoubleEasy(s);
        else
          cmpKey = (s == null ? "" : s);
      }
      item.parentHasSentMe = true; // Mark the item as sent
      entries.add(new Entry(name, item, cmpKey));
    }
    // Sort
    if(sortByName || sortField != null) {
      Collections.sort(entries);
      if(reverse) Collections.reverse(entries);
    }

    // Make the last mutable field of a divider the description
    Field lastMutableField = null;
    for(Field field : fields.values())
      if(field.mutable) lastMutableField = field;

    // Create a row for each item
    for(Entry entry : entries) {
      String name = entry.name;
      Item item = entry.item;
      HtmlElement row = H.tr();
      row.attr("itemName", name);
      if(item.isView()) row.attr("isView", true);

      if(item instanceof DividerItem)
        name = DividerItem.dividerStr; // Don't display name
      row.child(H.td(name)); // Name field
      for(Field field : fields.values()) { // Rest of the fields
        if(field.hidden) continue;
        if(item instanceof DividerItem) {
          cell = H.td(field == lastMutableField ? ((DividerItem)item).description : DividerItem.dividerStr);
        } else {
          Value value = field.getValue(item);
          cell = H.td(value.value).nowrap();
          if(field.width != 0)
            cell.attr("width", field.width);
          if(value.cmpKey != null)
            cell.attr("cmpKey", value.cmpKey);
        }
        row.child(cell);
      }
      table.child(row);
    }

    return table;
  }
  private static class Entry implements Comparable<Entry> {
    public Entry(String name, Item item, Comparable cmpKey) {
      this.name = name;
      this.item = item;
      this.cmpKey = cmpKey;
    }
    public int compareTo(Entry e) { return cmpKey.compareTo(e.cmpKey); }
    public final String name;
    public final Item item;
    public final Comparable cmpKey;
  }
  protected Pair<String,Boolean> getDefaultSortSpec() { return null; } // OVERRIDE

  protected HtmlElement putInBlock(HtmlElement table, String htmlName, String op) { // Helper function
    if(htmlName == null) htmlName = "unknown";
    Trail trail = getTrail();
    table.id(htmlName+".table");
    String title = getClass().getName() + " (" + trail.toDisplayString() + ")";
    String description = getDescription();
    if(!StrUtils.isEmpty(description)) title += ": " + description;
    HtmlElement block = H.div().child(H.div().child(title)).child(H.div().child(table));
    block.id(htmlName+".block");
    block.type(tableType());
    block.attr("op", op);
    block.attr("trail", trail.toRepnString());
    return block;
  }

  ////////////////////////////////////////////////////////////
  // Save items

  protected synchronized ResponseParams saveItems(RequestParams req) throws MyException {
    ResponseParams resp = new ResponseParams("Saved items");

    // Save the items (remove and order operations)
    OrderedMap<String, Item> newItems = new OrderedMap<String, Item>();
    String[] names = req.getStringListReq("items");
    for(String name : names) {
      Item item = getItem(name);
      addItem(newItems, item);
    }

    if(!req.getBoolean("force")) {
      // Add the items that haven't been even sent to the client,
      // even though they weren't specified in the request.
      // This is useful when the client doesn't have the most recent
      // update and makes a change (e.g., a purge),
      // whereas here at the server has also made a change (e.g., addToView).
      // When the client calls saveItems(), don't want to lose the server's
      // changes.  This is a crude way of preventing that.
      for(String name : items.keys()) {
        Item item = items.get(name);
        // If we already have added the item but we haven't sent.
        if(!item.parentHasSentMe && !newItems.containsKey(name)) {
          addItem(newItems, item);
          resp.put(name, "NEW");
        }
      }
    }
    items = newItems; // Fast switch!

    saveToDisk();

    return resp;
  }

  // Whether the names should be indices
  protected boolean namesAreIndices() { return false; } // OVERRIDE

  // Even if item already exists in items under a name already,
  // we will add item again under a different name.
  protected String itemToNewName(OrderedMap<String,Item> items, Item item) {
    if(namesAreIndices()) return ""+items.size(); // Use numbering
    // An item already has a name, presumably.
    // Try to use that; if not possible, attach _<integer> after it.
    String baseName = item.name;
    for(int q = 0; ; q++) {
      String name = baseName + (q == 0 ? "" : "_"+q);
      if(!items.containsKey(name))
        return name;
    }
  }
  protected String itemToNewName(Item item) { return itemToNewName(items, item); }

  // Whether we can have children items
  protected abstract boolean isView(); // OVERRIDE

  // Create new child item
  protected abstract Item newItem(String name) throws MyException; // OVERRIDE

  protected String tableType() { return "Item"; } // OVERRIDE

  // For saving to disk: convert between item and handles.
  // When overriding, return null if we don't want to have it saved.
  // Special handle prefixes:
  //  - .div: divider
  //  - .trail: full trail
  //  Otherwise, we assume the handle is a name.
  protected String itemToHandle(Item item) throws MyException { // OVERRIDE
    if(item instanceof InvalidHandleItem)
      return ((InvalidHandleItem)item).handle;
    if(item instanceof DividerItem)
      return ".div\t" + ((DividerItem)item).description;
    if(item.parent != this) // Foreign
      return ".trail\t" + item.getTrail().toRepnString();
    return ".name\t" + item.name;
  }
  protected Item handleToItem(String handle) throws MyException { // OVERRIDE
    String[] tokens = handle.split("\t", 2);
    if(tokens.length == 1) // Backward compatability
      tokens = new String[] { ".name", tokens[0] };

    Item item = null;
    if(tokens[0].equals(".div"))
      item = new DividerItem(this, "divider", tokens[1]);
    else if(tokens[0].equals(".trail"))
      item = trailToItem(new Trail(tokens[1]));
    else if(tokens[0].equals(".name"))
      item = getItemOrNew(tokens[1]);
    else
      throw new MyException("Invalid handle");
    return item;
  }

  // Get the actual file to read
  // To disable loading/saving from/to file, override and return null.
  protected String fileSourcePath() { // OVERRIDE
    if(sourcePath == null) return null;
    return
      new File(sourcePath).isDirectory() ?
      new File(sourcePath, "_index.index").toString() : sourcePath;
  }
  protected synchronized void loadFromDisk() throws MyException {
    if(fileSourcePath() == null) return;
    indentInput(0, IOUtils.readLinesEasy(fileSourcePath()), new IntRef(0));
  }
  private void indentInput(int indent, List<String> lines, IntRef lineIdx) throws MyException {
    OrderedMap<String,Item> newItems = new OrderedMap<String,Item>();
    Item item = null;
    metadataMap.clear();
    while(lineIdx.value < lines.size()) {
      String line = lines.get(lineIdx.value);
      int observedIndent = 0;
      while(observedIndent < line.length() && line.charAt(observedIndent) == '\t')
        observedIndent++;
      if(observedIndent < indent) break; // Done
      if(observedIndent > indent) { // Next
        item.indentInput(observedIndent, lines, lineIdx);
        continue;
      }

      String[] tokens = line.substring(observedIndent).split("\t", 2);
      if(tokens.length == 1) // Backward compatability
        tokens = new String[] { "item", tokens[0] };

      if(tokens[0].equals("item")) {
        try {
          addItem(newItems, item = handleToItem(tokens[1]));
        } catch(MyException e) {
          addItem(newItems, item = new InvalidHandleItem(this, tokens[1]));
        }
      }
      else
        metadataMap.put(tokens[0], tokens[1]);
      lineIdx.value++;
    }
    items = newItems; // Fast switch!
  }

  protected synchronized void saveToDisk() throws MyException {
    if(StrUtils.isEmpty(fileSourcePath())) return; // Nowhere to save
    try {
      PrintWriter out = IOUtils.openOut(fileSourcePath());
      indentOutput(0, out);
      out.close();
    } catch(IOException e) {
      throw new MyException("Unable to save to " + fileSourcePath());
    }
  }
  private void indentOutput(int indent, PrintWriter out) throws MyException {
    StringBuilder indBuf = new StringBuilder();
    for(int i = 0; i < indent; i++) indBuf.append('\t');
    for(Map.Entry<String,String> e : metadataMap.entrySet())
      out.println(indBuf + e.getKey() + "\t" + (e.getValue() == null ? "" : e.getValue()));
    for(Item item : items.values()) {
      String handle = itemToHandle(item);
      if(handle != null) {
        out.println(indBuf + "item\t" + handle); 
        if(item.isEmbedded() && item.parent == this)
          item.indentOutput(indent+1, out);
      }
    }
  }

  // Embedded items rely on their parent to save them to disk.
  private boolean isEmbedded() {
    return StrUtils.isEmpty(sourcePath) || StrUtils.isEmpty(fileSourcePath());
  }

  ////////////////////////////////////////////////////////////
  // Handle operation

  public ResponseObject handleOperation(OperationRP req, Permissions perm) throws MyException {
    String op = req.op;
    if(op.equals("getMetadataTable")) {
      updateMeNow(req.updateSpec);
      HtmlElement table = getMetadataTable();
      return new ResponseElement(putInBlock(table, req.get("name"), op));
    }
    else if(op.equals("saveMetadata")) {
      perm.checkCanModify();
      // In the metadata view (unlike items view),
      // the "item" is actually the field name
      Field field = getMetadataFields().get(req.getReq("item"));
      String value = req.getReq("value");
      field.changeValue(this, value);
      return new ResponseParams("Saved " + name + "." + field.name + " := " + value);
    }
    else if(op.equals("copyItem")) {
      perm.checkCanModify();
      Trail destTrail = new Trail(req.getReq("destTrail"));
      Item destItem = trailToItem(destTrail);
      destItem.addItem(this);
      destItem.saveToDisk();
      return new ResponseParams("Added " + name + " to " + destItem.name + ", which now has " + destItem.items.size() + " items");
    }
    else if(op.equals("childOp")) { // Apply an operation to child(ren)
      String childOp = req.getReq("childOp");
      req = new OperationRP(childOp, req);
      if(req.containsKey("childItem")) { // One child
        Item item = getItem(req.getReq("childItem"));
        return item.handleOperation(req, perm);
      }
      else if(req.containsKey("childItems")) { // Multiple children
        String[] childItemNames = req.getStringListReq("childItems");
        ItemsOpResponseParams resp = new ItemsOpResponseParams(childOp);
        for(String childItemName : childItemNames) {
          try {
            Item item = getItem(childItemName);
            ResponseObject childResp = item.handleOperation(req, perm);
            if(childResp instanceof ResponseParams)
              resp.setSuccess(childItemName, ((ResponseParams)childResp).getMsg());
            else
              resp.setSuccess(childItemName, childResp.toString());
          } catch(MyException e) {
            resp.setFailed(childItemName, e.getMessage());
          }
        }
        return resp.finish();
      }
      else
        throw new ArgumentException("Either childItem or childItems required");
    }
    else if(op.equals("getItemsTable")) {
      updateMeNow(req.updateSpec);
      HtmlElement table = getItemsTable();
      return new ResponseElement(putInBlock(table, req.get("name"), op));
    }
    else if(op.equals("saveItems")) {
      perm.checkCanModify();
      return saveItems(req);
    }
    else if(op.equals("saveValues")) {
      perm.checkCanModify();
      Item item = getItem(req.getReq("item"));
      Field field = getItemsFields().get(req.getReq("field"));
      String value = req.getReq("value");
      field.changeValue(item, value);
      return new ResponseParams("Saved " + item.name + "." + field.name + " := " + value);
    }
    else if(op.equals("addItem")) {
      Trail srcTrail = new Trail(req.getReq("srcTrail"));
      Item srcItem = trailToItem(srcTrail);
      addItem(srcItem);
      saveToDisk();
      return new ResponseParams("Added " + srcTrail.toDisplayString() + " to " + this);
    }
    else if(op.equals("addItems")) {
      Trail srcTrail = new Trail(req.getReq("srcTrail"));
      Item srcItem = trailToItem(srcTrail);
      for(Item item : srcItem.items.values()) addItem(item);
      saveToDisk();
      return new ResponseParams("Added " + srcTrail.toDisplayString() + " to " + this);
    }
    else if(op.equals("newItem")) {
      String name = req.getReq("name");
      Item item;
      if(name.startsWith("-"))
        item = new DividerItem(this, "divider", name.substring(1));
      else {
        // If name is empty, then create a number that hasn't been used
        if(name.equals("")) {
          for(int i = 0; ; i++) {
            name = ""+i;
            if(!items.containsKey(name)) break;
          }
        }
        item = newItem(name);
      }
      addItem(item);
      saveToDisk();
      return new ResponseParams("Created new " + item + " in " + this);
    }
    else if(op.equals("purge")) {
      // Purge the source path (doesn't really delete it, but moves it).
      if(sourcePath == null || !IOUtils.purgePath(new File(sourcePath)))
        throw new MyException("Unable to purge " + name);
      isDead = true;
      return new ResponseParams("Purged " + name);
    }
    else if(op.equals("getIntrinsicField"))
      return new ResponseParams(getIntrinsicFieldValue(req.getReq("field")).value);
    throw new MyException("Unknown operation: " + op);
  }

  ////////////////////////////////////////////////////////////
  // Updating

  // Reads items from the given directory
  protected void updateItemsFromDir(int depth,
      FileUtils.TraverseSpec spec, boolean stripExt) throws MyException {
    OrderedMap<String, Item> newItems = new OrderedMap<String, Item>();
    List<String> childFileNames = FileUtils.getChildren(sourcePath, depth, spec);
    childFileNames = sortFileNames(childFileNames);

    for(String childFileName : childFileNames) {
      String childName =
        stripExt ? IOUtils.stripFileExt(childFileName) : childFileName;
      Item item = getItemEasy(childName); // Recycle old one
      // Create new one if the old one doesn't exist
      if(item == null || item.isDead)
        item = newItem(childName);
      addItem(newItems, item);
    }
    items = newItems; // Fast switch!
  }

  // Sort alphabetically, but so that 5.exec precedes 10.exec
  private List<String> sortFileNames(List<String> names) {
    List<Pair<String,String>> pairs = new ArrayList();
    for (String name : names) {
      // Pad front with zeros
      StringBuilder buf = new StringBuilder();
      int n = 0;
      while (n < name.length() && Character.isDigit(name.charAt(n))) n++;
      while (n < 5) { buf.append('0'); n++; }
      pairs.add(new Pair(name, buf.toString()+name));
    }

    Collections.sort(pairs, new Pair.SecondComparator());

    List<String> newNames = new ArrayList<String>();
    for (Pair<String,String> p : pairs)
      newNames.add(p.getFirst());
    return newNames;
  }

  protected void updateItemsFromFile(UpdateSpec updateSpec) throws MyException {
    updateItemsFromFile(updateSpec, Collections.EMPTY_LIST, Collections.EMPTY_LIST);
  }
  protected void updateItemsFromFile(UpdateSpec updateSpec,
      List<? extends Item> prependItems, List<? extends Item> appendItems) throws MyException {
    loadFromDisk();
    OrderedMap<String, Item> newItems = new OrderedMap<String, Item>();
    for(Item item : prependItems) addItem(newItems, item); // Prepend
    for(Item item : items.values()) addItem(newItems, item);
    for(Item item : appendItems) addItem(newItems, item); // Append
    items = newItems; // Fast switch!
  }

  protected void updateChildren(UpdateSpec spec, UpdateQueue.Priority priority) {
    // Spec is the one to be used for the children
    if(priority == UpdateQueue.Priority.LOW) return;
    // Recursively update on children
    spec.queue.merge(getUpdateQueue(priority));
  }

  // For updating, determine what order to update
  protected UpdateQueue getUpdateQueue(UpdateQueue.Priority priority) {
    // Default: just return them in order
    UpdateQueue queue = new UpdateQueue();
    for(Item item : items.values())
      queue.enqueue(item, priority);
    return queue;
  }

  protected Item findAncestorByClass(Class c) {
    for(Item item = this; item != null; item = item.parent)
      if(item.getClass() == c) return item;
    return null;
  }

  protected boolean containsItem(Item item) {
    for(Item oldItem : items.values())
      if(item == oldItem) return true;
    return false;
  }

  public String toString() { return getTrail().toDisplayString(); }
}
