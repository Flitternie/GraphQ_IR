package fig.exec;

import static fig.basic.LogInfo.begin_track_printAll;
import static fig.basic.LogInfo.end_track;
import static fig.basic.LogInfo.error;
import static fig.basic.LogInfo.logs;
import static fig.basic.LogInfo.logss;
import static fig.basic.LogInfo.stderr;
import static fig.basic.LogInfo.stdout;

import java.io.File;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import fig.basic.CharEncUtils;
import fig.basic.ClassInitializer;
import fig.basic.Exceptions;
import fig.basic.IOUtils;
import fig.basic.ListUtils;
import fig.basic.LogInfo;
import fig.basic.Option;
import fig.basic.OptionsParser;
import fig.basic.OrderedStringMap;
import fig.basic.StopWatchSet;
import fig.basic.StrUtils;
import fig.basic.SysInfoUtils;
import fig.basic.Utils;
import fig.basic.IOUtils;
import fig.basic.MapUtils;
import fig.basic.Fmt;

import fig.record.Record;

/**
 * Represents all the settings and output of an execution of a program.
 * An execution is defined by all the options registered with OptionsParser.
 * Creates a directory for the execution in the execution pool dir.
 */
public class Execution {
  @Option(gloss="Whether to create a thread to monitor the status of this execution.")
    public static boolean monitor = true;

  // How to create the execution directory
  @Option(gloss="Directory to put all output files; if empty, use execPoolDir.")
    public static String execDir;
  @Option(gloss="Directory which contains all the executions.")
    public static String execPoolDir;
  @Option(gloss="Overwrite the contents of the execDir if it doesn't exist (e.g., when running a thunk).")
    public static boolean overwriteExecDir;

  @Option(gloss="Simply print options and exit.")
    public static boolean printOptionsAndExit = false;
  @Option(gloss="Miscellaneous options (written to options.map and output.map, displayed in servlet); example: a=3 b=4")
    public static ArrayList<String> miscOptions = new ArrayList();

  @Option(gloss="Name of the view to add this execution to in the servlet (simply creates an addToView file).")
    public static ArrayList<String> addToView = new ArrayList<String>();

  @Option(gloss="Character encoding")
    public static String charEncoding;
  @Option(gloss="Name of jar files to load prior to execution.  This is so that when the JARs change underneath us, we don't crash.")
    public static ArrayList<String> jarFiles = new ArrayList<String>();
  
  // Whether to print out start a main() track (LogInfo)
  @Option(gloss="Whether to wrap everything around a main() track")
    public static boolean startMainTrack = true;

  // Execution directory that we write to (execDir is just a suggestion)
  private static String actualExecDir;
  public static String getActualExecDir() { return actualExecDir; }

  private static boolean shouldCreate() {
    return execPoolDir != null || execDir != null;
  }

  // Passed to the options parser
  public static boolean ignoreUnknownOpts = false;

  static OrderedStringMap inputMap = new OrderedStringMap(); // Accessed by monitor thread
  private static OrderedStringMap outputMap = new OrderedStringMap();
  private static OptionsParser parser;
  private static MonitorThread monitorThread; // Thread for monitoring
  static int exitCode = 0;

  static boolean shouldBail = false; // Set by monitor thread
  public static boolean shouldBail() { return shouldBail; }
  
  private static void mkdirHard(File f) {
    if(!f.mkdir()) {
      stderr.println("Cannot create directory: " + f);
      System.exit(1);
    }
  }

  /**
   * Return an unused directory in the execution pool directory.
   * Set actualExecDir
   */
  public static String createActualExecDir() {
    if(!StrUtils.isEmpty(execPoolDir) && !new File(execPoolDir).isDirectory())
      throw Exceptions.bad("Execution pool directory '" + execPoolDir + "' doesn't exist");

    if(!StrUtils.isEmpty(execDir)) { // Use specified execDir
      boolean exists = new File(execDir).isDirectory();
      if(exists && !overwriteExecDir)
        throw Exceptions.bad("Directory already exists and overwrite flag is false");
      if (!exists) mkdirHard(new File(execDir));  // Create if it doesn't exist
      return actualExecDir = execDir;
    }

    // execDir hasn't been specified, so we need to pick one from a pool directory
    // execPoolDir must exist

    // Get a list of files that already exists
    Set<String> files = new HashSet<String>();
    for(String f : new File(execPoolDir).list()) files.add(f);

    // Go through and pick out a file that doesn't exist
    int numFailures = 0;
    for (int i = 0; ; i++) {
      // Either the virtual file (a link) or the actual file
      File f = new File(execPoolDir, i+".exec");
      if (!files.contains(i+".exec")) {
        mkdirHard(f);
        return actualExecDir = f.toString();
      }
    }
  }

