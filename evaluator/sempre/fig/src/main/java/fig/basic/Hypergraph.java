package fig.basic;

import java.io.*;
import java.util.*;
import fig.basic.*;
import fig.exec.*;
import fig.record.*;
import fig.prob.*;
import static fig.basic.LogInfo.*;

/**
 * Provides a module for doing inference over discrete structures
 * such as sequences and parse trees.  A distribution over possibly
 * exponentially many structures (widgets) is encoded compactly using a
 * directed hypergraph.
 *
 * Each hyperedge corresponds to a discrete decision which describes part of
 * the structure.  At sum nodes, exactly one hyperedge is chosen; at prod
 * nodes, all hyperedges are chosen.  The product of all chosen weights on the
 * hyperedges determines the probability of the widget (after appropriate
 * normalization).
 *
 * Notes:
 *  - We don't check for cycles.  You will get stack overflow if there are cycles.
 *  - The children of a product node or the two children of a hyperedge should be disjoint.
 *    Otherwise, you will get an assertion failed with invalid posterior probability > 1
 *    due to double counting.
 *    NOTE: this is unnecessarily restrictive.  We should get rid of this, but have to be careful.
 *    Updating posteriors with prob > 1 is fine, but when fetching the widget, user must do it right.
 *
 * To construct the graph:
 *   if(!addSumNode(node))
 *     addEdge(node, child1, child2, new HyperedgeInfo<Widget>() {
 *       // Implement getWeight(), setPosterior(), choose() here
 *     });
 *
 * To do inference and get back results:
 *   computePosteriors(): perform inference to compute posterior distribution over hyperpaths
 *   computeELogZEntropy(): compute some statistics about this inference
 *   fetchPosteriors(): call setPosterior on each hyperedge
 *   fetchBestHyperpath(widget): call choose on each hyperedge in the best one
 *   fetchSampleHyperpath(widget): call choose on each hyperedge in the best one
 *   fetchPosteriorHyperpath(widget): call choose on each hyperedge with a weight (TODO: combine it with fetchPosteriors)
 */
public class Hypergraph<Widget> {
  public enum NodeType { prod, sum }; // Each node represents either a product or a sum over its children

  private interface AbstractHyperedgeInfo<Widget> {
    public void setPosterior(double prob);
    public Widget choose(Widget widget); // Return the updated widget
  }
  public interface HyperedgeInfo<Widget> extends AbstractHyperedgeInfo<Widget> {
    public abstract double getWeight();
  }
  public interface LogHyperedgeInfo<Widget> extends AbstractHyperedgeInfo<Widget> {
    public double getLogWeight();
  }

  private class NullHyperedgeInfo<Widget> implements HyperedgeInfo<Widget> {
    public double getWeight() { return 1; }
    public void setPosterior(double prob) { }
    public Widget choose(Widget widget) { return widget; }
  }
  private final NullHyperedgeInfo<Widget> nullHyperedgeInfo = new NullHyperedgeInfo<Widget>();

  // Represents a choice involving a single multinomial.
  public static class MultinomialHyperedgeInfo<Widget> implements HyperedgeInfo<Widget> {
    public final double[] params;
    public final double[] counts;
    public final int i;
    public final double increment;
    public MultinomialHyperedgeInfo(double[] params, double[] counts, int i, double increment) {
      this.params = params;
      this.counts = counts;
      this.i = i;
      this.increment = increment;
    }
    public double getWeight() { return params[i]; }
    public void setPosterior(double prob) { counts[i] += prob * increment; }
    public Widget choose(Widget widget) { return widget; }
  }

  // Represents a choice involving a single multinomial.
  public static class MultinomialLogHyperedgeInfo<Widget> implements LogHyperedgeInfo<Widget> {
    public final double[] params;
    public final double[] counts;
    public final int i;
    public final double increment;
    public MultinomialLogHyperedgeInfo(double[] params, double[] counts, int i, double increment) {
      this.params = params;
      this.counts = counts;
      this.i = i;
      this.increment = increment;
    }
    public double getLogWeight() { return params[i]; }
    public void setPosterior(double prob) { counts[i] += prob * increment; }
    public Widget choose(Widget widget) { return widget; }
  }

