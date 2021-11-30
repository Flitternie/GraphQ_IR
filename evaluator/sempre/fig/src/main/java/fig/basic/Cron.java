package fig.basic;

/**
 * A useful class for doing a periodic task by polling to see if it's time.
 * At the same time, keep track of total time elapsed.
 */
public class Cron {
  private long intervalMS;
  private StopWatch intervalWatch;
  private StopWatch totalWatch;

  public Cron(long intervalMS) {
    this.intervalMS = intervalMS; 
    this.intervalWatch = new StopWatch().start();
    this.totalWatch = new StopWatch().start();
  }
  public static Cron eachSeconds(double secs) { return new Cron((int)(secs*1000)); }

  /**
   * Return true iff intervalMS has ellapsed since
   * the last call to hasReached() (or the constructor).
   */
  public boolean hasReached() {
    if(intervalWatch.stop().ms > intervalMS) {
      this.intervalWatch.start(); // Start time again
      return true;
    }
    return false;
  }

  public int intervalSecs() { return (int)(intervalMS/1000); }

  public long totalMS() { return totalWatch.stop().ms; }
  public int totalSecs() { return (int)(totalMS()/1000); }
}
