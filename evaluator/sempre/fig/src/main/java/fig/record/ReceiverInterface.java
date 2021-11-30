package fig.record;

import java.rmi.*;

/**
 * What the server will use to make callbacks to the client receiver.
 */
public interface ReceiverInterface extends Remote {
  public void printOut(String s) throws RemoteException;
  public void printErr(String s) throws RemoteException;
  public void executeMandate(Mandate mandate) throws RemoteException;
  public void flush() throws RemoteException;
}
