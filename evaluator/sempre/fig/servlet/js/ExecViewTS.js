inheritClass(ExecViewTS, ItemTS);

function ExecViewTS(table, block) {
  ItemTS.call(this, table, block);
  this.addAction(this.doKill,         "k: Kill checked execs (creates a kill file in the exec directory)");
  this.addAction(this.doReloadItems,  "r: Force reload all execs in this view from disk");
  //this.addAction(this.doStripExtCollectCheckedItems, "c: Collect/print no-ext checked items");
}

var CLASS = ExecViewTS.prototype;

CLASS.doStripExtCollectCheckedItems = function() {
  var names = this.getCheckedItemNames();
  for(var i = 0; i < names.length; i++)
    names[i] = names[i].replace(".exec", "");
  this.showMsg(verbatim(names.join(",")));
}

CLASS.doKill = function() {
  this.sendRequestWithCheckedItems("Kill checked execs?", "kill");
}

CLASS.doReloadItems = function() {
  var request = this.newChildRequest("reload", this.getAllItemNames());
  return this.sendRequest(request, this.reloadIfSuccessHandler());
}
