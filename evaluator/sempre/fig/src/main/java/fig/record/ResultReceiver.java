package fig.record;

import java.io.*;
import java.rmi.*;

/**
 * When the RecordShell client is behind a firewall, we cannot use RMI
 * callbacks.  A result receiver collects the things that are normally
 * sent to a receiver.  Later, a result receiver is returned to the client
 * and then those things can be processed.
 */
public class ResultReceiver implements ReceiverInterface, Serializable {
  private static final long serialVersionUID = 42;

  private StringBuilder sbOut;
  private StringBuilder sbErr;
  private Mandate mandate;

  public ResultReceiver() {
    this.sbOut = new StringBuilder();
    this.sbErr = new StringBuilder();
    this.mandate = new Mandate(false);
  }

  public void flush() { }

  // Just patiently collect the output.
  public void printOut(String s) throws RemoteException { sbOut.append(s); }
  public void printErr(String s) throws RemoteException { sbErr.append(s); }
  public void executeMandate(Mandate mandate) throws RemoteException {
    this.mandate.addMandate(mandate);
  }

  public String getOut() { return sbOut.toString(); }
  public String getErr() { return sbErr.toString(); }
  public Mandate getMandate() { return mandate; }
}
