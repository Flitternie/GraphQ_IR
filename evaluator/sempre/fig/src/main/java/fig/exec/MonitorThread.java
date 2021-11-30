package fig.exec;

import java.io.*;
import java.util.*;
import java.lang.Thread;
import fig.basic.*;
import static fig.basic.LogInfo.*;

/**
 * A separate thread that's responsible for outputting the status
 * of this execution and reading in commands.
 * The thread is actually contained inside.
 */
class MonitorThread implements Runnable {
  private static final int timeInterval = 300; // Number of milliseconds between monitoring
  private boolean stop;
  private Thread thread;
  private Thread mainThread;

  public MonitorThread() {
    this.stop = false;
    this.thread = new Thread(this);
    this.mainThread = Thread.currentThread();
  }

  String lastCmd = null;
  void processCommand(String cmd) {
    cmd = cmd.trim();
    if(cmd.equals("")) cmd = lastCmd;

    if(cmd == null) ;
    else if(cmd.equals("status")) {
      // Print status
      Execution.getInfo().print(stderr);
      Execution.printOutputMapToStderr();
      MapUtils.print(StopWatchSet.getStats(), stderr);
      stderr.println(Execution.getActualExecDir());
    }
    else if(cmd.equals("kill")) {
      stderr.println("MonitorThread: KILLING");
      Execution.setExecStatus("killed", true);
      Execution.printOutputMap(Execution.getFile("output.map"));
      Execution.beforeExit();
      throw new RuntimeException("Killed by input command");
    }
    else if (cmd.startsWith("stack")) {
      String[] tokens = cmd.split(" ");
      for (Map.Entry<Thread, StackTraceElement[]> e : Thread.getAllStackTraces().entrySet()) {
        Thread thread = e.getKey();
        //Thread thread = mainThread;
        StackTraceElement[] trace = e.getValue();
        //StackTraceElement[] trace = mainThread.getStackTrace();
        if (tokens.length == 2) {
          int n = Integer.parseInt(tokens[1]);
          trace = Arrays.copyOf(trace, Math.min(n, trace.length));
        }
        System.out.println("==== STACK TRACE FOR THREAD " + thread + "====");
        System.out.println(StrUtils.join(trace, "\n"));
      }
    }
    else if(cmd.equals("bail")) {
      // Up to program to look at this flag and actually gracefully stop
      stderr.println("MonitorThread: BAILING OUT");
      Execution.shouldBail = true;
    }
    else
      stderr.println("Invalid command: '" + cmd + "'");
    lastCmd = cmd;
  }

  void readAndProcessCommand() {
    try {
      int nBytes = System.in.available();
      if(nBytes > 0) {
        byte[] bytes = new byte[nBytes];
        System.in.read(bytes);
        String line = new String(bytes);
        processCommand(line);
      }
    } catch(IOException e) {
      // Ignore
    }
  }

  public void run() {
    try {
      while(!stop) {
        if(LogInfo.writeToStdout)
          readAndProcessCommand();

        // Input commands
        Execution.inputMap.readEasy(Execution.getFile("input.map"));

        boolean killed = Execution.getActualExecDir() != null && new File(Execution.getFile("kill")).exists();
        if(killed) Execution.setExecStatus("killed", true);

        // Output status
        Execution.putOutput("log.note", LogInfo.note);
        Execution.putOutput("exec.memory", SysInfoUtils.getUsedMemoryStr());
        Execution.putOutput("exec.time", new StopWatch(LogInfo.getWatch().getCurrTimeLong()).toString());
        Execution.putOutput("exec.errors", "" + LogInfo.getNumErrors());
        Execution.putOutput("exec.warnings", "" + LogInfo.getNumWarnings());
        Execution.setExecStatus("running", false);
        Execution.printOutputMap(Execution.getFile("output.map"));

        if(killed) {
          Execution.beforeExit();
          throw new RuntimeException("Killed by 'kill' file");
        }

        Utils.sleep(timeInterval);
      }
    } catch(Exception e) {
      e.printStackTrace();
      System.exit(1); // Die completely
    }
  }

  public void start() {
    thread.start();
  }

  public void finish() {
    stop = true;
    thread.interrupt();
  }
}