  // Get the path of the file (in the execution directory)
  public static String getFile(String file) {
    if(StrUtils.isEmpty(actualExecDir)) return null;
    if(StrUtils.isEmpty(file)) return null;
    return new File(actualExecDir, file).toString();
  }

  public static void linkFileToExec(String realFileName, String file) {
    if(StrUtils.isEmpty(realFileName) || StrUtils.isEmpty(file)) return;
    File f = new File(realFileName);
    Utils.createSymLink(f.getAbsolutePath(), getFile(file));
  }
  public static void linkFileFromExec(String file, String realFileName) {
    if(StrUtils.isEmpty(realFileName) || StrUtils.isEmpty(file)) return;
    File f = new File(realFileName);
    Utils.createSymLink(getFile(file), f.getAbsolutePath());
  }

  // Getting input and writing output
  public static boolean getBooleanInput(String s) {
    String t = inputMap.get(s, "0");
    return t.equals("true") || t.equals("1");
  }
  public synchronized static String getInput(String s) { return inputMap.get(s); }
  public synchronized static void putOutput(String s, Object t) { outputMap.put(s, StrUtils.toString(t)); }
  public synchronized static void printOutputMapToStderr() { outputMap.print(stderr); }
  public synchronized static void printOutputMap(String path) {
    if(StrUtils.isEmpty(path)) return;
    // First write to a temporary directory and then rename the file
    String tmpPath = path+".tmp";
    if(outputMap.printEasy(tmpPath))
      new File(tmpPath).renameTo(new File(path));
  }

  public static void setExecStatus(String newStatus, boolean override) {
    String oldStatus = outputMap.get("exec.status");
    if(oldStatus == null || oldStatus.equals("running")) override = true;
    if(override) putOutput("exec.status", newStatus);
  }

  public static void putLogRec(String key, Object value) {
    logss("%s = %s", key, value);
    Record.add(key, value);
    putOutput(key, value);
  }

  static OrderedStringMap getInfo() {
    OrderedStringMap map = new OrderedStringMap();
    map.put("Date", SysInfoUtils.getCurrentDateStr());
    map.put("Host", SysInfoUtils.getHostName());
    map.put("CPU speed", SysInfoUtils.getCPUSpeedStr());
    map.put("Max memory", SysInfoUtils.getMaxMemoryStr());
    map.put("Num CPUs", SysInfoUtils.getNumCPUs());
    return map;
  }

  public static void init(String[] args, Object... objects) {
    //// Parse options
    // If one of the objects is an OptionsParser, use that; otherwise, create a new one
    for(int i = 0; i < objects.length; i++) {
      if(objects[i] instanceof OptionsParser) {
        parser = (OptionsParser)objects[i];
        objects[i] = null;
      }
    }
    if(parser == null) parser = new OptionsParser();

    parser.register("log", LogInfo.class);
    parser.register("exec", Execution.class);
    parser.registerAll(objects);

    // These options are specific to the execution, so we don't want to overwrite them
    // with a previous execution's.
    parser.setDefaultDirFileName("options.map");
    parser.setIgnoreOptsFromFileName("options.map",
      ListUtils.newList("log.file", "exec.execDir", "exec.execPoolDir"));
    if(ignoreUnknownOpts) parser.ignoreUnknownOpts();
    if(!parser.parse(args)) System.exit(1);

    // Set character encoding
    if(charEncoding != null)
      CharEncUtils.setCharEncoding(charEncoding);

    if(printOptionsAndExit) { // Just print options and exit
      parser.getOptionPairs().print(stdout);
      System.exit(0);
    }

    // Create a new directory
    if (shouldCreate()) {
      createActualExecDir();
      LogInfo.file = getFile("log");

      // Copy the Jar files for reference
      for(String jarFile : jarFiles)
        Utils.systemHard(String.format("cp %s %s", jarFile, actualExecDir));
    }
    else {
      LogInfo.file = "";
    }

    initializeJars();

    // Handle miscOptions
    for(String opt : miscOptions) {
      String[] tokens = opt.split("=");
      if(tokens.length == 2)
        putOutput(tokens[0], tokens[1]);
    }

    LogInfo.init();
    Record.init(getFile("record"));
    if(startMainTrack) begin_track_printAll("main()");

    // Output options
    if (actualExecDir != null) logs("Execution directory: " + actualExecDir);
    getInfo().printEasy(getFile("info.map"));
    printOptions();
    if (shouldCreate() && addToView.size() > 0)
      IOUtils.printLinesHard(Execution.getFile("addToView"), addToView);

    // Start monitoring
    if (monitor) {
      monitorThread = new MonitorThread();
      monitorThread.start();
    }
  }

