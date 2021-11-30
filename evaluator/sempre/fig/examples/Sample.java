/*
This program which computes averages and in the process, demonstrates how fig
is used.
*/
import java.io.*;
import java.util.*;
import fig.basic.*;
import fig.exec.*;
import fig.prob.SampleUtils;

public class Sample implements Runnable {
  @Option(gloss="Number of samples") public int N = 3;
  @Option(gloss="Random seed used to draw samples") public Random random = new Random(1);

  public void run() {
    // Keep track of statistics
    StatFig stats = new StatFig();
    List<Double> samples = new ArrayList<Double>();

    LogInfo.begin_track("Simulating");
    for (int i = 0; i < N; i++) {
      double x = SampleUtils.sampleGaussian(random);
      LogInfo.logs("Sample %d: %f", i, x);
      stats.add(x);
      samples.add(x);
    }
    LogInfo.end_track();

    // Print out statistucs
    LogInfo.begin_track("Statistics");
    LogInfo.logs("Mean: %f", stats.mean());
    LogInfo.logs("Stddev: %f", stats.stddev());
    LogInfo.end_track();
    Execution.putOutput("mean", stats.mean());
    Execution.putOutput("stddev", stats.stddev());

    // Output some samples
    String path = Execution.getFile("samples");
    if (path != null) {
      PrintWriter out = IOUtils.openOutHard(path);
      for (double x : samples) out.println(x);
      out.close();
    }
  }

  public static void main(String[] args) {
    Execution.run(args, new Sample());
  }
}
