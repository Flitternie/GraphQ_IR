inheritClass(ExecsBlock, Block);
function ExecsBlock(blockSet, blockDiv) {
  Block.call(this, blockSet, blockDiv);
}
var CLASS = ExecsBlock.prototype;
CLASS.getStateConstructor = function(type) {
  if(type == "FileView") return FileViewTS;
  if(type == "ExecView") return ExecViewTS;
  if(type == "WorkerView") return WorkerViewTS;
  return ItemTS;
}

////////////////////////////////////////////////////////////

var blockSet;
function onLoad() { blockSet = new BlockSet(ExecsBlock); }
function onKeyPress(event) {
  if(blockSet.onKeyPress(event)) { // If processed
    event.returnValue = false; // IE
    event.preventDefault(); // Dom 2
    return false; // Netscape
  }
}