  // Even after we've initialized, we can still add more objects,
  // mostly for logging their options.
  public static void add(Object o) {
    parser.registerAll(new Object[] {o});
    printOptions();
  }

  private static void initializeJars() {
    if (jarFiles.size() > 0) {
      List<String> names = new ArrayList();
      for (String jarFile : jarFiles)
        names.add(new File(jarFile).getName());
      stderr.println("Loading JAR files: " + StrUtils.join(names));
      for (String jarFile : jarFiles) {
        // Load classes
        String jarPath = shouldCreate() ? new File(actualExecDir, new File(jarFile).getName()).getPath() : jarFile;
        ClassInitializer.initializeJar(jarPath);
      }
    }
  }

  // Might want to call this again after some command-line options were changed.
  public static void printOptions() {
    parser.getOptionPairs().printEasy(getFile("options.map"));
    parser.getOptionStrings().printEasy(getFile("options.help"));
  }

  public static void raiseException(Throwable t) {
    error(t + ":\n" + StrUtils.join(t.getStackTrace(), "\n"));
    t = t.getCause();
    if(t != null)
      error("Caused by " + t + ":\n" + StrUtils.join(t.getStackTrace(), "\n"));
    putOutput("exec.status", "exception");
    exitCode = 1;
  }

  public static void finish() {
    if (actualExecDir != null)
      outputMap.put("exec.disk", Fmt.bytesToString(IOUtils.diskUsageBytesUnder(actualExecDir)));

    Record.finish();

    if(monitor) monitorThread.finish();
    setExecStatus(shouldBail ? "bailed" : "done", false);
    outputMap.printEasy(getFile("output.map"));

    MapUtils.printEasy(StopWatchSet.getStats(), getFile("time.map"));

    if(actualExecDir != null) logs("Execution directory: " + actualExecDir);
    if(LogInfo.getNumErrors() > 0 || LogInfo.getNumWarnings() > 0)
      stderr.printf("%d errors, %d warnings\n",
          LogInfo.getNumErrors(), LogInfo.getNumWarnings());
    if(startMainTrack) end_track();

    System.exit(exitCode);
  }

  // This should be all we need to put in a main function.
  // args are the command-line arguments
  // First object is the Runnable object to call run on.
  // All of them are objects whose options args is to supposed to populate.
  public static void run(String[] args, Object... objects) {
	  runWithObjArray(args, objects);
  }
  
  public static void runWithObjArray(String[] args, Object[] objects)
  {
    init(args, objects);

    Object mainObj;
    if(objects[0] instanceof String) mainObj = objects[1];
    else                             mainObj = objects[0];

    try {
      ((Runnable)mainObj).run();
    } catch(Throwable t) {
      raiseException(t);
      LogInfo.flush();
    }

    finish();
  }

  // Handlers for before exiting
  public interface ExitHandler {
    public void run();
  }
  private static List<ExitHandler> exitHandlers = new ArrayList();
  public static void addExitHandler(ExitHandler handler) { exitHandlers.add(handler); }
  public static void beforeExit() {
    for(ExitHandler handler : exitHandlers) handler.run();
  }

  // Run a system command, keep track of orphans, and log the output nicely (with indents)
  public static void runSystemCommand(String header, final String cmd) {
    begin_track_printAll(header);
    logs("%s", cmd);
    try {
      final Process process = Utils.openSystem(cmd);
      addExitHandler(new ExitHandler() {
        public void run() {
          logs("KILLING PROCESS OF COMMAND: %s", cmd);
          process.destroy();
          try { process.waitFor(); }
          catch(InterruptedException e) { }
        }
      });
      process.getOutputStream().close();
      String line;

      begin_track_printAll("stdout");
      BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
      while ((line = in.readLine()) != null) logs("%s", line);
      in.close();
      end_track();

      begin_track_printAll("stderr");
      BufferedReader err = new BufferedReader(new InputStreamReader(process.getErrorStream()));
      while ((line = err.readLine()) != null) logs("%s", line);
      err.close();
      end_track();

      Utils.closeSystemHard(cmd, process);
    } catch(IOException e) {
      throw new RuntimeException(e);
    }
    end_track();
  }
}
