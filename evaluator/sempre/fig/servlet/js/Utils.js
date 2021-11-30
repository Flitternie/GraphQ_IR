////////////////////////////////////////////////////////////
// Utilities

// General operations {
function is(o, c) { return o.toString() == "[object " + c + "]"; }
function isDefined(o) { return typeof(o) != "undefined"; }
function min(a, b) { return a < b ? a : b; }
function max(a, b) { return a > b ? a : b; }
function swap(data, i, j) { var tmp = data[i]; data[i] = data[j]; data[j] = tmp; }
function isValidFileName(name) { return name.match(/^[a-zA-Z0-9\-\._]+$/); }

function lastInArray(arr) { return arr[arr.length-1]; }

function inheritClass(subclass, superclass) {
  subclass.prototype = cloneObj(superclass.prototype);
  //subclass.prototype.superclass = superclass.prototype;
  //subclass.prototype.base = superclass;
}

function popup(msg) { if(!confirm(msg)) throw "User canceled: " + msg; }

function verbatim(text) {
  text = text.replace(/</g, "&lt;");
  text = text.replace(/>/g, "&gt;");
  return "<pre>" + text + "</pre>";
}

function slice(arr, i, j) {
  // We have this because function.arguments does not the slice function
  if(i < 0) i = 0;
  if(!isDefined(j)) j = arr.length;
  if(j < 0) j += arr.length;
  if(j < 0) i = 0;
  if(j > arr.length) j = arr.length;
  var subArr = new Array(j-i);
  for(var k = i; k < j; k++)
    subArr[k-i] = arr[k];
  return subArr;
}

function indexOf(arr, x) {
  for(var i = 0; i < arr.length; i++)
    if(arr[i] == x) return i;
  return -1;
}

function removeAt(arr, j) {
  var newArr = new Array();
  for(var i = 0; i < arr.length; i++)
    if(i != j) add(newArr, arr[i]);
  return newArr;
}

function globalCall(self, func) {
  // Create a closure function that calls the specified function and arguments
  // using self
  // Typical usage: button.onclick = globalCall(this, this.Func, arg1, arg2);
  var args = slice(globalCall.arguments, 2);
  return function() { return func.apply(self, args); }
}
// }

// Collections utilities {
function add(l, x) { l[l.length] = x; }

function cloneObj(x) {
  var y = new Object();
  return clobberObj(x, y);
}
function clobberObj(x, y) { // x clobbers y
  if(x) for(var a in x) y[a] = x[a];
  return y;
}

function newObj() {
  return addToObj.apply(null, [new Object()].concat(newObj.arguments));
}

function addToObj(obj) {
  // Arguments: (obj, key1, value1, key2, value2, ...)
  // Return: new object
  // Does not modify current object
  var newObj = cloneObj(obj);
  var args = addToObj.arguments;
  for(var i = 1; i+1 < args.length; i += 2) {
    var key = args[i];
    var value = args[i+1];
    newObj[key] = value;
  }
  return newObj;
}
// }

// HTML operations {
function get(s) { return document.getElementById(s); }
function getReq(s) {
  var o = document.getElementById(s);
  if(!o) throw "Element " + s + " doesn't exist";
  return o;
}
function getAttrReq(node, key) {
  var value = node.getAttribute(key);
  if(!value) throw "Element '" + node + "' missing attribute " + key;
  return value;
}
function toggleChecked(o) { o.checked = !o.checked; }
function setChecked(o, b) { o.checked = b; }
function setBgColor(o, color) { o.style.backgroundColor = color; }

// Put text in a div.
function showtext(loc, s) { get(loc).innerHTML = s; }
function hidetext(loc)    { showtext(loc, ''); }

function offsetLeft(el) {
  y = el.offsetLeft;
  for (e = el.offsetParent; e; e = e.offsetParent)
    y += e.offsetLeft;
  return y;
}
function offsetTop(el) {
  y = el.offsetTop;
  for (e = el.offsetParent; e; e = e.offsetParent)
    y += e.offsetTop;
  return y;
}
function scrollToCtrl(ctrl) {
  if(!ctrl) return;
  window.scrollTo(window.pageXOffset, offsetTop(ctrl));
}
function centerCtrl(ctrl) {
  if(!ctrl) return;
  window.scrollTo(window.pageXOffset, offsetTop(ctrl) - window.innerHeight/2);
}
function keepCtrlInView(ctrl, margin) {
  if(!ctrl) return;
  var pageMinX = window.pageXOffset;
  var pageMaxX = pageMinX + window.innerWidth;
  var ctrlMinX = offsetLeft(ctrl);
  var ctrlMaxX = ctrlMinX + ctrl.offsetWidth;

  var pageMinY = window.pageYOffset;
  var pageMaxY = pageMinY + window.innerHeight;
  var ctrlMinY = offsetTop(ctrl);
  var ctrlMaxY = ctrlMinY; // + ctrl.offsetHeight; // Don't care about vertical end of control

  //alert(pageMin + "-" + pageMax + " " + ctrlMin + "-" + ctrlMax);
  var x = window.pageXOffset, y = window.pageYOffset;
       if(ctrlMinX < pageMinX) x = ctrlMinX - margin;
  else if(ctrlMaxX > pageMaxX) x = ctrlMaxX + margin;
       if(ctrlMinY < pageMinY) y = ctrlMinY - margin;
  else if(ctrlMaxY > pageMaxY) y = ctrlMaxY + margin;
  window.scrollTo(x, y);
}

