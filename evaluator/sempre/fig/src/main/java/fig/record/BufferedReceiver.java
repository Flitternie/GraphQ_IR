package fig.record;

import java.io.*;
import java.rmi.*;

/**
 * Getting output back to the client is expensive if we have to
 * make so many RMI calls, so use a buffer for the standard output.
 */
public class BufferedReceiver implements ReceiverInterface {
  private ReceiverInterface receiver;
  private StringBuilder sb;

  public BufferedReceiver(ReceiverInterface receiver) {
    this.receiver = receiver;
    this.sb = new StringBuilder();
  }

  public void flush() throws RemoteException {
    receiver.printOut(sb.toString());
    sb = new StringBuilder();
  }

  public void printOut(String s) throws RemoteException {
    sb.append(s);
    if(sb.length() >= 16*1024) flush(); // Heuristically tuned
  }

  public void printErr(String s) throws RemoteException {
    receiver.printErr(s);
  }

  public void executeMandate(Mandate mandate) throws RemoteException {
    receiver.executeMandate(mandate);
  }
}
