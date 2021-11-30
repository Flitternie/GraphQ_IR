package fig.basic;

import java.io.*;
import java.lang.reflect.Method;
import java.util.*;

/**
 * The logging output has a tree structure, where each node is a
 * line of output, and the depth of a node is its indent level.
 * A run is the sequence of children of some node.
 * A subset of the lines in the run will get printed.
 */
public class LogInfo {
  // Either in main mode.
  // List of LogInfos, one for each thread.
  private static ThreadLogInfo mainInfo;
  private static List<ThreadLogInfo> threadInfos = null;

  // Wrapped versions of the usual stdin/stdout/stderr.
  public static BufferedReader stdin;
  public static PrintWriter stdout, stderr;
  private static PrintWriter out, fileOut;  // Where to output stuff

  public static StopWatch watch;  // StopWatch that starts at the beginning of the program
  public static int numErrors;    // Number of errors
  public static int numWarnings;  // Number of warnings

  public static StopWatch getWatch() { return watch; }
  public static int getNumErrors() { return numErrors; }
  public static int getNumWarnings() { return numWarnings; }

  // Return an instance to use.
  private static ThreadLogInfo getInfo() {
    if (mainInfo == null)
      mainInfo = new ThreadLogInfo(out, fileOut);

    // Not in thread mode
    if (threadInfos == null) return mainInfo;

    Thread currentThread = Thread.currentThread();
    synchronized (threadInfos) {
      for (ThreadLogInfo info : threadInfos) {
        if (info.getThread() == currentThread) return info;
      }
      // Doesn't exist - add a new LogInfo
      ThreadLogInfo info = new ThreadLogInfo(mainInfo);
      threadInfos.add(info);
      return info;
    }
  }

  // Get the current indent level.  Useful if we throw an exception after
  // indenting several times, and we want to restore the indent level.
  public static int getIndLevel() { return getInfo().getIndLevel(); }

  public static void begin_threads() {
    if (threadInfos != null) throw new RuntimeException("Already in thread mode");
    mainInfo.flush();
    threadInfos = new ArrayList<ThreadLogInfo>();
  }

  public static void end_threads() {
    if (threadInfos == null) throw new RuntimeException("Not in thread mode");
    for (ThreadLogInfo info : threadInfos)
      info.flush();
    threadInfos = null;
  }

  public static void flush() {
    if (threadInfos != null) {
      for (ThreadLogInfo info : threadInfos)
        info.flush();
    }
    mainInfo.flush();
  }

  // Call the appropriate ThreadLogInfo.
  public static void begin_track(String format, Object... args) { getInfo().begin_track(format, args); }
  public static void begin_track_printAll(String format, Object... args) { getInfo().begin_track_printAll(format, args); }
  public static void begin_track_general(Object o, boolean printAllChildLines, boolean printIfParentPrinted) { getInfo().begin_track_general(o, printAllChildLines, printIfParentPrinted); }
  public static void end_track() { getInfo().end_track(); }
  public static <T> T end_track(T x) { return getInfo().end_track(x); }
  public static void log(Object o) { getInfo().log(o); }
  public static void logs(String format, Object... args) { getInfo().logs(format, args); }
  public static void dbgs(String format, Object... args) { getInfo().dbgs(format, args); }
  public static void dbg(Object o) { getInfo().dbg(o); }
  public static void errors(String format, Object... args) { getInfo().errors(format, args); }
  public static void error(Object o) { getInfo().error(o); }
  public static void warnings(String format, Object... args) { getInfo().warnings(format, args); }
  public static void warning(Object o) { getInfo().warning(o); }
  public static void fails(String format, Object... args) { getInfo().fails(format, args); }
  public static void fail(Object o) { getInfo().fail(o); }

  public static void logsForce(String format, Object...args) { getInfo().logsForce(format, args); }
  public static void logsForce(Object o) { getInfo().logsForce(o); }
  public static void logss(String format, Object... args) { getInfo().logss(format, args); }
  public static void logss(Object o) { getInfo().logss(o); }

