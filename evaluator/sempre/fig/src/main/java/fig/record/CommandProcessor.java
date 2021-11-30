package fig.record;

import java.util.*;
import fig.basic.*;
import java.rmi.*;
import java.rmi.server.*;

/**
 * Responsible for sending some commands to the server.
 */
public class CommandProcessor {
  private RecordServerInterface server;
  private Receiver receiver;
  private boolean isClient, firewall;

  public CommandProcessor(RecordServerInterface server,
      String baseTempDir, boolean isClient, boolean firewall) {
    this.server = server;
    this.receiver = new Receiver(baseTempDir, LogInfo.stdout, LogInfo.stderr);
    this.isClient = isClient;
    this.firewall = firewall;
  }
  public CommandProcessor(RecordServerInterface server,
      Receiver receiver, boolean isClient, boolean firewall) {
    this.server = server;
    this.receiver = receiver;
    this.isClient = isClient;
    this.firewall = firewall;
  }

  public void processCommand(String line) {
    try {
      if(isClient) UnicastRemoteObject.exportObject(receiver);
      ResultReceiver result = server.processCommand(line,
        firewall ? null : receiver); // If using a firewall, no callbacks
      if(result != null) // But whatever is returned is then added to the receiver
        receiver.addResult(result);
      if(isClient) UnicastRemoteObject.unexportObject(receiver, false);
    } catch(RemoteException e) {
      throw new RuntimeException(e);
    }
  }

  public void processCommandFile(String path) {
    for(String line : IOUtils.readProgramLinesHard(path))
      processCommand(line);
  }

  public void processCommandFiles(List<String> paths) {
    for(String path : paths)
      processCommandFile(path);
  }
}
