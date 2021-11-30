package fig.record;

import java.rmi.*;

/**
 * Local environment that's used during the execution of a command node only.
 */
public class LocalCommandEnv {
  private CommandEnv cmdEnv;
  private RecordNode currRecord; // Operate on this node
  private SubsetHint hint; // Hints on what children to keep
  private SubsetHint defaultHint; // If no hint is specified, this is what we use
  private VarBindingList varBindingList; // Variable bindings

  private LocalCommandEnv(CommandEnv cmdEnv, RecordNode currRecord,
      SubsetHint hint, SubsetHint defaultHint, VarBindingList varBindingList) {
    this.cmdEnv = cmdEnv;
    this.currRecord = currRecord;
    this.hint = hint;
    this.defaultHint = defaultHint;
    this.varBindingList = varBindingList;
  }
  public LocalCommandEnv(CommandEnv cmdEnv) {
    this(cmdEnv, cmdEnv.getGlobalEnv().getRootRecord(),
         ConstantSubsetHint.allHint, ConstantSubsetHint.allHint,
         VarBindingList.empty);
  }

  public LocalCommandEnv withCurrRecord(RecordNode currRecord) { // currRecord = NEW
    return new LocalCommandEnv(cmdEnv, currRecord, hint, defaultHint, varBindingList);
  }
  public LocalCommandEnv withHint(SubsetHint hint) { // hint = NEW
    return new LocalCommandEnv(cmdEnv, currRecord, hint, defaultHint, varBindingList);
  }
  public LocalCommandEnv withDefaultHint(SubsetHint defaultHint) { // defaultHint = NEW
    return new LocalCommandEnv(cmdEnv, currRecord, hint, defaultHint, varBindingList);
  }
  public LocalCommandEnv withHintIsDefault() { // hint = defaultHint
    return withHint(defaultHint);
  }
  public LocalCommandEnv withHintIsSame() { // hint = hint
    return this;
  }
  public LocalCommandEnv withNewBinding(String var, String val) {
    return new LocalCommandEnv(cmdEnv, currRecord, hint, defaultHint,
      varBindingList.withNewBinding(var, val));
  }
  // This is set by a command node before invoking exec() on its children,
  // so the know which child it is
  public LocalCommandEnv withIndex(int index) {
    return withNewBinding("index", ""+index);
  }
  public VarBindingList getVarBindingList() { return varBindingList; }

  public RecordNode getCurrRecord() { return currRecord; }
  public GnuPlotter getPlotter() { return cmdEnv.getPlotter(); }
  public ReceiverInterface getReceiver() { return cmdEnv.getReceiver(); }
  public CommandEnv getCmdEnv() { return cmdEnv; }
  public GlobalEnv getGlobalEnv() { return cmdEnv.getGlobalEnv(); }

  public SubsetHint getHint() { return hint; }
  public RecordNode applyHint(RecordNode record) {
    return SubsetHintUtils.applyHint(hint, record);
  }

  // Logging
  public void log(Object o) {
    try { getReceiver().printErr(o+"\n"); }
    catch(RemoteException e) { throw new RuntimeException(e); }
  }
  public void log(String fmt, Object... args) { log(String.format(fmt, args)); }
  public void dbg(Object o) { log("DBG " + o); }
  public void dbg(String fmt, Object... args) { dbg(String.format(fmt, args)); }
}