  public static void updateStdStreams() {
    try {
      stdin  = CharEncUtils.getReader(System.in);
      stdout = CharEncUtils.getWriter(System.out);
      stderr = CharEncUtils.getWriter(System.err);
    } catch(IOException e) {
      throw new RuntimeException(e);
    }
  }

  // Initialize no matter what.
  static {
    updateStdStreams();
    watch = new StopWatch();
    watch.start();
    out = stdout;  // Default
  }

  // Called explicitly after command-line options are set.
  public static void init() {
    // Write to file, stdout?
    if (!file.equals("")) {
      fileOut = IOUtils.openOutHard(file);
    } else {
      fileOut = null;
    }
    if (writeToStdout) {
      out = stdout;
    } else {
      out = null;
    }
  }

  // This is dangerous, but useful when we want to redirect log output to
  // various places in the middle of an Execution.
  public static void setFileOut(PrintWriter newFileOut) {
    flush();
    if (threadInfos != null) {
      for (ThreadLogInfo info : threadInfos)
        info.setFileOut(newFileOut);
    }
    mainInfo.setFileOut(newFileOut);
    fileOut = newFileOut;
  }
  public static PrintWriter getFileOut() { return fileOut; }

  //////////////////////////////////////////////////////////// 

  // Options
  @Option(gloss="Maximum indent level.")
    public static int maxIndLevel = Integer.MAX_VALUE;
  @Option(gloss="Maximum number of milliseconds between consecutive lines of output.")
    public static int msPerLine = 0;
  @Option(gloss="File to write log.")
    public static String file = "";
  @Option(gloss="Whether to output to the console.", name="stdout")
    public static boolean writeToStdout = true;
  @Option(gloss="Dummy placeholder for a comment")
    static public String note = "";
  @Option(gloss="Maximum number of errors (via error()) to print")
  	static public int maxPrintErrors = 10000;
  @Option(gloss="Maximum number of warnings (via warning()) to print")
  	static public int maxPrintWarnings = 10000;
}

class ThreadLogInfo {
  // Private state.
  private PrintWriter out, fileOut;  // Where to output stuff
  private boolean buffered;       // Whether we buffer everything that's printed, and only displaying it when flush() is called.
  private int indLevel;           // Current indent level.
  private int stoppedIndLevel;    // At what level did we stop printing
  private int flushLevel;         // When get back to this level, print

  private Thread thread;          // Thread associated with this Run
  private StringBuilder buf;      // The buffer to be flushed out the next time logs is called.
  private ArrayList<LogRun> runs; // Indent level -> state

  // Default setup
  public ThreadLogInfo(PrintWriter out, PrintWriter fileOut) {
    this.out = out;
    this.fileOut = fileOut;
    this.buffered = false;
    this.indLevel = 0;
    this.stoppedIndLevel = -1;
    this.flushLevel = -1;
    initBasic();
  }

  public ThreadLogInfo(ThreadLogInfo info) {
    this.out = info.out;
    this.fileOut = info.fileOut;
    this.buffered = true;
    this.indLevel = info.indLevel;
    this.stoppedIndLevel = info.stoppedIndLevel;
    this.flushLevel = info.indLevel;
    initBasic();
  }

  private void initBasic() {
    this.thread = Thread.currentThread();
    this.buf = new StringBuilder();
    this.runs = new ArrayList<LogRun>(128);
    for (int i = 0; i < 128; i++)
      runs.add(new LogRun());
  }

  public Thread getThread() { return thread; }

  public int getIndLevel() { return indLevel; }

  public void setFileOut(PrintWriter newFileOut) { this.fileOut = newFileOut; }

