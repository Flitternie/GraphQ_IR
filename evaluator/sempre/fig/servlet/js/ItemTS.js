/**
 * An item table state knows about operations and trails.
 * Additional fields:
 *   - isView (item)
 */
inheritClass(ItemTS, TableState);

function ItemTS(table, block) {
  TableState.call(this, table, block);
  this.addAction(this.doUp,                 "_: Go up the trail hierarchy", "u");
  this.addAction(this.doGo,                 "_: Go to a trail by name (will prompt)", "g");
  this.addAction(this.doSwitchTables,       "_: Switch between metadata/items view", "shift-t");
  this.addAction(this.doNewWindow,          "_: Move current block to new window", "shift-w");
  this.addAction(this.doCopyToClipboard,    "_: Copy current block to clipboard", "shift-y");
  this.addAction(this.doClearClipboard,     "_: Clear clipboard", "shift-z");
  if(this.isItemsTable()) {
    this.addAction(this.doSaveItems,    "s: Save items (including order) in current view");
    this.addAction(this.doPurge,        "p: Purge checked items (moves files on disk to .purged)");
    this.addAction(this.doNewItem,      "_: Create new item (- for divider)", "shift-n");
    //this.addAction(this.doGetIntrinsicFields, "f: Get field values of checked items");
    this.addAction(this.doCopyItemsToClipboard, "_: Copy checked items to clipboard", "y");
    this.addAction(this.doPasteItemsFromClipboard, "_: Paste items from clipboard into current view", "p");
  }
}

var CLASS = ItemTS.prototype;

CLASS.TABLE_METADATA = "getMetadataTable";
CLASS.TABLE_ITEMS    = "getItemsTable";
CLASS.clipboardView = function() { return "baskets\tclipboard"; }

CLASS.newRequest = function(op) {
  var request = new Object();
  request.mode = "op";
  request.op = op;
  request.trail = this.getTrail();
  return request;
}

CLASS.newChildRequestWithCurrItem = function(op) {
  return this.newChildRequest(op, this.itemName(this.currItem));
}

CLASS.newChildRequest = function(op, childItemSpec) {
  var request = new Object();
  request.mode = "op";
  request.op = "childOp";
  request.childOp = op;
  if(typeof(childItemSpec) == "string")
    request.childItem = childItemSpec;
  else // Array
    request.childItems = childItemSpec.join("\t");
  request.trail = this.getTrail();
  return request;
}

// Table type is either TABLE_METADATA or TABLE_ITEMS
CLASS.getOp = function() { return this.block.request.op; }
CLASS.getTrail = function() { return this.block.request.trail; }
CLASS.getTableType = function() { return this.getOp(); }
CLASS.isItemsTable = function() { return this.getTableType() == this.TABLE_ITEMS; }

CLASS.reloadIfSuccessHandler = function() {
  var self = this;
  return function(resp) {
    if(resp.success == "true")
      self.block.reload();
  }
}

CLASS.getSaveRequest = function(cell, value) {
  var request = this.newRequest(this.isItemsTable() ? "saveValues" : "saveMetadata");
  request.item = this.cellToRow(cell).getAttribute("itemName");
  request.field = this.cellToHeader(cell).getAttribute("fieldName");
  request.value = value;
  return request;
}

CLASS.doSaveItems = function() {
  var request = this.newRequest("saveItems");
  request.items = this.getAllItemNames().join("\t");
  this.sendRequest(request, this.reloadIfSuccessHandler());
}

CLASS.doCopyToClipboard = function() {
  var trail = this.clipboardView(); if(!trail) return;
  var request = this.newRequest("copyItem");
  request.destTrail = trail;
  this.sendRequest(request);
}

CLASS.doClearClipboard = function() {
  var trail = this.clipboardView(); if(!trail) return;
  var request = this.newRequest("saveItems");
  request.trail = trail;
  request.items = "";
  request.force = "true"; // Don't keep things that we haven't seen
  this.sendRequest(request);
}

CLASS.doPasteItemsFromClipboard = function() {
  var trail = this.clipboardView(); if(!trail) return;
  var request = this.newRequest("addItems");
  request.srcTrail = trail;
  this.sendRequest(request, this.reloadIfSuccessHandler());
}