  private static class NodeInfo {
    NodeInfo(Object node, NodeType nodeType) { this.node = node; this.nodeType = nodeType; }
    final Object node; // Just for visualizing/debugging
    NodeType nodeType; // Can be changed
    final List<Hyperedge> edges = new ArrayList(); // Children
    BigDouble insideScore, outsideScore, maxScore; // Things we compute during inference
    public String toString() { return node.toString(); }
  }
  private static class Hyperedge {
    final NodeInfo dest1, dest2; // Child nodes
    final AbstractHyperedgeInfo info; // Specifies I/O for the hyperedge
    BigDouble weight;
    Hyperedge(NodeInfo dest1, NodeInfo dest2, AbstractHyperedgeInfo info) {
      this.dest1 = dest1;
      this.dest2 = dest2;
      this.info = info;
    }

    public void setWeight() {
      if(info instanceof HyperedgeInfo)
        this.weight = BigDouble.fromDouble(((HyperedgeInfo)info).getWeight());
      else if(info instanceof LogHyperedgeInfo)
        this.weight = BigDouble.fromLogDouble(((LogHyperedgeInfo)info).getLogWeight());
      else
        throw new RuntimeException("Unknown type of info");

      if(weight.isZero()) weight.setToVerySmall(); // Avoid zeros so everything has some positive probability
    }

    public String toString() { return String.format("%s %s (%s)", dest1, dest2, weight); }
  }

  // Specifies the hypergraph and stores the computations
  public boolean debug = false;
  public boolean allowEmptyNodes = false; // Do we allow nodes with no children?
  private HashMap<Object,NodeInfo> nodes = new HashMap();
  private NodeInfo[] topologicalOrdering;

  // Start and end nodes
  private final Object startNode = addNodeAndReturnIt("START", NodeType.sum); // use sum or prod versions
  public final Object endNode = addNodeAndReturnIt("END", NodeType.sum);
  public final Object invalidNode = "INVALID";
  private final NodeInfo startNodeInfo = getNodeInfoOrFail(startNode);
  private final NodeInfo endNodeInfo = getNodeInfoOrFail(endNode);
  private Hyperedge terminalEdge = new Hyperedge(endNodeInfo, endNodeInfo, nullHyperedgeInfo);

  // Things we're going to compute
  private double logZ = Double.NaN; // Normalization constant
  private double elogZ = Double.NaN; // E_q(z|x) log weight(x,z)
  private double entropy = Double.NaN; // Entropy of the posterior q(z|x)

  public double getLogZ() { return logZ; }
  public double getELogZ() { return elogZ; }
  public double getEntropy() { return entropy; }

  // Add nodes: return whether added something
  public boolean addSumNode(Object node) { return addNode(node, NodeType.sum); }
  public boolean addProdNode(Object node) { return addNode(node, NodeType.prod); }

  public Object sumStartNode() { getNodeInfoOrFail(startNode).nodeType = NodeType.sum; return startNode; }
  public Object prodStartNode() { getNodeInfoOrFail(startNode).nodeType = NodeType.prod; return startNode; }

  public int numEdges(Object node) { return getNodeInfoOrFail(node).edges.size(); }
  public int numNodes() { return nodes.size(); }

  public void assertNonEmpty(Object node) {
    assert numEdges(node) > 0 : node + " has no children hyperedges (it's empty)";
  }

  // Add edges
  public void addEdge(Object source) { addEdge(source, endNode, endNode, nullHyperedgeInfo); }
  public void addEdge(Object source, AbstractHyperedgeInfo<Widget> info) { addEdge(source, endNode, endNode, info); }
  public void addEdge(Object source, Object dest1) { addEdge(source, dest1, endNode, nullHyperedgeInfo); }
  public void addEdge(Object source, Object dest1, AbstractHyperedgeInfo<Widget> info) { addEdge(source, dest1, endNode, info); }
  public void addEdge(Object source, Object dest1, Object dest2) { addEdge(source, dest1, dest2, nullHyperedgeInfo); }
  public void addEdge(Object source, Object dest1, Object dest2, AbstractHyperedgeInfo<Widget> info) {
    assert source != invalidNode;
    if(debug) dbgs("add %s -> %s %s", source, dest1, dest2);
    if(dest1 == invalidNode || dest2 == invalidNode) return;
    assert source != dest1 && source != dest2; // Catch obvious loops
    getNodeInfoOrFail(source).edges.add(new Hyperedge(getNodeInfoOrFail(dest1), getNodeInfoOrFail(dest2), info));
  }