  public void begin_track(String format, Object... args) {
    begin_track_general(String.format(format, args), false, false);
  }
  public void begin_track_printAll(String format, Object... args) {
    begin_track_general(String.format(format, args), true, false);
  }
  public synchronized void begin_track_general(Object o,
      boolean printAllChildLines, boolean printIfParentPrinted) {
    if (indWithin()) {
      if (printIfParentPrinted && parentPrinted()) thisRun().forcePrint();
      if (thisRun().shouldPrint()) {
        print(o);
        buf.append(" {\n"); // Open the block.

        childRun().init();
        childRun().printAllLines = printAllChildLines;
      }
      else {
        stoppedIndLevel = indLevel;
      }
    }

    indLevel++;
  }

  public synchronized void end_track() {
    if (indLevel == 0) {
      throw new RuntimeException("Already at indLevel = 0, can't decrement (you probably have too many end_track's)");
    }
    indLevel--;

    if (stoppedIndLevel == indLevel) {
      stoppedIndLevel = -1;
    }

    if (indWithin()) {
      if (thisRun().newLine()) { // Note that we pay for the line only at the end
        // Finish up child level.
        indLevel++;
        int n = thisRun().numOmitted();
        if (n > 0)
          print("... " + n + " lines omitted ...\n");
        indLevel--;
        childRun().finish();

        //System.out.println("BUF '" + buf + "'");
        if (childRun().numLines == 0 && buf.length() > 0) // Nothing was printed.
          buf.delete(buf.length() - " {".length(), buf.length()); // Just pretend we didn't open the block.
        else // Something indented was printed.
          print("}"); // Close the block.

        // Print time
        StopWatch ct = childRun().watch;
        if (ct.ms > 1000) {
          rawPrint(" [" + ct);
          if (indLevel > 0) {
            StopWatch tt = thisRun().watch;
            rawPrint(", cum. " + new StopWatch(tt.getCurrTimeLong()));
          }
          rawPrint("]");
        }
        rawPrint("\n");
      }
    }

    if (indLevel == flushLevel)
      flush();
  }

  // Convenient way to end and return a value
  public <T> T end_track(T x) { end_track(); return x; }

  // Normal printing
  public void logs(String format, Object... args) {
    log(String.format(format, args));
  }
  public void log(Object o) {
    if (indWithin() && thisRun().newLine())
      printLines(o);
  }
  
  // Always print
  public void logsForce(String format, Object...args) {
    printLines(String.format(format, args));
  }
  public void logsForce(Object o) {
    thisRun().newLine();
    printLines(o);
  }
  
  // Print if parent printed
  public void logss(String format, Object... args) {
    logss(String.format(format, args));
  }
  public void logss(Object o) {
    if (parentPrinted()) thisRun().forcePrint();
    log(o);
  }
  private boolean parentPrinted() {
    // Parent must have been a track, so its run information has not been
    // updated yet.  Therefore, shouldPrint() is valid.
    return indLevel == 0 ||
      (stoppedIndLevel == -1 && indLevel <= LogInfo.maxIndLevel && parentIndWithin() && parentRun().shouldPrint());
  }

  // Log different types of information
  public void dbgs(String format, Object... args) { dbg(String.format(format, args)); }
  public void dbg(Object o) { logs("DBG: " + o); }
  public void errors(String format, Object... args) { error(String.format(format, args)); }
  public void error(Object o) { if (LogInfo.numErrors++ < LogInfo.maxPrintErrors) print("ERROR: " + o + "\n"); }
  public void warnings(String format, Object... args) { warning(String.format(format, args)); }
  public void warning(Object o) { if (LogInfo.numWarnings++ < LogInfo.maxPrintWarnings) print("WARNING: " + o + "\n"); }
  public void fails(String format, Object... args) { fail(String.format(format, args)); }
  public void fail(Object o) { throw Exceptions.bad(o); }

  // Print random things
  public void printProgStatus() {
    logs("PROG_STATUS: time = " + LogInfo.watch.stop() + ", memory = " + SysInfoUtils.getUsedMemoryStr());
  }
  public <T> void printList(String s, String lines) {
    printList(s, Arrays.asList(lines.split("\n")));
  }
  public <T> void printList(String s, List<T> items) {
    LogInfo.begin_track_printAll(s);
    for (T x : items) log(x);
    LogInfo.end_track();
  }

