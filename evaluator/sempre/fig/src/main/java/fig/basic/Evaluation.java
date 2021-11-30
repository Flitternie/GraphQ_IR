package fig.basic;

import fig.basic.Fmt;
import fig.basic.LispTree;
import fig.basic.LogInfo;
import fig.basic.StatFig;
import fig.exec.Execution;

import java.util.*;

/**
 * An Evaluation measures how well the system is doing on a set of examples.
 * Formally, it is just a collection of arbitrary statistics.
 *
 * @author Percy Liang
 */
public class Evaluation {
  private List<String> names = new ArrayList<String>();
  private List<StatFig> values = new ArrayList<StatFig>();

  // Just for printing out
  private Set<String> cumulativeNames = new HashSet<String>();

  public StatFig getFig(String name) {
    int i = names.indexOf(name);
    if (i == -1)
      return null;
    return values.get(i);
  }

  // Methods to add new metrics to evaluation and aggregate evaluations.
  private StatFig getFigHard(String name) {
    int i = names.indexOf(name);
    if (i == -1) {
      i = names.size();
      names.add(name);
      values.add(new StatFig());
    }
    return values.get(i);
  }

  // Same as add, but must mark |name| as cumulative.
  // Affects printing out the summary
  public void addCumulative(String name, boolean value) { addCumulative(name, value ? 1 : 0); }
  public void addCumulative(String name, double value) {
    cumulativeNames.add(name);
    add(name, value);
  }

  public void add(String name, boolean value) { add(name, value ? 1 : 0); }
  public void add(String name, double value) { add(name, null, value); }
  public void add(String name, Object key, double value) {
    StatFig fig = new StatFig();
    fig.add(key, value);
    add(name, fig);
  }
  public void add(String name, StatFig fig) {
    getFigHard(name).add(fig);
  }
  public synchronized void add(Evaluation eval) {
    for (int i = 0; i < eval.names.size(); i++)
      add(eval.names.get(i), eval.values.get(i));
    cumulativeNames.addAll(eval.cumulativeNames);
  }

  public LispTree toLispTree() {
    LispTree out = LispTree.proto.newList();
    for (int i = 0; i < names.size(); i++) {
      out.addChild(LispTree.proto.newList(names.get(i), Fmt.D(values.get(i).mean())));
    }
    return out;
  }

  public static Evaluation fromLispTree(LispTree t) {
    Evaluation e = new Evaluation();
    for (int i = 0; i < t.children.size(); i++) {
      e.add(
          t.child(i).child(0).value,
          Double.parseDouble(t.child(i).child(1).value));
    }
    return e;
  }

  public String summary() { return summary(" "); }
  public String summary(String delim) {
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < names.size(); i++) {
      if (i > 0) out.append(delim);
      double value;
      if (cumulativeNames.contains(names.get(i)))
        value = values.get(i).sum();
      else
        value = values.get(i).mean();
      out.append(names.get(i) + '=' + Fmt.D(value));
    }
    return out.toString();
  }

  private void putOutput(String prefix, StatFig fig) {
    Execution.putOutput(prefix + ".count", fig.count());
    if (fig.count() > 0) {
      Execution.putOutput(prefix + ".mean", fig.mean());
      Execution.putOutput(prefix + ".max", fig.max());
    }
  }

  private String basePrefix(String prefix) {
    String[] parts = prefix.split("\\."); return parts[parts.length - 1];
  }

  public void putOutput(String prefix) {
    for (int i = 0; i < names.size(); i++)
      putOutput(basePrefix(prefix) + "." + names.get(i), values.get(i));
  }
  public void logStats(String prefix) {
    LogInfo.begin_track_printAll("Evaluation stats for %s", prefix);
    for (int i = 0; i < names.size(); i++)
      LogInfo.log(names.get(i) + " = " + values.get(i));
    LogInfo.end_track();
  }

  Map<String, Map<String, Object>> toMap() {
    Map<String, Map<String, Object>> m = new HashMap<String, Map<String, Object>>(names.size());
    for (int i = 0; i < names.size(); i++)
      m.put(names.get(i), statFigToMap(values.get(i)));
    return m;
  }

  private static Map<String, Object> statFigToMap(StatFig fig) {
    Map<String, Object> m = new HashMap<String, Object>(7);
    m.put("min", fig.min());
    m.put("minKey", fig.minKey());
    m.put("max", fig.max());
    m.put("maxKey", fig.maxKey());
    m.put("mean", fig.mean());
    m.put("stddev", fig.stddev());
    m.put("count", fig.count());
    return m;
  }
}
