/**
 * Augments an HTML table to enhance the table viewing experience.
 * A TableState keeps track of all the state needed for that.
 * Main features:
 *   - Lots of good keyboard shortcuts.
 *   - Sort fields, edit fields...
 * How to use:
 *   When the HTML page is loaded, call new TableState(table);
 *   Call the onKeyPress(event) function to enable keyboard shortcuts.
 *   The table data consists of a matrix of (item, field) cells.
 *   Each item and each field has a name, and it's entirely symmetric.
 * Attributes (can be applied to the item, field, or cell):
 *   - itemName (item): unique name of item
 *   - fieldName (field): unique name of field
 *   - multiline (item, field, cell): whether a cell, when edited, should use a textarea
 *   - mutable, immutable (item, field, cell): whether a cell can be modified
 *   - numeric (field): whether the values are numeric (for sorting purposes)
 *   - gloss (item, field): what the heck this field is
 *   - cmpKey (cell): use this to compare (for sorting purposes)
 *   - justify (field): left, center, or right
 *   - id (table): ID of the table
 * Methods to consider overriding:
 *   - getOpenMetaRequests()
 *   - getSaveRequest()
 * A meta-request contains the following fields:
 *   - type: where to put the results of the request (block, msgPanel, newWindow)
 *   - block (if type is block): where to put it
 *   - request: what to put
 */

var checkedColor = "FFFFBB"; // When a row is selected
var cursorColor = "D0D0D0"; // When the cursor is on a cell

function TableState(table, block) {
  if(!block) throw "No block specified for " + table;
  if(typeof(table) == "string") table = getReq(table);

  this.table = table;
  this.block = block;

  // The first two rows and first two columns are the cursor and (checkbox or header).
  // The rest is actual content.
  // Within this rest,
  // rows are called items (indexed by i) and
  // columns are called fields (indexed by j).
  this.numItems   = table.rows.length-1; // Minus header
  this.numFields  = table.rows[0].cells.length;
  this.currItem   = 0;
  this.currField  = 0;
  this.useHotKeys = true;
  this.toggleHotKeysButton = null;
  this.numArgBuf = ""; // Number argument that we're building

  // Map from hotkey to function
  this.hotkeyMap = new Object();
  this.actionsMenu  = createElement("select"); // A drop-down menu for actions
  this.actionsPanel = createDiv(); // Place for buttons
  this.dataPanel    = createDiv(); // Place for putting data
  this.msgPanel     = createDiv(); // Place for messages

  // Parameters
  this.focusAfterReload = false;

  // Create panels
  insertManyAfter([this.actionsMenu, this.actionsPanel, this.dataPanel, this.msgPanel], this.table);

  this.prepareActionsMenu();
  this.prepareTable();
}

var CLASS = TableState.prototype;

// Constants {
CLASS.COL_CURSOR = 0;
CLASS.COL_CHECKBOX = 1;
CLASS.ROW_CURSOR = 0;
CLASS.ROW_HEADER = 1;
CLASS.ITEM_OFFSET = 2;
CLASS.FIELD_OFFSET = 2;
CLASS.MARGIN = 50;
// }

// Initialization {
CLASS.prepareActionsMenu = function() {
  // Setup actions menu
  this.actionsMenu.appendChild(new Option("- Actions -"));
  this.actionsMenu.onchange = globalCall(this, this.doSelectedAction);
  var self = this;
  //this.actionsMenu.onkeypress = function(event) // When hit escape, blur
  //this.actionsMenu.onkeydown = function(event) { // When hit escape, blur
    //if(event.keyCode == 27) self.selectActionsMenu(false);
  //}
  this.tempDisableHotKeysOnFocus(this.actionsMenu);

  // Add action buttons
  this.addAction([this.openCurrItem, "inline"],    "_: Open current item (row) in same block", "o");
  this.addAction([this.openCurrItem, "newBlock"],  "_: Open current item (row) in new block",  "shift-o");
  this.addAction([this.openCurrItem, "newWindow"], "_: Open current item (row) in new window", "ctrl-shift-o");
  this.addAction(this.doRemoveCheckedItems,        "r: Remove checked items from view (client-side)");
  this.addAction(this.doCollectCheckedItems,       "c: Show names of checked items (client-side)");
  this.addAction(this.doPrintAggregateStats,       "a: Show min/mean/max of field values of checked items in message panel");
  //this.addAction(this.doShowSource,                "_: Show source");
  this.addAction(this.doHelp,                      "_: Help",                           "shift-?");
  this.addAction([this.sortByCurrField, false],    "_: Sort (incr.) by current field (column)",  "s");
  this.addAction([this.sortByCurrField, true],     "_: Sort (decr.) by current field (column)",  "shift-s");
  this.addAction(this.searchInCurrField,           "_: Search by current field (column)",        "f");
  this.addAction(this.toggleShowCurrField,         "_: Toggle show current field (column)",      "shift-f");
  this.addAction(this.clearMsgPanel,               "_: Clear message panel",            "shift-c");
  this.toggleHotKeysButton = this.addAction(this.toggleUseHotKeys, this.useHotKeysStr());
}