  private LogRun parentRun() { return runs.get(indLevel-1); }
  private LogRun thisRun()   { return runs.get(indLevel); }
  private LogRun childRun()  { return runs.get(indLevel+1); }

  // If we were to print a new line, should we print?
  private boolean indWithin()       { return indLevel   <= LogInfo.maxIndLevel; }
  private boolean parentIndWithin() { return indLevel-1 <= LogInfo.maxIndLevel; }

  // buf -> output
  public void flush() {
    //System.out.println("FLUSH " + buf);
    if (out != null) { out.print(buf); out.flush(); }
    if (fileOut != null) { fileOut.print(buf); fileOut.flush(); }
    buf.delete(0, buf.length());
  }

  private void rawPrint(Object o) {
    if (buffered) { buf.append(o); return; }
    flush();
    if (out != null) { out.print(o); out.flush(); }
    if (fileOut != null) { fileOut.print(o); fileOut.flush(); }
  }

  // Print with indent; flush the buffer as necessary
  private void print(Object o) {
    for (int i = 0; i < indLevel; i++) rawPrint("  ");
    rawPrint(o);
  }
  // If there are new lines, put indents before them
  private void printLines(Object o) {
    if (o == null) o = "null";
    String s = StrUtils.toString(o);
    if (s.indexOf('\n') == -1)
      print(s+"\n");
    else
      for (String t : StrUtils.split(s, "\n")) print(t+"\n");
  }
}

/**
 * A run is a sequence of lines of text, some of which are printed.
 * Stores the state associated with a run.
 */
class LogRun {
  public LogRun() {
    watch = new StopWatch();
    init();
  }
  void init() {
    numLines = 0;
    numLinesPrinted = 0;
    nextLineToPrint = 0;
    printAllLines = false;
    watch.reset();
    watch.start();
  }
  void finish() {
    // Make it clear that this run is not printed.
    // Otherwise, logss might think its
    // parent was printed when it really wasn't.
    nextLineToPrint = -1;
    watch.stop();
  }

  void forcePrint() { forcePrint = true; }
  boolean shouldPrint() { return forcePrint || nextLineToPrint == numLines; }
  int numOmitted() { return numLines - numLinesPrinted; }

  /**
   * Decide whether to print the next line.  If yes,
   * then you must print it.
   * @return Whether the next line should be printed.
   */
  boolean newLine() {
    boolean p = shouldPrint();
    numLines++;
    if (!p) return false; // Assume forcePrint == false
    
    // Ok, we're going to print this line.
    numLinesPrinted++;

    // Decide next line to print.
    int msPerLine = LogInfo.msPerLine;
    if (numLines <= 2  || // Print first few lines anyway.
       msPerLine == 0 || // Print everything.
       printAllLines  || // Print every line in this run (by fiat).
       forcePrint)       // Force-printed things shouldn't affect timing.
      nextLineToPrint++;
    else {
      long elapsed_ms = watch.getCurrTimeLong();
      if (elapsed_ms == 0) { // No time has elapsed.  
        // This usually applies in the beginning of a run when we have
        // no idea how long things are going to take
        nextLineToPrint *= 2; // Exponentially increase time between lines.
      }
      else // Try to maintain the number of lines per second.
        nextLineToPrint += (int)Math.max((double)numLines * msPerLine / elapsed_ms, 1);
    }
    forcePrint = false;

    return true;
  }

  int numLines;           // Number of lines that we've gone through so far in this run.
  int numLinesPrinted;    // Number of lines actually printed.
  int nextLineToPrint;    // Next line to be printed (lines are 0-based).
  StopWatch watch;        // Keeps track of time spent on this run.
  boolean printAllLines;  // Whether or not to force the printing of each line.
  boolean forcePrint;     // Whether to print out the next item (is reset afterwards).
}
