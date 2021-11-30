function BlockSet(blockType) {
  this.blocks = new Array();
  this.blockType = blockType;
  this.currIndex = 0;
  this.useHotKeys = true;

  // HACK: get focus onto something on the page so we can use keyboard shortcuts
  var dummy = createElement("a");
  insertBefore(dummy, document.body.firstChild);
  dummy.focus();
  
  this.addAllBlocks(document.body);
  this.setCurrIndex(this.currIndex);
}

var CLASS = BlockSet.prototype;

CLASS.currBlock = function() { return this.blocks[this.currIndex]; }

CLASS.addBlock = function(block, refBlock) {
  // Insert block after refBlock
  if(!block) return;
  var i = refBlock ? indexOf(this.blocks, refBlock) : -1;
  if(i == -1)
    add(this.blocks, block);
  else
    this.blocks.splice(i+1, 0, block);
  return block;
}

CLASS.findBlock = function(name) {
  for(var i = 0; i < this.blocks.length; i++)
    if(this.blocks[i].name == name) return this.blocks[i];
  return null;
}

CLASS.getBlock = function(type, recycle, block) {
  if(!type) type = "unknown";

  // If recycle, return the block of the given type
  // If such block doesn't exist, create it
  if(recycle) {
    // Find existing one
    for(var i = 0; i < this.blocks.length; i++)
      if(this.blocks[i].type == type)
        return this.blocks[i];
  }

  // Create a new one
  for(var q = 0; ; q++) {
    var name = type+(q?q:"");
    if(!this.findBlock(name)) {
      if(!block) block = lastInArray(this.blocks);
      var blockDiv = this.createBlockDivAfter(type, name, block);
      return this.addBlock(new this.blockType(this, blockDiv), block);
    }
  }
}

CLASS.createBlockDivAfter = function(type, name, block) {
  // Create a block div after the given block's
  var blockDiv = createDiv();
  blockDiv.setAttribute("id", name+".block");
  blockDiv.setAttribute("type", type);
  insertManyAfter([createElement("p"), blockDiv], block.blockDiv);
  return blockDiv;
}

CLASS.addAllBlocks = function(node) {
  // Find all the blocks under node
  for(var childNode = node.firstChild; childNode; childNode = childNode.nextSibling) {
    if(!Block.isBlock(childNode)) continue;
    var block = new this.blockType(this, childNode);
    block.prepare();
    this.addBlock(block);
  }
}

CLASS.setCurrIndex = function(newIndex) {
  //alert(newIndex + " " + this.currIndex + " " + this.blocks.length);
  if(newIndex < 0 || newIndex >= this.blocks.length) return;
  this.blocks[this.currIndex].setSelected(false);
  this.blocks[newIndex].setSelected(true);
  this.currIndex = newIndex;
}

// View the beginning of the current block
CLASS.viewBeginCurrBlock = function() {
  keepCtrlInView(this.currBlock().blockDiv, 0);
}

CLASS.setCurrBlock = function(block) {
  for(var i = 0; i < this.blocks.length; i++)
    if(this.blocks[i] == block) { this.setCurrIndex(i); return; }
}

CLASS.removeCurrBlock = function() {
  this.removeBlock(this.currBlock());
}

CLASS.removeBlock = function(block) {
  if(!block) return;
  block.die();
  var index = indexOf(this.blocks, block);
  this.blocks = removeAt(this.blocks, index);
  this.currIndex = min(this.blocks.length-1, this.currIndex);
  this.setCurrIndex(this.currIndex);
}

CLASS.onKeyPress = function(event) {
  if(!this.useHotKeys) return false;
  var hotkey = eventToHotkey(event);
       if(hotkey == "ctrl-f")       { this.setCurrIndex(this.currIndex+1); return true; }
  else if(hotkey == "ctrl-b")       { this.setCurrIndex(this.currIndex-1); return true; }
  else if(hotkey == "ctrl-shift-d") { this.removeCurrBlock(); return true; }
  else if(this.currBlock()) {
    return this.currBlock().onKeyPress(event); // Dispatch to current block
  }
  this.viewBeginCurrBlock();
}