  // Helpers
  private boolean addNode(Object node, NodeType nodeType) { // Return whether a new node was added
    NodeInfo info = nodes.get(node);
    if(info != null) return false;
    nodes.put(node, new NodeInfo(node, nodeType));
    return true;
  }
  private Object addNodeAndReturnIt(Object node, NodeType nodeType) { // Return the node that we added
    if(!addNode(node, nodeType)) throw Exceptions.bad("Can't add node");
    return node;
  }
  private NodeInfo getNodeInfoOrFail(Object node) {
    NodeInfo info = nodes.get(node);
    assert info != null : "Node doesn't exist in hypergraph (need to add nodes before edges containing them): "+node;
    return info;
  }

  private void checkGraph() {
    // Make sure that all nodes have children (except end of course)
    if(!allowEmptyNodes) {
      int numBadNodes = 0;
      for(NodeInfo nodeInfo : nodes.values()) {
        if(nodeInfo.edges.size() == 0 && nodeInfo.node != endNode) {
          errors("Node has no children: "+nodeInfo.node);
          numBadNodes++;
        }
      }
      if(numBadNodes > 0) throw Exceptions.bad(numBadNodes + " bad nodes (those without children)");
    }

    // FUTURE: check for cycles to be more graceful
    // Now, we just wait for computeTopologicalOrdering() to stack overflow
  }

  private void computeTopologicalOrdering() {
    if(topologicalOrdering != null) return;
    checkGraph();
    topologicalOrdering = new NodeInfo[nodes.size()];
    HashSet<NodeInfo> hit = new HashSet();
    IntRef i = new IntRef(nodes.size()-1);
    computeReverseTopologicalOrdering(hit, startNodeInfo, i);
    if(i.value != -1)
      throw Exceptions.bad("Not all nodes reachable from startNode");
    assert topologicalOrdering[0] == startNodeInfo;
    if(!allowEmptyNodes)
      assert topologicalOrdering[topologicalOrdering.length-1] == endNodeInfo;
  }
  private void computeReverseTopologicalOrdering(HashSet<NodeInfo> hit, NodeInfo nodeInfo, IntRef i) {
    if(hit.contains(nodeInfo)) return;
    for(Hyperedge edge : nodeInfo.edges) {
      computeReverseTopologicalOrdering(hit, edge.dest1, i);
      computeReverseTopologicalOrdering(hit, edge.dest2, i);
    }
    topologicalOrdering[i.value--] = nodeInfo;
    hit.add(nodeInfo);
  }

  //////////////////////////////////////////////////////////// 

  public Hypergraph() { }

  public void computePosteriors(boolean viterbi) {
    computeTopologicalOrdering();
    setHyperedgeWeights();
    computeInsideMaxScores(viterbi);
    if(!viterbi) computeOutsideScores();
    if(viterbi) this.logZ = startNodeInfo.maxScore.toLogDouble();
    else        this.logZ = startNodeInfo.insideScore.toLogDouble();
  }

  private void setHyperedgeWeights() {
    for (NodeInfo nodeInfo : topologicalOrdering) {
      for (Hyperedge edge : nodeInfo.edges) {
        //logs("setWeight %s -> %s", nodeInfo, edge);
        edge.setWeight();
      }
      // Invalidate
      nodeInfo.maxScore = null;
      nodeInfo.insideScore = null;
      nodeInfo.outsideScore = null;
    }
  }

