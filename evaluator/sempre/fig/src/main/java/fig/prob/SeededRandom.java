package fig.prob;

/**
 * Because `java.util.Random` doesn't have `getSeed()`.
 *
 * Typical usage:
 * - Have a master SeededRandom instance in your program, which logs
 *   it seed to some log file.
 * - Every other Random seeds itself from the master and also log its
 *   seed (see `nextRandom()`).
 * - These Randoms should all have names (and possibly log their seeds
 *   as well to a log file).
 */
public class SeededRandom extends java.util.Random {
  private long seed;

  public SeededRandom() { super(); }
  public SeededRandom(long seed) { super(seed); }

  public long getSeed() {
    return seed;
  }

  @Override
  public void setSeed(long seed) {
    this.seed = seed;
    super.setSeed(seed);
  }

  public SeededRandom nextRandom() {
    return new SeededRandom(nextLong());
  }
}