CLASS.prepareTable = function() {
  // Put the table in standard form (add the appropriate rows and columns) {
  // Add rows (header row already exists)
  var cursorRow = createElement("tr");
  for(var field = 0; field < this.numFields; field++) {
    var cell = createElement("td", "align", "center");
    cursorRow.appendChild(cell);
  }
  insertBefore(cursorRow, this.table.rows[0]);

  // Add columns
  var state = this;
  for(var r = 0; r < this.table.rows.length; r++) {
    var row = this.table.rows[r];
    var item = r-this.ITEM_OFFSET;

    // Checkbox (only for the items, not row cursor or row header)
    var checkBoxCell = createElement("td");
    if(item >= 0) {
      var checkbox = createElement("input");
      checkbox.type = "checkbox";
      checkBoxCell.appendChild(checkbox);
    }
    insertBefore(checkBoxCell, row.cells[0]);

    // Cursor
    var cursor = createElement("td");
    insertBefore(cursor, row.cells[0]);
  }
  // }

  // Bold the headings and enable tooltips
  var confGloss = function(cell) {
    cell.onclick = function() { alert(cell.getAttribute("fieldName") + ": " + cell.getAttribute("gloss")); };
    //cell.onmouseover = function() { return escape("gloss"); };
    //cell.onmouseover = function() { alert(escape(cell.getAttribute("gloss"))); };
  };
  for(var field = 0; field < this.numFields; field++) {
    var cell = this.fieldToHeader(field); //this.rowToCell(this.table.rows[this.ROW_HEADER], field);
    cell.innerHTML = "<b>" + cell.innerHTML + "</b>";
    cell.align = "center";
    confGloss(cell);
  }
  //tt_Init();

  // Set mutable, justify, multiline, single-click for each cell
  for(var item = 0; item < this.numItems; item++) {
    var row = this.itemToRow(item);

    var itemMutable = row.getAttribute("mutable") != null;
    var itemMultiline = row.getAttribute("multiline") != null;
    for(var field = 0; field < this.numFields; field++) {
      var fieldMutable = this.fieldToHeader(field).getAttribute("mutable") != null;
      var fieldMultiline = this.fieldToHeader(field).getAttribute("multiline") != null;
      var justify = this.fieldToHeader(field).getAttribute("justify") || "left";

      var cell = this.rowToCell(row, field);
      cell.align = justify;
      cell.mutable = (cell.getAttribute("immutable") == null) && ((cell.getAttribute("mutable") != null) || itemMutable || fieldMutable);
      cell.multiline = (cell.getAttribute("multiline") != null) || itemMultiline || fieldMultiline;
      if(cell.mutable) {
        cell.ondblclick = globalCall(this, this.startEditCell, cell);
        cell.style.color = "606000";
      }

      cell.onclick = globalCall(this, this.setCurrItemField, cell);
    }
  }

  // Set corner (go up one level)
  this.urcornerCell().innerHTML = '<img src="images/up-arrow.gif">';
  this.urcornerCell().onclick = globalCall(this, this.doUp);

  this.refresh();
}
// }