  private void computeInsideMaxScores(boolean viterbi) {
    if(viterbi && this.startNodeInfo.maxScore != null) return; // Already computed
    if(!viterbi && this.startNodeInfo.insideScore != null) return; // Already computed

    for(int i = topologicalOrdering.length-1; i >= 0; i--) {
      NodeInfo nodeInfo = topologicalOrdering[i];
      BigDouble score;
      if(viterbi) score = nodeInfo.maxScore = BigDouble.invalid();
      else        score = nodeInfo.insideScore = BigDouble.invalid();
      if(nodeInfo == endNodeInfo) { score.setToOne(); continue; }
      switch(nodeInfo.nodeType) {
        case sum:
          score.setToZero();
          for(Hyperedge edge : nodeInfo.edges) {
            if(viterbi) score.updateMax_mult3(edge.weight, edge.dest1.maxScore, edge.dest2.maxScore);
            else        score.incr_mult3(edge.weight, edge.dest1.insideScore, edge.dest2.insideScore);
            //assert score.M != 0 : score + " " + edge.weight + " " + edge.dest1.insideScore + " " + edge.dest2.insideScore;
          }
          break;
        case prod:
          score.setToOne();
          for(Hyperedge edge : nodeInfo.edges) {
            if(viterbi) score.mult_mult3(edge.weight, edge.dest1.maxScore, edge.dest2.maxScore);
            else        score.mult_mult3(edge.weight, edge.dest1.insideScore, edge.dest2.insideScore);
          }
          break;
      }
      //if(!viterbi) dbgs("insideScore(%s) = %s", nodeInfo.node, nodeInfo.insideScore);
    }
    if(viterbi) assert !startNodeInfo.maxScore.isZero() : "Max score = 0";
    else        assert !startNodeInfo.insideScore.isZero() : "Marginal score = 0";
  }

  private void computeOutsideScores() {
    if(startNodeInfo.outsideScore != null) return; // Already computed

    // Initialize values to zero
    for(NodeInfo nodeInfo : topologicalOrdering)
      nodeInfo.outsideScore = BigDouble.zero();

    startNodeInfo.outsideScore.setToOne();
    for(int i = 0; i < topologicalOrdering.length; i++) {
      NodeInfo nodeInfo = topologicalOrdering[i];
      if(nodeInfo.insideScore.isZero()) continue; // This happens for dead nodes
      //dbgs("outsideScore(%s) = %s", nodeInfo.node, nodeInfo.outsideScore);
      switch(nodeInfo.nodeType) {
        case sum:
          for(Hyperedge edge : nodeInfo.edges) {
            if(edge.dest1 != endNodeInfo) edge.dest1.outsideScore.incr_mult3(nodeInfo.outsideScore, edge.weight, edge.dest2.insideScore);
            if(edge.dest2 != endNodeInfo) edge.dest2.outsideScore.incr_mult3(nodeInfo.outsideScore, edge.weight, edge.dest1.insideScore);
          }
          break;
        case prod:
          for(Hyperedge edge : nodeInfo.edges) {
            if(edge.dest1 != endNodeInfo) edge.dest1.outsideScore.incr_mult2div1(nodeInfo.outsideScore, nodeInfo.insideScore, edge.dest1.insideScore);
            if(edge.dest2 != endNodeInfo) edge.dest2.outsideScore.incr_mult2div1(nodeInfo.outsideScore, nodeInfo.insideScore, edge.dest2.insideScore);
          }
          break;
      }
    }
  }

  public void fetchPosteriors(boolean viterbi) {
    if(viterbi) fetchPosteriorsMax(); // Only need to call setPosteriors on the best widget
    else        fetchPosteriorsSum(); // Call setPosteriors on each hyperedge
  }

