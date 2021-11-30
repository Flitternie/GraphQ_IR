package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

public class ExecItem extends Item {
  private static final int runningTimeoutMs = 5*60*1000; // 5 minutes: just for display
  private static final int hardRunningTimeoutMs = 30*60*1000; // 30 minutes: treat execution as lost

  // Whether it has been purged
  private boolean isDead;
  // Whether its fields have been updated for the first time yet;
  // Used to prioritize updating of exec items and
  // used to mark something as immutable.
  public boolean hasUpdated;
  // If true, don't update again once we've updated.
  public boolean immutable;
  private FileKeyMap fileKeyMap;

  public boolean isDead() { return isDead; }

  public ExecItem(Item parent, String name, String sourcePath) {
    super(parent, name, sourcePath);
    this.fileKeyMap = new FileKeyMap(sourcePath);
  }

  protected Value getIntrinsicFieldValue(String fieldName) throws MyException {
    if(fieldName.equals("sinceLastModified")) return getSinceLastModifiedTimeValue();
    String value = fileKeyMap.get(fieldName);
    if (value != null) return new Value(value);
    return super.getIntrinsicFieldValue(fieldName);
  }
  protected void changeIntrinsicFieldValue(String fieldName, String value) throws MyException {
    if(fileKeyMap.put(fieldName, value)) return;
    super.changeIntrinsicFieldValue(fieldName, value);
  }

  public static Value getSinceLastModifiedTimeValue(long lastModifiedTime) {
    long time = getSinceLastModifiedTime(lastModifiedTime);
    return new Value(new StopWatch(time).toString(), ""+time);
  }

  public static long getSinceLastModifiedTime(long lastModifiedTime) { return new Date().getTime() - lastModifiedTime; }

  public Value getSinceLastModifiedTimeValue() throws MyException {
    long lastModified = new File(sourcePath, "output.map").lastModified();
    Value value = getSinceLastModifiedTimeValue(lastModified);
    // Put an asterisk if the program hasn't responded in a while and the
    // program status is running; in this case the program probably just died
    if(isRunning() && getSinceLastModifiedTime(lastModified) >= runningTimeoutMs)
      return new Value(value.value+"*", value.cmpKey);
    return value;
  }

  private long getSinceLastModifiedTime() {
    long lastModified = new File(sourcePath, "output.map").lastModified();
    return getSinceLastModifiedTime(lastModified);
  }

  public boolean isRunning() {
    // If status is null, then that counts as running too, presumably because
    // we haven't loaded the status yet.  But the file says the execution is
    // running but we haven't heard back from it for a long time, assume that
    // the execution died, and this doesn't constitute running.
    String status = getStatus();
    return status == null || ("running".equals(status) && getSinceLastModifiedTime() < hardRunningTimeoutMs);
  }
  public boolean isThunk() { return "thunk".equals(getStatus()); }
  public String getStatus() { return fileKeyMap.get("output.map:exec.status"); }

  protected FieldListMap getMetadataFields() {
    return createDefaultFields();
  }

  public static FieldListMap createDefaultFields() {
    FieldListMap fields = new FieldListMap();
    fields.add("info.map:Host", "host",                "Host on which this execution happened").processor = new ValueProcessor("s/\\..*/");
    fields.add("info.map:Date", "date",                "When the execution began").processor = new ValueProcessor("DATE");
    fields.add("sinceLastModified", "last",            "Time since last modification").numeric = true;
    fields.add("output.map:exec.disk", "disk",         "Disk usage").numeric = true;
    fields.add("output.map:exec.memory", "mem",        "Memory usage").numeric = true;
    fields.add("output.map:exec.time", "time",         "Execution time").numeric = true;
    fields.add("numErrorsAndWarnings", "err",          "Number of LogInfo warnings/errors", new Object[] {"$output.map:exec.errors", ",", "$output.map:exec.warnings"}).setNumeric(true).processor = new ValueProcessor("s/^,$//");
    fields.add("output.map:exec.status", "status",     "Program status").mutable = true;
    fields.add("options.map:exec.miscOptions", "opts", "Miscellaneous options").setMutable(true).rank = 2;
    fields.add("options.map:log.note", "note",         "Notes/comments about the execution").setMutable(true).rank = 10;
    return fields;
  }
  public static FieldListMap createThunkFields() {
    FieldListMap fields = new FieldListMap();
    fields.add("job.map:priority", "priority", "Priority (lower the better)").setMutable(true).setNumeric(true);
    fields.add("job.map:nice", "nice", "Nice value to run the command").setMutable(true).setNumeric(true);
    fields.add("job.map:workingDir", "workingDir", "The current directory that the command is run").mutable = true;
    fields.add("job.map:reqMemory", "reqMemory", "Amount of memory required (MB)").setNumeric(true).setMutable(true);
    fields.add("job.map:command", "command", "Notes/comments about the execution").setMutable(true);
    return fields;
  }
  // For thunks
  protected int getPriority() { return Utils.parseIntEasy(fileKeyMap.get("job.map:priority"), 0); }
  protected int getReqMemory() { return Utils.parseIntEasy(fileKeyMap.get("job.map:reqMemory"), 0); }
  protected int getNice() { return Utils.parseIntEasy(fileKeyMap.get("job.map:nice"), 0); }
  protected String getWorkingDir() { return fileKeyMap.get("job.map:workingDir"); }
  protected String getCommand() { return fileKeyMap.get("job.map:command"); }

  public void update(UpdateSpec spec, UpdateQueue.Priority priority) throws MyException {
    if(isDead) return; // No sense in updating if we're dead
    // If we're immutable, then don't update if we've already updated
    if(immutable && hasUpdated) return;

    // Update
    fileKeyMap.clear(); // Will force update later
    immutable = !isRunning() && !isThunk(); // Don't update if not running anymore
    hasUpdated = true;
    super.update(spec, priority);
  }

  public void kill() throws MyException {
    // Just create a file called "kill" in the execution directory.
    if(!IOUtils.createNewFileEasy(new File(sourcePath, "kill").toString()))
      throw new MyException("Unable to kill " + name + " by creating a kill file");
  }

  public ResponseObject handleOperation(OperationRP req, Permissions perm) throws MyException {
    String op = req.op;
    if(op.equals("kill")) {
      kill();
      return new ResponseParams("Killed " + name);
    }
    if(op.equals("reload")) {
      immutable = false; // Make it mutable, so next time it will be updated
      return new ResponseParams("Reloading " + name);
    }
    return super.handleOperation(req, perm);
  }

  protected boolean isView() { return false; }
  public Item newItem(String name) throws MyException { throw MyExceptions.unsupported; }
}