// Writing to the message panel {
CLASS.showMsg = function(text) {
  this.msgPanel.innerHTML = text;
}
CLASS.showWarning = function(text) {
  this.msgPanel.innerHTML = "<font color=orange>WARNING: " + text + "</font>";
}
CLASS.showError = function(text) {
  this.msgPanel.innerHTML = "<font color=red>ERROR: " + text + "</font>";
}
CLASS.clearMsgPanel = function() {
  this.msgPanel.innerHTML = "";
}
CLASS.dbg = function(text) {
  this.msgPanel.appendChild(createDiv(text + "<br>"));
}
CLASS.dbgObj = function(x) {
  this.dbg(x + ":");
  for(k in x) this.dbg("  " + k + ": " + x[k]);
}
// }

// Actions (setup) {
CLASS.addAction = function(func, text, hotkey) {
  // Create the function (attach it to this object)
  // Return the control created (button or menu option)
  if(typeof(func) == "function")
    globalFunc = globalCall(this, func);
  else // An array, of the form (func, arg1, arg2, ...)
    globalFunc = globalCall.apply(null, [this].concat(func));

  // Create the hotkey
  if(hotkey)
    this.hotkeyMap[hotkey] = globalFunc;

  // Create a button
  /*if(text) {
    var el = createElement("input");
    el.type = "button";
    el.value = text;
    el.onclick = globalFunc;
    this.actionsPanel.appendChild(el);
    return el;
  }*/

  // Add to drop-down menu
  if(text) {
    var opt = new Option(text + (hotkey ? " [" + hotkey + "]" : ""));
    var self = this;
    opt.action = globalFunc;
    this.actionsMenu.appendChild(opt);
    return opt;
  }
}

CLASS.doSelectedAction = function() {
  // Execute the selected action on the drop-down box
  var opt = this.actionsMenu.options[this.actionsMenu.selectedIndex];
  if(opt && opt.action)
    opt.action();
  // Done - lose focus (doesn't work when we have popped up a dialog box)
  this.selectActionsMenu(false);
}

CLASS.selectActionsMenu = function(b) {
  // b is whether to focus or blur
  this.actionsMenu.selectedIndex = 0;
  var t = this;
  if(b) { // Modified to work with Google Chrome
    var m = this.actionsMenu;
    this.actionsMenu.focus();
    this.actionsMenu.onkeydown = function(event) {
      var key = eventToHotkey(event);
      if(key == "return") m.blur();
      else if (key == "escape") m.blur();
      // Still allow event to go through
    }
  }
  else
    this.actionsMenu.blur();
}
// }

// Accessors {
CLASS.urcornerCell = function()          { return this.table.rows[this.ROW_CURSOR].cells[this.COL_CURSOR]; }
CLASS.itemToRow  = function(item)        { return this.table.rows[item+this.ITEM_OFFSET]; }
CLASS.rowToCell  = function(row, field)  { return row.cells[field+this.FIELD_OFFSET]; }
CLASS.itemCol    = function(item, col)   { return this.table.rows[item+this.ITEM_OFFSET].cells[col]; }
CLASS.itemField  = function(item, field) {
  var row = this.itemToRow(item);
  return row && this.rowToCell(row, field);
}
CLASS.currCell   = function()            { return this.itemField(this.currItem, this.currField); }
CLASS.itemName  = function(item)  { return this.itemToRow(item).getAttribute("itemName"); }
CLASS.fieldName = function(field) { return this.fieldToHeader(field).getAttribute("fieldName"); }
CLASS.fieldToHeader = function(field) { return this.rowToCell(this.table.rows[this.ROW_HEADER], field); }
CLASS.fieldToCursor = function(field) { return this.rowToCell(this.table.rows[this.ROW_CURSOR], field); }
CLASS.cellToRow    = function(cell)  { return cell.parentNode; }
CLASS.cellToHeader = function(cell)  {
  row = this.cellToRow(cell);
  for(var field = 0; field < this.numFields; field++)
    if(this.rowToCell(row, field) == cell)
      return this.fieldToHeader(field);
  return null;
}
CLASS.nameToItem = function(name) {
  for(var item = 0; item < this.numItems; item++)
    if(this.itemName(item) == name)
      return item;
  return null;
}

CLASS.getCheckedItemRows = function() {
  var items = new Array();
  for(var item = 0; item < this.numItems; item++) {
    if(this.isItemChecked(item))
      add(items, this.itemToRow(item));
  }
  return items;
}
CLASS.getCheckedItemNames = function() {
  var items = new Array();
  for(var item = 0; item < this.numItems; item++) {
    if(this.isItemChecked(item))
      add(items, this.itemName(item));
  }
  return items;
}
CLASS.getAllItemNames = function() {
  var items = new Array();
  for(var item = 0; item < this.numItems; item++)
    add(items, this.itemName(item));
  return items;
}
// }