  public void computeELogZEntropy(boolean viterbi) {
    if(viterbi) { // Easy case: q(z|x) is degenerate
      this.elogZ = this.logZ;
      this.entropy = 0;
      return;
    }

    this.elogZ = 0;
    this.entropy = 0;
    for(NodeInfo nodeInfo : topologicalOrdering) {
      //dbg(startNodeInfo.insideScore);
      double nodeProb = BigDouble.mult2div1(nodeInfo.outsideScore, nodeInfo.insideScore, startNodeInfo.insideScore).toDouble();
      if(nodeProb == 0) continue;
      switch(nodeInfo.nodeType) {
        case sum:
          for(Hyperedge edge : nodeInfo.edges) {
            double edgeProb = BigDouble.mult4div1(nodeInfo.outsideScore, edge.weight,
              edge.dest1.insideScore, edge.dest2.insideScore, startNodeInfo.insideScore).toDouble();
            if(edgeProb == 0) continue;
            elogZ += edgeProb * edge.weight.toLogDouble();
            entropy -= edgeProb * Math.log(edgeProb/nodeProb);
          }
          break;
        case prod:
          // No uncertainty, so no contribution to entropy
          for(Hyperedge edge : nodeInfo.edges)
            elogZ += nodeProb * edge.weight.toLogDouble();
          break;
      }
    }
  }

  private void fetchPosteriorsSum() {
    for(NodeInfo nodeInfo : topologicalOrdering) {
      switch(nodeInfo.nodeType) {
        case sum:
          for(Hyperedge edge : nodeInfo.edges) {
            double prob = BigDouble.mult4div1(nodeInfo.outsideScore, edge.weight,
              edge.dest1.insideScore, edge.dest2.insideScore, startNodeInfo.insideScore).toDouble();
            assert prob >= 0 && prob <= 1+1e-6 : nodeInfo + " " + edge + " has invalid posterior probability " + prob;
            //if(prob > 0.1) dbgs("setPosterior sum %s %s", edge, Fmt.D(prob));
            edge.info.setPosterior(prob);
          }
          break;
        case prod:
          for(Hyperedge edge : nodeInfo.edges) {
            double prob = BigDouble.mult2div1(nodeInfo.outsideScore, nodeInfo.insideScore, startNodeInfo.insideScore).toDouble();
            assert prob >= 0 && prob <= 1+1e-6 : nodeInfo + " " + edge + " has invalid posterior probability " + prob;
            //if(prob > 0.1) dbgs("setPosterior prod %s %s", edge, Fmt.D(prob));
            edge.info.setPosterior(prob);
          }
          break;
      }
    }
  }

  private void fetchPosteriorsMax() {
    HyperpathChooser chooser = new HyperpathChooser();
    chooser.viterbi = true;
    chooser.setPosterior = true;
    chooser.recurse(startNodeInfo);
  }

  // Return the best or a sampled solution
  public HyperpathResult<Widget> fetchBestHyperpath(Widget widget) {
    computeInsideMaxScores(true);
    HyperpathChooser chooser = new HyperpathChooser();
    chooser.viterbi = true;
    chooser.widget = widget;
    chooser.choose = true;
    chooser.recurse(startNodeInfo);
    return new HyperpathResult(chooser.widget, chooser.logWeight);
  }
  public HyperpathResult<Widget> fetchSampleHyperpath(Random random, Widget widget) {
    computeInsideMaxScores(false);
    HyperpathChooser chooser = new HyperpathChooser();
    chooser.viterbi = false;
    chooser.widget = widget;
    chooser.random = random;
    chooser.choose = true;
    chooser.recurse(startNodeInfo);
    return new HyperpathResult(chooser.widget, chooser.logWeight);
  }

  public static class HyperpathResult<Widget> {
    public HyperpathResult(Widget widget, double logWeight) {
      this.widget = widget;
      this.logWeight = logWeight;
    }
    public final Widget widget;
    public final double logWeight;
  }

  private class HyperpathChooser {
    boolean viterbi;
    Widget widget;
    Random random;
    // Which function to call to return what was chosen
    boolean choose;
    boolean setPosterior;
    double logWeight; // Likelihood of the weight of the hyperpath chosen

