package fig.record;

import java.rmi.*;

/**
 * The environment in which a command node is executed.
 * One is created per processCommand() call.
 */
public class CommandEnv {
  private GlobalEnv globalEnv;
  private GnuPlotter plotter; // Build up plots over a command.
  private ReceiverInterface receiver;
  // Cache the last reader so if we need to read the same file more than
  // once (and especially in a nearby location), we don't need to open
  // the file again and seek there.
  private OffsetReader lastReader;

  public CommandEnv(GlobalEnv globalEnv, ReceiverInterface receiver) {
    this.globalEnv = globalEnv;
    this.plotter = new GnuPlotter();
    this.receiver = receiver;
    this.lastReader = null;
    globalEnv.getLoadFileState().init(receiver);
  }
  public void finish() {
    globalEnv.getLoadFileState().finish();
  }

  public GlobalEnv getGlobalEnv() { return globalEnv; }
  public GnuPlotter getPlotter() { return plotter; }
  public ReceiverInterface getReceiver() { return receiver; }

  public void sendMandateToReceiver() {
    flushPlot();
  }

  public void flushPlot() {
    try {
      receiver.executeMandate(getPlotter().makeMandate(globalEnv.getCleanupMandate()));
    } catch(RemoteException e) {
      throw new RuntimeException(e);
    }
    getPlotter().reset();
  }
}