// Refresh the table display {
CLASS.makeItemIndex = function() {
  // Should call this function whenever the order of items change
  this.numItems = this.table.rows.length - this.ITEM_OFFSET;
  for(var item = 0; item < this.numItems; item++) {
    this.itemToRow(item).item = item;
    this.itemCol(item, this.COL_CURSOR).onclick = globalCall(this, this.setCurrItemOrOpen, item);
    this.itemCol(item, this.COL_CHECKBOX).onclick = globalCall(this, this.updateCheckedItem, item);
    this.updateCheckedItem(item);
    this.updateCursorItem(item, this.currItem == item);
  }
}
CLASS.makeFieldIndex = function() {
  // Should call this function whenever order of fields change
  for(var field = 0; field < this.numFields; field++) {
    this.fieldToHeader(field).field = field;
    this.fieldToCursor(field).onclick = globalCall(this, this.setCurrField, field);
  }
}
CLASS.refresh = function() {
  this.makeItemIndex();
  this.makeFieldIndex();
  this.setCurrItem(this.currItem);
  this.setCurrField(this.currField);
}
// }

// Set, manipulate checked items, fields {
CLASS.isItemChecked = function(item) {
  return this.itemCol(item, this.COL_CHECKBOX).firstChild.checked;
}
CLASS.updateCheckedItem = function(item) {
  setBgColor(this.itemToRow(item),
    this.isItemChecked(item) ? checkedColor : null);
}
CLASS.updateCursorItem = function(item, b) {
  this.itemCol(item, this.COL_CURSOR).innerHTML = b ? '<img src="images/row-arrow.gif">' : "";
}
CLASS.updateCursorField = function(field, b) {
  this.fieldToCursor(field).innerHTML = b ? '<img src="images/col-arrow.gif">' : "";
}
CLASS.updateCursorCell = function(item, field, b) {
  var cell = this.itemField(item, field);
  if(cell) setBgColor(cell, b ? cursorColor : null);
}

CLASS.setCurrItem = function(newItem) {
  if(this.numItems == 0) return;
  if(newItem < 0) newItem = 0;
  if(newItem >= this.numItems) newItem = this.numItems-1;
  this.updateCursorItem(this.currItem, false);
  this.updateCursorItem(newItem, true);
  this.updateCursorCell(this.currItem, this.currField, false);
  this.updateCursorCell(newItem, this.currField, true);
  this.currItem = newItem;
  keepCtrlInView(this.currCell(), this.MARGIN);
}
CLASS.setCurrItemOrOpen = function(newItem) {
  // For clicking
  if(this.currItem == newItem) // Open if already selected
    this.openCurrItem("inline")
  else
    this.setCurrItem(newItem);
}

CLASS.setCurrField = function(newField) {
  if(this.numFields == 0) return;
  if(newField < 0) newField = 0;
  if(newField >= this.numFields) newField = this.numFields-1;
  this.updateCursorField(this.currField, false);
  this.updateCursorField(newField, true);
  this.updateCursorCell(this.currItem, this.currField, false);
  this.updateCursorCell(this.currItem, newField, true);
  this.currField = newField;
  keepCtrlInView(this.currCell(), this.MARGIN);
}

CLASS.setCurrItemField = function(cell) {
  // Change currItem and currField when click cell
  // These values may have changed over time
  var item = this.cellToRow(cell).item;
  var field = this.cellToHeader(cell).field;
  this.setCurrItem(item);
  this.setCurrField(field);
  this.block.select();
}

CLASS.setCheckedItem = function(item, b) {
  this.itemCol(item, this.COL_CHECKBOX).firstChild.checked = b;
  this.updateCheckedItem(item);
}
CLASS.toggleCheckedItem = function(item) {
  if(item < 0 || item >= this.numItems) return;
  toggleChecked(this.itemCol(item, this.COL_CHECKBOX).firstChild);
  this.updateCheckedItem(item);
}

