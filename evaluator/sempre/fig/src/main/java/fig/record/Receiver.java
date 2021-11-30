package fig.record;

import java.io.*;

/**
 * What the client should do.
 * Need to run rmic on this class.
 */
public class Receiver implements ReceiverInterface {
  private String baseTempDir;
  private PrintWriter out, err;

  public Receiver(String baseTempDir, PrintWriter out, PrintWriter err) {
    this.baseTempDir = baseTempDir;
    this.out = out;
    this.err = err;
  }

  public void printOut(String s) { out.print(s); out.flush(); }
  public void printErr(String s) { err.print(s); err.flush(); }

  public void executeMandate(Mandate mandate) {
    if(!new File(baseTempDir).exists())
      new File(baseTempDir).mkdir();
    mandate.execute(baseTempDir);
  }

  // Take the the stuff collected by the result receiver
  // and process it as if this receiver got it.
  public void addResult(ResultReceiver result) {
    printOut(result.getOut());
    printErr(result.getErr());
    executeMandate(result.getMandate());
  }

  // Nothing to do
  public void flush() { }
}
