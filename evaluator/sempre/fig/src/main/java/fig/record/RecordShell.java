package fig.record;

import fig.basic.*;
import fig.exec.*;
import static fig.basic.LogInfo.stdin;
import static fig.basic.LogInfo.stdout;
import static fig.basic.LogInfo.stderr;
import java.io.*;
import java.util.*;
import java.rmi.*;
import java.rmi.server.*;

public class RecordShell {
  public static class Options {
    @Option(gloss="Hostname of record server.")
      public String serverHost = "localhost";
    @Option(gloss="Local command files files to process.")
      public ArrayList<String> commandFiles = new ArrayList<String>();
    @Option(gloss="Interactive mode.")
      public boolean interactive = true;
    @Option(gloss="Temporary directory")
      public String baseTempDir = "tmp";
    @Option(gloss="Whether the client is behind a firewall")
      public boolean firewall = true;
    @Option(gloss="Identifier of the record server to connect to.", required=true)
      public String id;
  }

  private Options options;
  private RecordServerInterface server;

  public RecordShell(Options options) {
    this.options = options;
    connectToServer();
  }

  private void connectToServer() {
    try {
      this.server = (RecordServerInterface)Naming.lookup(
          "//"+options.serverHost+"/RecordServer/"+options.id);
    } catch(Exception e) {
      throw new RuntimeException(e);
    }
  }

  private static void printStackTrace(Throwable t) {
    stderr.println("EXCEPTION: " + t.getMessage());
    stderr.print(Utils.getStackTrace(t, "sun.reflect"));
    stderr.flush();
  }

  public void run() {
    // Run the script files
    new CommandProcessor(server, options.baseTempDir,
        true, options.firewall).processCommandFiles(options.commandFiles);
    if(!options.interactive) return;

    // Now run the shell loop
    IOUtils.LineMunger munger = new IOUtils.LineMunger() {
      public void beforeLine(boolean isContinuation) {
        try {
          if(isContinuation) stdout.print("... ");
          else stdout.print(server.getPrompt());
          stdout.flush();
        } catch(ConnectException e) {
          stderr.println("Connection to server lost, reconnecting...");
          connectToServer();
        } catch(Throwable t) {
          printStackTrace(t);
        }
      }
      public void afterFullLine(String line) {
        try {
          // Figure out what to do with output of the command
          String pipeCmd = null, outFile = null;
          int i;
          i = line.indexOf(" | ");
          if(i != -1) { pipeCmd = line.substring(i+3).trim(); line = line.substring(0, i); }
          i = line.indexOf(" > ");
          if(i != -1) { outFile = line.substring(i+3).trim(); line = line.substring(0, i); }

          BufferedReader in = null, err = null;
          PrintWriter out = null;
          Process proc = null;
          if(pipeCmd != null) { // Setup the pipe
            proc = Utils.openSystem("cat | " + pipeCmd);
            out = CharEncUtils.getWriter(proc.getOutputStream());
            in = CharEncUtils.getReader(proc.getInputStream());
            err = CharEncUtils.getReader(proc.getErrorStream());
          }
          else if(outFile != null) { // Set up the output file
            out = IOUtils.openOutHard(outFile);
          }
          else // Write to console
            out = stdout;

          // Run the command! (could throw exception)
          Receiver receiver = new Receiver(options.baseTempDir, out, stderr);
          new CommandProcessor(server, receiver,
              true, options.firewall).processCommand(line);

          // Output of redirected shell command to console
          if(out != stdout) out.close();
          if(proc != null) {
            IOUtils.copy(err, stderr); err.close();
            IOUtils.copy(in, stdout); in.close();
            Utils.closeSystemEasy("cat | " + pipeCmd, proc);
          }
        } catch(ConnectException e) {
          stderr.println("Connection to server lost, reconnecting...");
          connectToServer();
        } catch(Throwable t) {
          printStackTrace(t);
        }
      }
    };

    try {
      IOUtils.doProgramLines(stdin, munger);
      stdout.println("");
    } catch(IOException e) {
      throw new RuntimeException(e);
    }
  }

  public static void main(String[] args) {
    Options options = new Options();
    if(!new OptionsParser().register("main", options).parse(args)) return;

    try {
      RecordShell shell = new RecordShell(options);
      shell.run();
    } catch(Throwable t) {
      printStackTrace(t);
    }
  }
}