CLASS.uncheckAllItems = function() {
  for(var item = 0; item < this.numItems; item++) {
    setChecked(this.itemCol(item, this.COL_CHECKBOX).firstChild, false);
    this.updateCheckedItem(item);
  }
}
// }

CLASS.moveCheckedItems = function(destItem) {
  if(this.numItems == 0) return;
  if(destItem < 0) destItem = 0;
  if(destItem >= this.numItems) destItem = this.numItems-1;
  // Move all checked items to current position (insert before current item)
  var destRow = this.itemToRow(destItem);
  var srcRows = this.getCheckedItemRows();
  for(var i = 0; i < srcRows.length; i++)
    insertBefore(srcRows[i], destRow);
  this.currItem = destItem;
  this.makeItemIndex();
}

// Operate on current item or field {
CLASS.moveCurrItem = function(newItem) {
  if(this.numItems == 0) return;
  if(newItem < 0) newItem = 0;
  if(newItem >= this.numItems) newItem = this.numItems-1;
  var currRow = this.itemToRow(this.currItem);
  if(newItem < this.currItem) insertBefore(currRow, this.itemToRow(newItem));
  else                        insertAfter(currRow, this.itemToRow(newItem));
  this.currItem = newItem;
  this.makeItemIndex();
}

CLASS.moveCurrField = function(newField) {
  if(this.numFields == 0) return;
  if(newField < 0) newField = 0;
  if(newField >= this.numFields) newField = this.numFields-1;
  // Swap the columns for each row
  for(var r = 0; r < this.table.rows.length; r++) {
    var row = this.table.rows[r];
    var cell = this.rowToCell(row, this.currField);
    //var obj = row;
    if(newField < this.currField) insertBefore(cell, this.rowToCell(row, newField));
    else                          insertAfter(cell, this.rowToCell(row, newField));
  }
  this.currField = newField;
  this.makeFieldIndex();
}

CLASS.toggleShowCurrField = function() {
  this.toggleShowField(this.currField);
}
CLASS.toggleShowField = function(field) {
  for(var r = 1; r < this.table.rows.length; r++) {
    var row = this.table.rows[r];
    var cell = this.rowToCell(row, field);
    if(cell.saveInnerHTML) {
      cell.innerHTML = cell.saveInnerHTML;
      cell.saveInnerHTML = null;
    }
    else {
      cell.saveInnerHTML = cell.innerHTML;
      cell.innerHTML = "";
    }
  }
}

CLASS.searchInCurrField = function() {
  var query = prompt("Search query: ");
  if(!query) return;
  var field = this.currField;

  // Find matches
  var matches = new Array();
  for(var item = 0; item < this.numItems; item++) {
    var cell = this.itemField(item, field);
    if(cell.innerHTML.match(query))
      matches[matches.length] = this.itemToRow(item);
  }

  // Move the matching ones to the beginning
  for(var i = matches.length-1; i >= 0; i--) {
    insertBefore(matches[i], this.table.rows[this.ITEM_OFFSET]);
  }
  // Highlight them
  for(var item = 0; item < this.numItems; item++)
    this.setCheckedItem(item, item < matches.length); 

  // If there are any, move cursor to the top
  if(matches.length > 0) {
    this.makeItemIndex();
    this.setCurrItem(0);
  }
}

CLASS.sortByCurrField = function(decreasing) {
  var field = this.currField;

  // Get items from table
  var numeric = this.fieldToHeader(field).getAttribute("numeric") != null;
  var triples = new Array(this.numItems); // list of (comparison key, original index, data) triples

  // Get rows to sort (if some checked, just do the checked ones; otherwise, sort them all)
  var rows = this.getCheckedItemRows();
  if(rows.length == 0) { // Use
    for(var item = 0; item < this.numItems; item++)
      add(rows, this.itemToRow(item));
  }

  for(var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var cell = this.rowToCell(row, field);
    var cmpKey = cell.getAttribute("cmpKey") || cell.innerHTML;
    if(numeric) cmpKey = parseFloat(cmpKey);
    triples[i] = new Array(cmpKey, i, row);
  }

  /*for(var i = 0; i < this.numItems; i++) {
    var row = this.itemToRow(i);
    var cell = this.rowToCell(row, field);
    var cmpKey = cell.getAttribute("cmpKey") || cell.innerHTML;
    if(numeric) cmpKey = parseFloat(cmpKey);
    triples[i] = new Array(cmpKey, i, row);
  }*/

  // Sort by the key, break ties with i (stable sort)
  triples.sort(function(p1, p2) {
    var cmp = (p1[0] < p2[0] ? -1 : (p1[0] > p2[0] ? 1 : (p1[1] < p2[1] ? -1 : 1)));
    return decreasing ? -cmp : cmp});

  // Put back in table
  var parentNode = this.table.rows[0].parentNode;
  for(var i = 0; i < this.numItems; i++)
    parentNode.appendChild(triples[i][2]);
  // TODO: when move rows around, cursors and shaded cells are not refreshed properly; fix this

  this.makeItemIndex();
}