function friendlyStr(key) {
  if(key == 27) return "escape";
  if(key == 13) return "return";
  return String.fromCharCode(key).toLowerCase();
}
function eventToHotkey(event) {
  // Hotkey is a string of form [ctrl-][shift-]<key> (everything is lowercase)
  // Note: in Safari, the character code is actually A=1, B=2, ...
  // We are using Firefox.
  var key = event.charCode || event.keyCode;
  var hotkey = "";
  if(event.ctrlKey) hotkey += "-ctrl";
  if(event.shiftKey) hotkey += "-shift";
  hotkey += "-" + friendlyStr(key);
  hotkey = hotkey.substring(1);
  return hotkey;
}
// }

// DOM operations {
function createElement() {
  var args = createElement.arguments;
  var tag = args[0];
  var el = document.createElement(tag);
  for(var i = 1; i+1 < args.length; i += 2)
    el[args[i]] = args[i+1];
  return el;
}
function createDiv(text) {
  var el = createElement("div");
  if(text) el.innerHTML = text;
  return el;
}
function createHidden() {
  var el = createElement("input");
  el.type = "hidden";
  return el;
}

function insertBefore(newNode, currNode) {
  currNode.parentNode.insertBefore(newNode, currNode);
}
function insertAfter(newNode, currNode) {
  //alert(newNode + " " + currNode);
  var parentNode = currNode.parentNode;
  if(parentNode.lastChild == currNode)
    parentNode.appendChild(newNode);
  else
    parentNode.insertBefore(newNode, currNode.nextSibling);
}
function insertManyAfter(newNodes, currNode) {
  for(var i = 0; i < newNodes.length; i++) {
    insertAfter(newNodes[i], currNode);
    currNode = newNodes[i];
  }
}

function removeElement(node) {
  node.parentNode.removeChild(node);
}
function removeAllChildren(node) {
  while(node.childNodes.length > 0)
    node.removeChild(node.firstChild);
}

function replaceCtrlWithHTML(ctrl, html) {
  ctrl.innerHTML = html; // Replace ctrl's innards
  var newCtrl = ctrl.firstChild;
  insertBefore(newCtrl, ctrl); // Rip the innards out
  removeElement(ctrl); // Kill ctrl
  return newCtrl;
}
// }

// URL operations {
function baseURL() {
  var url = window.location;
  return "http://" + url.host + url.pathname;
}

function getURLParams(url) {
  if(!url) url = window.location;
  // Extract GET parameters from url and return a hash table
  url = url.toString();
  var tokens = url.split(/[\?&]/);
  //alert(url + " " + tokens.length);
  var ht = new Object();
  for(var i = 1; i < tokens.length; i++) {
    var keyValue = tokens[i].split("=");
    //alert(keyValue[0] + " = " + keyValue[1]);
    ht[keyValue[0]] = keyValue[1];
  }
  return ht;
}

function addURLParams(useExisting) {
  var params = useExisting ? getURLParams(window.location) : new Object();
  var args = addURLParams.arguments;
  for(var i = 1; i+1 < args.length; i += 2) {
    var key = args[i];
    var value = args[i+1];
    params[key] = value;
  }
  params = requestStr(params);
  return baseURL() + (params ? "?"+params : "");
}

function addURLParamsObj(params) {
  // Not using existing params
  params = requestStr(params);
  return baseURL() + (params ? "?"+params : "");
}

function escapeStr(s) {
  // In addition, need this
  return escape(s).replace(/\+/g, "%2B");
}

function requestStr(r) {
  // r is an object
  var s = "";
  for(var x in r) {
    if(s.length > 0) s += "&";
    s += escapeStr(x) + "=" + escapeStr(r[x]);
  }
  return s;
}
// }
