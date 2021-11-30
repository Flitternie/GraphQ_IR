package fig.record;

import fig.basic.*;
import java.io.*;
import java.util.*;
import java.rmi.*;
import java.rmi.server.*;

public class RecordServer extends UnicastRemoteObject implements RecordServerInterface {
  public static class Options {
    @Option(gloss="The root directory.")
      public String rootPath = ".";
    @Option(gloss="Command files to process.")
      public ArrayList<String> commandFiles = new ArrayList<String>();
    @Option(gloss="Temporary directory")
      public String baseTempDir = "tmp";
    @Option(gloss="Identifier of this record server instance.", required=true)
      public String id;
  }

  private RecordNode root;
  private GlobalEnv globalEnv;

  public RecordServer(String rootPath) throws RemoteException {
    this.root = new FullRecordNode(null, null);
    this.globalEnv = new GlobalEnv(root);

    // Root directory
    this.root.addChild(PathRecordNode.newPathNode(null,
          globalEnv.getLoadFileState(), rootPath));
    // TODO: create a hash table record node that we can store to
  }

  public String getPrompt() throws RemoteException {
    //return globalEnv.getCurrRecord().getPathString();
    return "> ";
  }

  public ResultReceiver processCommand(String line, ReceiverInterface receiver) throws RemoteException {
    if(StrUtils.isEmpty(line)) return null;

    // If using a callback, buffer it;
    // Otherwise, we create our new receiver right now and return it later.
    boolean useCallback = (receiver != null);
    if(useCallback)
      receiver = new BufferedReceiver(receiver);
    else
      receiver = new ResultReceiver();

    CommandEnv cmdEnv = new CommandEnv(globalEnv, receiver);

    // Parse the command
    CommandNode cmd = CommandUtils.parse(line, cmdEnv);
    if(cmd == null) return null;

    // Print out the command
    if(globalEnv.verbose(2)) {
      try {
        RecordNodeUtils.sendRecordNodetoReceiver(
          new TwigRecordNode(null, null, cmd), cmdEnv.getReceiver());
      } catch(Exception e) { throw new RuntimeException(e); }
    }

    // Execute the command
    RecordNode result = cmd.exec(new LocalCommandEnv(cmdEnv));
    // Send the results back
    RecordNodeUtils.sendRecordNodetoReceiver(result, receiver);

    cmdEnv.sendMandateToReceiver();
    cmdEnv.finish();

    receiver.flush();
    // Return the result receiver if we're not using callbacks
    return useCallback ? null : (ResultReceiver)receiver;
  }

  public static void main(String[] args) {
    Options options = new Options();
    if(!new OptionsParser().register("main", options).parse(args)) return;

    try {
      RecordServer server = new RecordServer(options.rootPath);
      new CommandProcessor(server, options.baseTempDir,
          false, false).processCommandFiles(options.commandFiles);
      Naming.rebind("RecordServer/"+options.id, server);
    } catch(Throwable t) {
      t.printStackTrace();
    }
  }
}