CLASS.openCurrItem = function(showType) {
  this.openItem(this.itemToRow(this.currItem), showType);
}
// }

// Actions {
CLASS.doRemoveCheckedItems = function() {
  this.removeItemNames(this.getCheckedItemNames());
}

CLASS.doCollectCheckedItems = function() {
  this.showMsg(verbatim(this.getCheckedItemNames().join(" ")));
}

CLASS.doPrintAggregateStats = function() {
  // Each item contains a sequence of tracks, separated by ';'
  // For each track, compute statistics
  var msg = "";
  for (var t = 0; ; t++) {
    var sum0 = 0;
    var sum1 = 0;
    var sum2 = 0;
    var min = 1e100;
    var max = -1e100;
    var field = this.currField;
    for(var item = 0; item < this.numItems; item++) {
      if(this.isItemChecked(item)) {
        var row = this.itemToRow(item);
        var cell = this.rowToCell(row, field);
        var x = cell.getAttribute("cmpKey") || cell.innerHTML;
        x = parseFloat(x.split(";")[t]);
        if (!isNaN(x)) {
          sum0 += 1;
          sum1 += x;
          sum2 += x*x;
          min = Math.min(min, x);
          max = Math.max(max, x);
        }
      }
    }
    if (sum0 == 0) break; // No more entries
    var mean = sum1/sum0;
    var stddev = Math.sqrt(sum2/sum0 - mean*mean);
    msg += min + " / " + mean.toFixed(3) + "~" + stddev.toFixed(3) + " / " + max + " (" + sum0 + ")\n";
  }
  this.showMsg(verbatim(msg));
}

CLASS.doShowSource = function() {
  // Show source in another window
  var win = window.open("about:blank");
  var source = document.body.innerHTML;
  win.document.body.innerHTML = verbatim(source);
}

CLASS.doHelp = function() {
  var msg = "";
  var itemGloss = this.itemToRow(this.currItem).getAttribute("gloss");
  var fieldGloss = this.fieldToHeader(this.currField).getAttribute("gloss");
  msg += "Current item: " + this.itemName(this.currItem);
  if(itemGloss) msg += " ("+itemGloss+")";
  msg += "<br>";
  msg += "Current field: " + this.fieldName(this.currField);
  if(fieldGloss) msg += " ("+fieldGloss+")";
  msg += "<br>";
  msg += "Press 'E' or double-click cell to edit.<br>";
  this.showMsg(msg);
}
// }

// Operations on generic items, fields, cells {
CLASS.removeItemNames = function(itemNames) {
  for(var i = 0; i < itemNames.length; i++) {
    var item = this.nameToItem(itemNames[i]);
    if(item != null)
      removeElement(this.itemToRow(item));
  }
  this.currItem = 0;
  this.makeItemIndex();
}