    private void recurse(NodeInfo nodeInfo) {
      if(nodeInfo == endNodeInfo) return;

      switch(nodeInfo.nodeType) {
        case sum:
          int n = nodeInfo.edges.size();
          // Compute scores
          BigDouble[] scores = new BigDouble[n];
          for(int i = 0; i < n; i++) {
            Hyperedge edge = nodeInfo.edges.get(i);
            if(viterbi) scores[i] = BigDouble.mult3(edge.weight, edge.dest1.maxScore, edge.dest2.maxScore);
            else        scores[i] = BigDouble.mult3(edge.weight, edge.dest1.insideScore, edge.dest2.insideScore);
          }
          // Choose edge
          int chosenIndex;
          if(viterbi) chosenIndex = BigDouble.argmax(scores);
          else        chosenIndex = BigDouble.normalizeAndSample(random, scores);
          if(chosenIndex == -1)
            throw Exceptions.bad("Unable to choose from: %s", Fmt.D(scores));
          Hyperedge chosenEdge = nodeInfo.edges.get(chosenIndex);
          if(choose) widget = (Widget)chosenEdge.info.choose(widget);
          //if(choose) dbg("Choose "+widget);
          if(setPosterior) chosenEdge.info.setPosterior(1.0);
          logWeight += chosenEdge.weight.toLogDouble();

          recurse(chosenEdge.dest1);
          recurse(chosenEdge.dest2);
          break;
        case prod:
          // Recurse on each edge
          for(Hyperedge edge : nodeInfo.edges) {
            if(choose) widget = (Widget)edge.info.choose(widget);
            if(setPosterior) edge.info.setPosterior(1.0);
            logWeight += edge.weight.toLogDouble();
            recurse(edge.dest1);
            recurse(edge.dest2);
          }
          break;
      }
    }
  }

  // An example of how to use the class.
  // Create a simple mixture model and run EM on it.
  //  h ~ Multinomial
  //  for j = 1, ..., L:
  //    x_j ~ Multinomial depending on h
  private static class HyperedgeTest {
    @Option(gloss="Number of possible values of the latent variable") public int K = 3;
    @Option(gloss="Number of possible values of observed variables") public int D = 3;
    @Option(gloss="Number of observed variables") public int L = 3;
    @Option(gloss="Number of examples to generate") public int numExamples = 100;
    @Option(gloss="Number of EM iterations to run") public int numIters = 20;
    Random random = new Random(1);

    class Params {
      double[] pi = new double[K];
      double[][] emissions = new double[K][D];

      void initRandom() {
        pi = new Dirichlet(K, 1).sample(random);
        for (int h = 0; h < K; h++)
          emissions[h] = new Dirichlet(D, 1).sample(random);
      }

      void normalize() {
        NumUtils.normalize(pi);
        for (int h = 0; h < K; h++)
          NumUtils.normalize(emissions[h]);
      }

      void log() {
        LogInfo.begin_track("Params");
        LogInfo.logs("pi = %s", Fmt.D(pi));
        for (int h = 0; h < K; h++)
          LogInfo.logs("emissions[%d] = %s", h, Fmt.D(emissions[h]));
        LogInfo.end_track();
      }
    }

    public HyperedgeTest() {
      // Initialize parameters
      Params params = new Params();
      params.initRandom();
      params.log();

      // Generate artificial data
      List<int[]> examples = new ArrayList<int[]>();
      for (int i = 0; i < numExamples; i++) {
        int h = random.nextInt(K);
        int[] x = new int[L];
        for (int j = 0; j < L; j++)
          x[j] = random.nextDouble() < 0.8 ? h % D : random.nextInt(D);
        examples.add(x);
      }

      for (int iter = 0; iter < numIters; iter++) {
        // E-step
        Params counts = new Params();
        double logZ = 0;
        for (int[] x : examples) {
          Hypergraph H = new Hypergraph();
          Object rootNode = H.sumStartNode();
          for (int h = 0; h < K; h++) {  // For each value of hidden states...
            String hNode = "h="+h;
            H.addProdNode(hNode);
            H.addEdge(rootNode, hNode, new MultinomialHyperedgeInfo(params.pi, counts.pi, h, 1));
            for (int j = 0; j < L; j++)
              H.addEdge(hNode, H.endNode, new MultinomialHyperedgeInfo(params.emissions[h], counts.emissions[h], x[j], 1));
          }
          H.computePosteriors(false);
          H.fetchPosteriors(false);
          logZ += H.getLogZ();
        }
        logs("logZ = %s", logZ);

        // M-step
        counts.normalize();
        params = counts;
      }

      params.log();
    }
  }

  public static void main(String[] args) {
    new HyperedgeTest();
  }
}