CLASS.doNewItem = function() {
  var name = prompt("Item name (use prefix - for divider)?");
  if(name == null) return; // (allow empty names)
  var request = this.newRequest("newItem");
  request.name = name;
  this.sendRequest(request, this.reloadIfSuccessHandler());
}

CLASS.doGetIntrinsicFields = function() {
  var items = this.getCheckedItemNames();
  if(items.length == 0) return;
  var name = prompt("Field name?"); if(!name) return;
  var request = this.newChildRequest("getIntrinsicField", items);
  request.field = name;
  this.sendRequest(request);
}

CLASS.doCopyItemsToClipboard = function() {
  var trail = this.clipboardView(); if(!trail) return;
  var items = this.getCheckedItemNames();
  if(items.length == 0) return;
  var request = this.newChildRequest("copyItem", items);
  request.destTrail = trail;
  this.sendRequest(request);
}

CLASS.doUp = function() {
  //var request = this.newRequest(this.getOp());
  var request = this.newRequest(this.TABLE_ITEMS);
  var parentTrail = this.getTrail().split("\t").slice(0, -1).join("\t");
  request.trail = parentTrail;
  this.block.reload(request);
}

CLASS.doGo = function() {
  var trail = prompt("Trail to go to (e.g., baskets clipboard)?");
  if(trail == null) return;
  var request = this.newRequest(this.getOp());
  request.trail = trail.replace(/ /g, "\t");
  this.block.reload(request);
}

CLASS.doNewWindow = function() {
  var request = this.newRequest(this.getOp());
  request.mode = "display";
  request.name = "untitled";
  this.sendMetaRequest({type:"newWindow", request:request});
  this.block.blockSet.removeBlock(this.block);
}

CLASS.doVisualize = function(mode) {
  var request = this.newRequest("visualize");
  request["visualize.mode"] = mode;
  this.sendMetaRequest({type:"dataPanel", request:request});
}

CLASS.isView = function() { return this.table.getAttribute("isView") != null; }

CLASS.doSwitchTables = function() {
  var request = this.newRequest(
    !this.isView() || this.isItemsTable() ?
    this.TABLE_METADATA : this.TABLE_ITEMS);
  this.block.reload(request);
}

CLASS.getOpenMetaRequests = function(row, showType) {
  if(!this.isItemsTable()) return null;
  var request = this.newChildRequest(null, row.getAttribute("itemName"));
  var block = this.block;

  function req(op) { return addToObj(request, "childOp", op); }
  function thisBlock() { return block; }
  function nextBlock() { return block.createBlockNext(); }
  function endBlock()  { return block.createBlockEnd(); }

  var isView = row.getAttribute("isView") != null;
  if(showType == "inline")
    return isView ? [{type:"block", block:thisBlock(), request:req(this.TABLE_ITEMS)}]
                  : [{type:"block", block:thisBlock(), request:req(this.TABLE_METADATA)}];
  if(showType == "newBlock")
    return isView ? [{type:"block", block:endBlock(), request:req(this.TABLE_ITEMS),    focus:true}]
                  : [{type:"block", block:endBlock(), request:req(this.TABLE_METADATA), focus:true}];
  if(showType == "newWindow")
    return [{type:"newWindow", request:addToObj(req(this.TABLE_METADATA), "mode", "display", "name", "untitled")}];
}

CLASS.sendRequestWithCheckedItems = function(msg, op, respHandler) {
  var items = this.getCheckedItemNames();
  if(items.length == 0) return null;
  if(msg && !confirm(msg + " (" + items.length + " items)")) return null;

  var request = this.newChildRequest(op, items);
  return this.sendRequest(request, respHandler);
}

CLASS.doPurge = function() {
  var self = this;
  function respHandler(resp) {
    // Remove the rows that were successfully removed
    if(resp.successItems) {
      var successItemNames = resp.successItems.split("\t");
      self.removeItemNames(successItemNames);
      self.doSaveItems();
    }
  }
  this.sendRequestWithCheckedItems("Permanently purge checked items?", "purge", respHandler);
}