CLASS.startEditCell = function(cell) {
  if(!this.getSaveRequest) {
    this.showError("Saving not supported");
    return;
  }
  if(!cell.mutable) {
    this.showError("Cell is not mutable");
    return;
  }
  if(cell.editing) {
    this.showError("Already being edited");
    return;
  }

  var value = cell.innerHTML;
  cell.innerHTML = "";
  cell.saveInnerHTML = value;

  // Input box
  var input = createElement(cell.multiline ? "textarea" : "input"); 
  if(cell.multiline) {
    input.rows = 10; // TODO: adapt to size
    input.cols = 60;
  }
  input.value = cell.multiline ? value.replace(/<br>/g, "\n") : value;
  this.tempDisableHotKeysOnFocus(input);
  cell.appendChild(input);
  if(cell.multiline)
    cell.appendChild(createElement("br"));

  // Save
  var saveButton = createElement("input");
  saveButton.type = "button";
  saveButton.value = "Save";
  saveButton.onclick = globalCall(this, this.endEditCell, cell, true);
  cell.appendChild(saveButton);

  // Cancel
  var cancelButton = createElement("input");
  cancelButton.type = "button";
  cancelButton.value = "Cancel";
  cancelButton.onclick = globalCall(this, this.endEditCell, cell, false);
  cell.appendChild(cancelButton);

  // Hit enter to save
  //input.onkeypress = function(event)
  input.onkeydown = function(event) {
    var key = eventToHotkey(event);
    if(key == (cell.multiline ? "cltr-m" : "return")) { // Ctrl-enter or enter
      saveButton.focus();
      saveButton.onclick(); // Save it!
    }
    else if(key == "escape") { // Escape
      cancelButton.focus();
      cancelButton.onclick(); // Save it!
    }
    else if(key == "cltr-e") { // Toggle boolean (doesn't work in Chrome)
      if(input.value == "true")
        input.value = "false";
      else if(input.value == "false" || input.value == "")
        input.value = "true";
    }
  }

  cell.editing = true;
  input.focus();
}

CLASS.endEditCell = function(cell, save) {
  var self = this;
  function morphCell(text, msg) {
    cell.innerHTML = (text != null) ? text : cell.saveInnerHTML;
    cell.editing = false;
    if(msg) self.showMsg(msg);
    return text != null;
  }

  if(!save) return morphCell(null, "Canceled save");

  // Save new value
  var value = cell.firstChild.value; // Get the contents of the input box
  value = value.replace(/\n/g, "<br>");
  value = value.replace(/\\t/g, "\t"); // How you can type tabs

  var request = this.getSaveRequest(cell, value);
  function respHandler(resp) {
    if(resp.success == "true")
      morphCell(value, null);
    else
      cell.firstChild.focus();
  }
  this.sendRequest(request, respHandler);
}

CLASS.openItem = function(row, showType) {
  if(!this.getOpenMetaRequests) {
    this.showError("Open not supported");
    return;
  }

  // Three values of showType: inline, newBlock, newWindow
  // These are mere suggestions, which map to actual placement of data
  // (see ItemTS)
  var metaRequests = this.getOpenMetaRequests(row, showType);
  if(metaRequests == null) return;
  for(var i = 0; i < metaRequests.length; i++) {
    var metaRequest = metaRequests[i];
    this.sendMetaRequest(metaRequest);
  }
}
// }

CLASS.sendMetaRequest = function(metaRequest) {
  if(metaRequest.type == "block")
    metaRequest.block.reload(metaRequest.request, metaRequest.focus); // Assume stateConstructor already filled in
  else if(metaRequest.type == "msgPanel")
    this.sendRequest(metaRequest.request);
  else if(metaRequest.type == "dataPanel")
    this.sendDataRequest(metaRequest.request);
  else if(metaRequest.type == "newWindow")
    window.open(addURLParamsObj(metaRequest.request)); // Open in new window
}

// Request and response {
CLASS.sendRequest = function(request, respHandler) {
  var self = this;
  var handler = function(req) {
    var text = req.responseText;
    // When get reply, put it in the message panel
    // responseText is always UTF-8, which means that if the server
    // sends us something else, we screw up
    // Would like to use responseBody, but is not supported apparently
    self.showMsg(verbatim(text));
    centerCtrl(self.msgPanel);
    if(respHandler)
      respHandler(self.parseResponse(text));
  }
  return this.sendRequestHelper(request, handler);
}

CLASS.sendDataRequest = function(request) {
  var self = this;
  var handler = function(req) {
    self.dataPanel.innerHTML = req.responseText;
    centerCtrl(self.dataPanel);
  }
  return this.sendRequestHelper(request, handler);
}

CLASS.sendRequestHelper = function(request, handler) {
  // Open connection and send request
  url = baseURL();
  var conn = new XHConn();
  if(conn && conn.connect(url, "GET", requestStr(request), handler)) {
    return true;
  }
  else {
    this.showError("Request failed");
    return false;
  }
}

