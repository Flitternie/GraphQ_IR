/**
 * A block stores a self-contained unit of information.
 * It contains the following things:
 *   - name: uniquely identifies the block
 *   - blockDiv: has id <name>.block
 *   - type: used to determine what kind of table class to create in the block
 *   - stateConstructor: used to construct states
 * When it has content:
 *   - state (via stateConstructor)
 *   - request: specifies how to reload the contents of the table
 *              (can be filled in when we reload)
 *   - TODO: a request history so we can go forward and backwards like a webbrowser
 */

function Block(blockSet, blockDiv) {
  this.blockSet = blockSet;
  this.state = null; // Set in prepare()
  this.selected = false;
  this.visible = true;

  this.setBlockDiv(blockDiv);
}

Block.isBlock = function(blockDiv) {
  if(!blockDiv) return false;
  if(!blockDiv.getAttribute) return false;
  var id = blockDiv.getAttribute("id");
  return id && id.match('^(.+)\.block$');
}

var CLASS = Block.prototype;

CLASS.setBlockDiv = function(blockDiv) {
  // Set name
  var id = getAttrReq(blockDiv, "id");
  var m = id.match('^(.+)\.block$');
  if(!m) throw "Bad block id: " + id;
  this.name = m[1];
  if(!this.name) throw "Bad name";
  this.type = getAttrReq(blockDiv, "type");
  this.stateConstructor = this.getStateConstructor(this.type);

  this.request = new Object();
  this.request.mode = "op";
  this.request.name = this.name;
  this.request.op = blockDiv.getAttribute("op");
  this.request.trail = blockDiv.getAttribute("trail");

  this.blockDiv = blockDiv;
}

// PLEASE OVERRIDE
CLASS.getStateConstructor = function(type) { return TableState; }

CLASS.prepare = function() {
  this.state = new this.stateConstructor(this.name+".table", this);
  this.setupHideShow();
  this.refresh();
  return this;
}

// If focus, grab selected
CLASS.reload = function(request, focus) {
  request = clobberObj(request, cloneObj(this.request));

  var conn = new XHConn();
  var self = this;
  function handler(req) {
    var text = req.responseText;
    var bad = req.getResponseHeader("Content-Type").match("^text/plain") ||
      text.match('Apache Tomcat'); // HACK
    if(bad) {
      // Bad: if this block hasn't been populated before, then delete it
      var block = self; // Where to display the error message
      if(self.state == null) {
        block = self.blockSet.currBlock();
        self.blockSet.removeBlock(self); // Delete it
      }
      block.showMsg(verbatim(text)); // Message (probably error)
    }
    else {
      try {
        var settings = self.state && self.state.saveSettings();
        self.setBlockDiv(replaceCtrlWithHTML(self.blockDiv, text)); // Block
        self.prepare();
        if(settings) self.state.restoreSettings(settings);
      } catch(e) {
        alert("Bad response (" + e + "): " + text);
      }
    }
    if(focus) this.blockSet.setCurrBlock(self);
  }
  if(conn && conn.connect(baseURL(), "GET", requestStr(request), handler)) {
    return true;
  }
  else {
    this.state.showErrorMsg("Cannot connect to reload");
    return false;
  }
}

CLASS.showMsg = function(msg) {
  if(this.state)
    this.state.showMsg(msg);
  else
    blockDiv.innerHTML = "<pre>" + msg + "</pre>";
}

CLASS.setupHideShow = function(id) {
  function findDivFromNode(node, inclusive) {
    if(!inclusive && node != null) node = node.nextSibling;
    while(node != null && !is(node, "HTMLDivElement"))
      node = node.nextSibling;
    return node;
  }

  this.titleDiv = findDivFromNode(this.blockDiv.firstChild, true);
  this.contentsDiv = findDivFromNode(this.titleDiv, false);
  this.hiddenNode = createHidden(); // Place to put contents when contents are hidden
  insertAfter(this.hiddenNode, this.contentsDiv);

  this.titleDiv.onclick = globalCall(this, this.toggleVisible);
  this.titleDiv.innerHTML = this.visibleStr() + " " + this.titleDiv.innerHTML;
}

CLASS.visibleStr = function() { return this.visible ? "-" : "+"; }
CLASS.setSelected = function(b) {
  this.selected = b;
  this.titleDiv.style.color = b ? "red" : "black";
}

CLASS.setVisible = function(visible, force) {
  if(!force && this.visible == visible) return;

  this.visible = visible;
  this.titleDiv.innerHTML = this.visibleStr() + this.titleDiv.innerHTML.substring(1);
  if(visible)
    insertAfter(this.hiddenNode.firstChild, this.titleDiv); // Restore contents from hidden node
  else
    this.hiddenNode.appendChild(this.contentsDiv); // Put contents in hidden node
  return this;
}
CLASS.toggleVisible = function() {
  this.setVisible(!this.visible);
}

CLASS.refresh = function() {
  this.setVisible(this.visible);
  this.setSelected(this.selected);
}

CLASS.select = function() {
  if(this == this.blockSet.currBlock) return;
  this.blockSet.setCurrBlock(this);
}

CLASS.die = function() { removeElement(this.blockDiv); }

CLASS.duplicateBlock = function() {
  var newBlock = this.createBlockNext();
  newBlock.reload(addToObj(this.request, "name", newBlock.name), true);
}

CLASS.onKeyPress = function(event) {
  var hotkey = eventToHotkey(event);
       if(hotkey == "ctrl-a")  this.toggleVisible();
  else if(hotkey == "shift-r") this.reload();
  else if(hotkey == "ctrl-d")  this.duplicateBlock();
  else if(this.visible) return this.state.onKeyPress(event);
  else return false;
  return true;
}

CLASS.createBlockNext = function() { return this.blockSet.getBlock(null, false, this); }
CLASS.createBlockEnd = function()  { return this.blockSet.getBlock(null, false); }