CLASS.parseResponse = function(str) {
  // The response string consists of a sequence of lines,
  // each line with a key-value pair, separated by a single tab
  var lines = str.split(/\r?\n/);
  var response = new Object();
  for(var i = 0; i < lines.length; i++) {
    var s = lines[i];
    var j = s.indexOf("\t");
    if(j == -1) continue;
    var key = s.substring(0, j);
    var value = s.substring(j+1);
    response[key] = value;
    //this.dbg(key + " = " + value + " (" + value.length + ")");
  }
  return response;
}
// }

CLASS.onKeyPress = function(event) {
  // Return whether this event was handled
  if(!this.useHotKeys) return false;
  var hotkey = eventToHotkey(event); 

  // Add to number argument
  if(parseInt(hotkey) >= 0 && parseInt(hotkey) <= 9) {
    this.numArgBuf += hotkey;
    return true;
  }

  // Get hotkey mapping
  var func = this.hotkeyMap[hotkey];
  if(func) { func(); return true; }

  var d = parseInt(this.numArgBuf) || 1;
  var e = parseInt(this.numArgBuf) || this.numItems;

  // Could move these into the hotkey mapping (but they would pollute the menu)
       if(hotkey == "shift-e") { this.startEditCell(this.currCell()); }  // Edit current cell
  else if(hotkey == "shift-k") { this.moveCurrItem(this.currItem-d); }   // Move item up
  else if(hotkey == "shift-j") { this.moveCurrItem(this.currItem+d); }   // Move item down
  else if(hotkey == "shift-h") { this.moveCurrField(this.currField-d); } // Move field left
  else if(hotkey == "shift-l") { this.moveCurrField(this.currField+d); } // Move field right
  else if(hotkey == "shift-g") { this.setCurrItem(e-1); }
  else if(hotkey == "shift-m") { this.moveCheckedItems(this.currItem); } // Move to current
  else if(hotkey == "shift-x") { this.uncheckAllItems(); }
  else if(hotkey == "k") { this.setCurrItem(this.currItem-d); }
  else if(hotkey == "j") { this.setCurrItem(this.currItem+d); }
  else if(hotkey == "h") { this.setCurrField(this.currField-d); }
  else if(hotkey == "l") { this.setCurrField(this.currField+d); }
  else if(hotkey == "x") {
    for(var item = this.currItem; item < this.currItem+d; item++)
      this.toggleCheckedItem(item);
  }
  else if(hotkey == "a") { this.selectActionsMenu(true); }
  else return false;

  this.numArgBuf = ""; // Reset number argument
  return true;
}

CLASS.saveSettings = function() {
  var settings = new Object();
  settings.currItem = this.currItem;
  settings.currField = this.currField;
  settings.msgPanelText = this.msgPanel.innerHTML;
  settings.hiddenFields = new Array();
  for(var field = 0; field < this.numFields; field++) {
    var cell = this.fieldToHeader(field);
    if(cell.saveInnerHTML) // Hidden
      add(settings.hiddenFields, field);
  }
  return settings;
}

CLASS.restoreSettings = function(settings) {
  this.setCurrItem(settings.currItem);
  this.setCurrField(settings.currField);
  this.msgPanel.innerHTML = settings.msgPanelText;
  for(var i = 0; i < settings.hiddenFields.length; i++) {
    var field = settings.hiddenFields[i];
    this.toggleShowField(field);
  }
}

// Hot keys {
CLASS.setUseHotKeys = function(b) {
  this.useHotKeys = b;
  var tag = is(this.toggleHotKeysButton, "HTMLOptionElement") ? "text" : "value";
  this.toggleHotKeysButton[tag] = this.useHotKeysStr();
}
CLASS.toggleUseHotKeys = function() {
  this.setUseHotKeys(!this.useHotKeys);
}
CLASS.useHotKeysStr = function() {
  return this.useHotKeys ? "Disable hotkeys" : "Enable hotkeys";
}
CLASS.setTempUseHotKeys = function(b) {
  this.block.blockSet.useHotKeys = b;
}
CLASS.tempDisableHotKeysOnFocus = function(node) {
  node.onfocus = globalCall(this, this.setTempUseHotKeys, false);
  node.onblur = globalCall(this, this.setTempUseHotKeys, true);
}
// }
