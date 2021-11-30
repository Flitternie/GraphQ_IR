package fig.record;

import fig.basic.*;
import java.util.*;

/**
 * A function command node includes a rich set of basic
 * functions that operate on record nodes.
 *
 * FUTURE:
 *  - Blur the distinction between arguments into a function and the
 *    node returned by children command.
 *  - Fancier version of replaceChildKeys.
 */
public class FuncCommandNode extends TwigRecordNode implements CommandNode {
  public static final CommandNode noOpCmd =
    new FuncCommandNode("noOp", Collections.EMPTY_LIST, null, false);
  public static final CommandNode identityCmd =
    new FuncCommandNode("identity", Collections.EMPTY_LIST, null, false);
  public static final CommandNode childKeysCmd =
    new FuncCommandNode("keySkeleton", Collections.singletonList("1"), identityCmd, false);
  public static final CommandNode keySkeletonCmd =
    new FuncCommandNode("keySkeleton", Collections.EMPTY_LIST, identityCmd, false);
  public static final CommandNode withoutChildrenCmd =
    new FuncCommandNode("withoutChildren", Collections.EMPTY_LIST, identityCmd, false);

  public static boolean isImmutableCmd(CommandNode cmd) {
    return cmd == FuncCommandNode.noOpCmd ||
           cmd == FuncCommandNode.identityCmd ||
           cmd == FuncCommandNode.childKeysCmd ||
           cmd == FuncCommandNode.keySkeletonCmd ||
           cmd == FuncCommandNode.withoutChildrenCmd;
  }

  private final String name; // Name of function
  private final List<String> args; // Arguments to the function
  // Whether this function should actually be applied on children and the
  // results concatenated; could be implemented with compose, but this is
  // easier to special case.
  private final boolean applyToChildren;
  private ArgsParser parser;

  public FuncCommandNode(String name, List<String> args, CommandNode child, boolean applyToChildren) {
    super((applyToChildren ? "map-" : "") + name, StrUtils.join(args), child);
    this.name = name;
    this.args = args;
    this.applyToChildren = applyToChildren;
    this.parser = new ArgsParser(VarBindingList.varEscapeChar, args);
  }

  public String getName() { return name; }

  // Return a version that doesn't apply to children:
  // Called by a version that does.
  private FuncCommandNode notApplyToChildrenCmd() {
    return new FuncCommandNode(name, args, identityCmd, false);
  }

  // A key skeleton of a record tries to retain the full recursive structure of
  // the record, but only recurses only the first occurence of each key.
  // The value is also thrown away, and replaced with the number of occurrences of the key
  private RecordNode extractKeySkeleton(RecordNode record,
      int maxDepth, String key, String value, IntRef numNodes) {
    FullRecordNode result = new FullRecordNode(key, value);
    numNodes.value++;

    if(maxDepth > 0) {
      // Count number of times each child key occurs
      Map<String, Integer> counts = new LinkedHashMap<String, Integer>();
      for(RecordNode childRecord : record.getChildren()) {
        String childKey = childRecord.getKey();
        MapUtils.incr(counts, childKey, 1);
      }
      
      // Now go through the nodes again and recurse,
      // removing the key from counts as we go so we don't repeat.
      for(RecordNode childRecord : record.getChildren()) {
        // Note: limit number of total nodes, not number of children
        String childKey = childRecord.getKey();
        if(!counts.containsKey(childKey)) continue; // Skip keys we already have
        result.addChild(extractKeySkeleton(childRecord,
              maxDepth-1, childKey, ""+counts.get(childKey), numNodes));
        counts.remove(childKey);
      }
    }
    return result;
  }

  /**
   * Treat the first child choice as the row coordinate
   * and the second child choice as the column coordinate
   * of a matrix.
   */
  private static RecordNode transposeRecordNode(RecordNode record) {
    FullRecordNode newRecord =
      new FullRecordNode(record.getKey(), record.getValue());
    List<RecordNode> children = record.getChildren(); // Rows
    RecordNode prototypeRecord = children.get(0);

    for(int i = 0; i < prototypeRecord.numChildren(); i++) { // Columns
      FullRecordNode newChild = new FullRecordNode(
          prototypeRecord.getChildren().get(i).getKey(),
          prototypeRecord.getChildren().get(i).getValue());
      for(RecordNode child : children) { // Rows
        if(i < child.numChildren())
          newChild.addChild(child.getChildren().get(i).shallowCopy(
                child.getKey(), child.getValue()));
      }
      newRecord.addChild(newChild);
    }
    return newRecord;
  }

  private static RecordNode replaceIndex(RecordNode tree, List<RecordNode> list) {
    // For leaf nodes...
    if(tree.numChildren() == 0) {
      // Get the index
      int idx = (int)tree.getDoubleValue();
      // Out of bounds: return null
      if(idx < 0 || idx >= list.size()) return LeafRecordNode.nullNode;
      // Lookup the index get an element out of the list
      return list.get(idx);
    }

    // Recursively replace for all its children
    FullRecordNode newTree = new FullRecordNode(tree.getKey(), tree.getValue());
    for(RecordNode child : tree.getChildren())
      newTree.addChild(replaceIndex(child, list));
    return newTree;
  }

  private static RecordNode raise(RecordNode record, String key, String value) {
    return new TwigRecordNode(key, value, record);
  }
  private static RecordNode raise(RecordNode record) {
    return new TwigRecordNode(null, null, record);
  }

  private class ExecState {
    private LocalCommandEnv localEnv;
    public ExecState(LocalCommandEnv localEnv) {
      this.localEnv = localEnv;
    }

    public RecordNode exec() {
      RecordNode record = localEnv.getCurrRecord();
      VarBindingList bindings = localEnv.getVarBindingList();
      // Call child command node to obtain an intermediate result,
      // and then perform the function on the result
      CommandNode childCmd = (CommandNode)getChild();

      if(name.equals("identity")) return record;
      if(name.equals("noOp")) return LeafRecordNode.nullNode;

      if(name.equals("sub") || name.equals("head") || name.equals("tail") ||
         name.equals("Sub") || name.equals("Head") || name.equals("Tail")) {
        // Purpose: set the hint (either the temporary one or the default one)
        // Arguments: description of the hint
        SubsetHint hint;
        String lname = name.toLowerCase();
        if(lname.equals("sub")) {
          //parser.setNames("start", "end", "skipcount").parse(bindings);
          hint = new PeriodicSubsetHint(args, bindings);
        }
        else if(lname.equals("head")) {
          parser.setNames("count").parse(bindings);
          hint = new PeriodicSubsetHint(
              ListUtils.newList(""+0, ""+parser.getInt("count", 10)), bindings);
        }
        else if(lname.equals("tail")) {
          parser.setNames("count").parse(bindings);
          hint = new PeriodicSubsetHint(
              ListUtils.newList(""+(-parser.getInt("count", 10)), "1f"), bindings);
        }
        else
          throw Exceptions.unknownCase;

        // Set the hint and call children
        LocalCommandEnv childLocalEnv = localEnv.withHint(hint);
        if(!lname.equals(name)) // Uppercase means set default
          childLocalEnv = childLocalEnv.withDefaultHint(hint);
        return localEnv.applyHint(childCmd.exec(childLocalEnv));
      }
      if(name.equals("map")) {
        // Purpose: a functional for loop.
        // Bind a variable to one of several values
        // and evaluate the child command with each of those binding.
        // Arguments: variable, value1, value2, value3, ...
        FullRecordNode result = new FullRecordNode("map", null);
        parser.parse(bindings);
        String var = parser.getHard(0);
        for(int i = 1; i < parser.size(); i++) {
          String val = parser.getHard(i);
          RecordNode node = childCmd.exec(
            localEnv.withHintIsDefault().withNewBinding(var, val).withIndex(i-1));
          result.addChild(node.shallowCopy(var, val));
        }
        return result;
      }

      // Sequence of events:
      //  - Apply the children with the default hint to get result.
      //  - Do some processing to get newResult.
      //  - Apply the hint to newResult.
      RecordNode result = childCmd.exec(localEnv.withHintIsDefault());

      // We need to apply the command to children
      if(applyToChildren)
        return SubsetHintUtils.applyHint(localEnv.getHint(), result,
            notApplyToChildrenCmd(), localEnv.withHintIsDefault());

      RecordNode newResult;
      if(name.equals("define")) {
        // Purpose: define a global macro (SIDE-EFFECTS!)
        // Arguments: variable name, value name
        String var = args.get(0);
        String val = args.get(1);
        localEnv.getGlobalEnv().putVar(var, val);
        newResult = raise(new LeafRecordNode(var, val));
      }
      else if(name.equals("key")) {
        // Purpose: replace the key with a new key
        // Arguments: the new key
        parser.setNames("newKey").parse(bindings);
        String newKey = parser.get("newKey", null);
        newResult = result.shallowCopy(newKey, result.getValue());
      }
      else if(name.equals("replaceKey")) {
        // Purpose: modify the key with a regular expression
        // Arguments: regex1=replacement1, regex2=replacement2, etc.
        // regex is the regular expression
        // replacement is replacement string
        // Apply each of these replacements in turn.
        String newKey = result.getKey();
        parser.parse(bindings);
        for(int i = 0; i < parser.size(); i++) {
          List<String> kv = StrUtils.splitIgnoreEscaped(parser.getHard(i), "=");
          if(kv.size() == 0)
            throw new RuntimeException("Invalid argument: " + parser.getHard(i));
          if(kv.size() == 1) kv.add(""); // Replace with nothing
          newKey = newKey.replaceAll(kv.get(0), kv.get(1));
        }
        newResult = result.shallowCopy(newKey, result.getValue());
      }
      else if(name.equals("childKeys")) {
        // Purpose: Replace children keys with the list of the following
        // Arguments (non-standandard): list of children keys to use
        // !key is cumbersome to use here.
        newResult = new FullRecordNode(result.getKey(), result.getValue());
        parser.parse(bindings);
        for(int i = 0; i < result.numChildren(); i++) {
          RecordNode childNode = result.getChildren().get(i);
          String childKey = parser.get(i, childNode.getKey()); // Replace the child key
          String childValue = childNode.getValue();
          newResult.addChild(childNode.shallowCopy(childKey, childValue));
        }
      }
      else if(name.equals("childValues")) {
        // Purpose: Replace children values with the list of the following
        // Arguments (non-standandard): list of children values to use
        // !value is cumbersome to use here.
        newResult = new FullRecordNode(result.getKey(), result.getValue());
        parser.parse(bindings);
        for(int i = 0; i < result.numChildren(); i++) {
          RecordNode childNode = result.getChildren().get(i);
          String childKey = childNode.getKey();
          String childValue = parser.get(i, childNode.getValue()); // Replace the child value
          newResult.addChild(childNode.shallowCopy(childKey, childValue));
        }
      }
      else if(name.equals("save")) {
        // Purpose: saves the record node to disk so that it can be read off again.
        // Saving is done on the server side.
        // Arguments: file path to save it to
        parser.setNames("out", "append").parse(bindings);
        RecordNodeUtils.writeRecordNode(result, parser.getHard("out"), parser.getBoolean("append", false));
        newResult = result.withoutChildren();
      }
      else if(name.equals("raise")) {
        // Purpose: add one level of hierarchy on top of the result node
        // Arguments: key, value (optional)
        // Add one more level of hierarchy
        parser.setNames("key", "value").parse(bindings);
        String key = parser.get("key", null);
        String value = parser.get("value", null);
        newResult = raise(result, key, value);
      }
      else if(name.equals("diff")) {
        // Purpose: takes the first two children's values and subtracts them,
        // putting it in the parent's value.
        // Arguments: none
        double diff;
        if(result.numChildren() < 2)
          diff = Double.NaN;
        else
          diff = result.getChildren().get(0).getDoubleValue() -
                 result.getChildren().get(1).getDoubleValue();
        newResult = RecordNodeUtils.prependKeyValue(result, "diff", ""+diff);
      }
      else if(name.equals("transpose")) {
        // Purpose: transposes the result structure
        // Arguments: none
        newResult = transposeRecordNode(result);
      }
      else if(name.equals("keySkeleton")) {
        // Purpose: extracts the skeleton of the result structure
        // Arguments: the maximum depth of recursion
        parser.setNames("maxDepth").parse(bindings);
        int maxDepth = parser.getInt("maxDepth", Integer.MAX_VALUE);
        newResult = extractKeySkeleton(result, maxDepth,
            result.getKey(), result.getValue(), new IntRef(0));
      }
      else if(name.equals("withoutChildren")) {
        // Purpose: remove the children of the current node
        // Arguments: none
        newResult = result.withoutChildren();
      }
      else if(name.equals("unloadChildren")) {
        // Purpose: unload the children of the result node
        // Arguments: none
        if(result instanceof PathRecordNode) {
          ((PathRecordNode)result).unloadChildren();
          System.gc();
        }
        newResult = result.withoutChildren();
      }
      else if(name.equals("filestat")) {
        // Purpose: get file information: put the file node under the
        // statistics
        // Arguments: (mtime|size|...)
        parser.setNames("type").parse(bindings);
        String type = parser.getHard("type");
        String key = null, value = null;
        if(type != null && result instanceof PathRecordNode) {
          java.io.File path = ((PathRecordNode)result).getPath();
          key = type;
          if(type.equals("mtime")) value = ""+path.lastModified();
          else if(type.equals("path")) value = path.toString();
          else if(type.equals("size")) value = ""+path.length();
        }
        newResult = new TwigRecordNode(key, value, result);
      }
      else if(name.equals("open")) {
        // Ask client to open the file
        // Arguments: none
        // Return: just a inert leaf version of the file
        // (don't want to accidentally load a binary file)
        if(result instanceof PathRecordNode) {
          // Get the real file
          java.io.File realPath = ((PathRecordNode)result).getPath();
          // Create the mandate
          // Can't cleanup, otherwise we lose the file
          Mandate mandate = new Mandate(false);
          String tempPath = mandate.tempifyFileName(realPath.getName());
          mandate.addCommand("open " + tempPath);
          mandate.addFile(new Mandate.FileBundle(tempPath, realPath));
          // Execute it!
          try {
            localEnv.getReceiver().executeMandate(mandate);
          } catch(java.rmi.RemoteException e) {
            throw new RuntimeException(e);
          }
        }
        // Don't use withoutChildren(): want inert version
        newResult = new LeafRecordNode(result.getKey(), result.getValue());
      }
      else if(name.equals("elect")) {
        // Purpose: make the first child of result
        // the parent of the rest of result's children.
        // If no children, then return identity.
        // Arguments: none
        if(result.numChildren() < 2)
          newResult = result;
        else {
          List<RecordNode> nodes = result.getChildren();
          RecordNode root = nodes.get(0).withoutChildren();
          FullRecordNode newRoot = new FullRecordNode(root.getKey(), root.getValue());
          for(RecordNode child : root.getChildren()) newRoot.addChild(child);
          for(int i = 1; i < nodes.size(); i++) newRoot.addChild(nodes.get(i));
          newResult = new TwigRecordNode(result.getKey(), result.getValue(), newRoot);
        }
      }
      else if(name.equals("stretch")) {
        // Purpose: take the value of result and put it as the child.
        // Arguments: none
        newResult = new TwigRecordNode(result.getKey(), null,
          new LeafRecordNode("value", result.getValue()));
      }
      else {
        // The following commands build up newResult gradually.
        FullRecordNode newFullResult =
          new FullRecordNode(result.getKey(), result.getValue());
        newResult = newFullResult;

        if(name.equals("source")) {
          // Purpose: source a command file (whose name is key of result node)
          // Arguments: whether to return the detailed results
          parser.setNames("path", "detail").parse(bindings);
          boolean detail = parser.getBoolean("detail", false);
          String path = parser.get("path", result.getKey());
          // For each line, execute it
          int lineNum = 0;
          RecordNode rootRecord = localEnv.getGlobalEnv().getRootRecord();
          // Execute in root directory
          localEnv = localEnv.withCurrRecord(rootRecord).withHintIsDefault();
          for(String line : IOUtils.readProgramLinesHard(path)) {
            lineNum++;
            CommandNode cmd = CommandUtils.parse(line, localEnv.getCmdEnv());
            RecordNode child = cmd.exec(localEnv);
            if(detail) newFullResult.addChild(child.shallowCopy("line", ""+lineNum));
          }
        }
        else if(name.equals("remove0")) {
          // Purpose: remove children with 0 children
          // Arguments: none
          for(RecordNode node : result.getChildren())
            if(node.numChildren() > 0)
              newFullResult.addChild(node);
        }
        else if(name.equals("replaceIndex")) {
          // Purpose: replace the indices in a record node with nodes from a list
          // Arguments: none
          // result's first child's children is the list L
          // result's second child is the node whose leaf nodes whose value
          // are replaced with appropriate node from the list
          RecordNode list = result.getChildren().get(0);
          RecordNode tree = result.getChildren().get(1);
          newResult = replaceIndex(tree, list.getChildren());
        }
        else if(name.equals("flatten")) {
          // Purpose: merge the children nodes C of result into one tree by
          // concatenating C's children.  Throw away the key/values of C.
          // Arguments: append, integrate, prepend, replace or (null)
          // Specifies whether to append the key/value pair from C down to C's children.
          parser.setNames("propagate").parse(bindings);
          String propagate = parser.get("propagate", null);

          // Optimization: if only one child, nothing to flatten
          if(propagate == null && result.numChildren() == 1)
            newResult = result.getChildren().get(0).shallowCopy(result.getKey(), result.getValue());

          for(RecordNode node : result.getChildren()) { // C
            for(RecordNode child : node.getChildren()) { // C's children
              RecordNode newChild;
              if("prepend".equals(propagate))
                newChild = RecordNodeUtils.prependKeyValue(child, node.getKey(), node.getValue());
              else if("append".equals(propagate))
                newChild = RecordNodeUtils.appendKeyValue(child, node.getKey(), node.getValue());
              else if("integrate".equals(propagate))
                newChild = child.shallowCopy(node.getKey()+" "+child.getKey(), node.getValue()+" "+child.getValue());
              else if("replace".equals(propagate))
                newChild = child.shallowCopy(node.getKey(), node.getValue());
              else
                newChild = child;
              newFullResult.addChild(newChild);
            }
          }
        }
        else if(name.equals("stat")) {
          // Purpose: Compute statistics of the children
          // Arguments: none
          StatFig fig = new StatFig();
          for(RecordNode node : result.getChildren())
            fig.add(node.getDoubleValue());
          newFullResult.addChild(new LeafRecordNode("count", ""+fig.count()));
          newFullResult.addChild(new LeafRecordNode("min", ""+fig.min()));
          newFullResult.addChild(new LeafRecordNode("max", ""+fig.max()));
          newFullResult.addChild(new LeafRecordNode("mean", ""+fig.mean()));
          newFullResult.addChild(new LeafRecordNode("stddev", ""+fig.stddev()));
          newFullResult.addChild(new LeafRecordNode("sum", ""+fig.sum()));
        }
        else if(name.equals("min") || name.equals("max")) {
          // Purpose: compute min/max
          // Arguments: none
          boolean isMin = name.equals("min");
          RecordNode bestNode = null;
          int bestIndex = -1;
          double bestValue = isMin ? Double.POSITIVE_INFINITY : Double.NEGATIVE_INFINITY;
          for(int index = 0; index < result.numChildren(); index++) {
            RecordNode node = result.getChildren().get(index);
            double value = node.getDoubleValue();
            if(isMin ? (value < bestValue) : (value > bestValue)) {
              bestValue = value;
              bestNode = node;
              bestIndex = index;
            }
          }
          if(bestNode != null)
            newFullResult.addChild(RecordNodeUtils.appendKeyValue(bestNode, "index", ""+bestIndex));
        }
        else if(name.equals("combineSeries")) {
          // Purpose: take a list of time series and compute error bars on them
          // Arguments: mode (none or stddev or range)
          // Input record: a list of nodes, each node contains a time series
          // Output record: a single averaged time series
          parser.setNames("mode").parse(bindings);
          String mode = parser.get("mode", "none");

          List<Double> evalxs = new ArrayList(); // List of x values that we're going to evaluate at
          String key = null; // Set later
          List<List<Pair<Double,Double>>> runs = new ArrayList();
          for(RecordNode runNode : result.getChildren()) { // For each run...
            List<Pair<Double,Double>> run = new ArrayList();
            int index = 0;
            for(RecordNode node : runNode.getChildren()) {
              // Parse it
              if(key == null) key = node.getKey();
              double[] p = StrUtils.doubleSplit(RecordNodeUtils.getPrimaryValue(node));
              if(p.length == 1) p = new double[] { index, p[0] };
              if(p.length != 2) throw Exceptions.bad("Expected length 2 vector, got '%s' instead", Fmt.D(p));
              evalxs.add(p[0]);
              run.add(new Pair(p[0], p[1]));
              index++;
            }
            Collections.sort(run, new Pair.FirstComparator());
            runs.add(run);
          }
          // Sort and remove duplicate x values that we're going to evaluate at
          Collections.sort(evalxs);
          List<Double> tmpxs = new ArrayList();
          double lastx = Double.NaN;
          for(double x : evalxs) {
            if(NumUtils.equals(x, lastx)) continue;
            tmpxs.add(x);
            lastx = x;
          }
          evalxs = tmpxs;

          // Now go through each evaluation point and evaluate each run at that point
          // If that point doesn't exist, interpolate
          newResult = new FullRecordNode(result.getKey(), result.getValue());
          int R = runs.size(); // Number of runs
          int[] ri = new int[R]; // Current pointer for each of the runs
          for(double evalx : evalxs) { // For each evaluation point x
            // Evaluate each run at x (interpolating if necessary)
            // If can't interpolate, break out and forget about this evalx
            StatFig fig = new StatFig();
            for(int r = 0; r < R; r++) { // For each run...
              List<Pair<Double,Double>> run = runs.get(r);
              double x = Double.NaN, y = Double.NaN;
              // Advance pointer until we exceed or equal evalx
              while(ri[r] < run.size()) {
                x = run.get(ri[r]).getFirst();
                y = run.get(ri[r]).getSecond();
                if(x >= evalx) break;
                ri[r]++;
              }
              if(ri[r] == run.size()) break;
              if(NumUtils.equals(x, evalx)) fig.add(y); // Get it exactly
              else if(ri[r]-1 >= 0) { // Can interpolate
                double prevx = run.get(ri[r]-1).getFirst();
                double prevy = run.get(ri[r]-1).getSecond();
                assert prevx < evalx && evalx <= x : prevx + " " + evalx + " " + x;
                //localEnv.dbg(prevx + " " + prevy + " " + x + " " + y + " " + evalx);
                fig.add(prevy + (evalx-prevx)/(x-prevx)*(y-prevy));
              }
            }
            if(fig.count() == R) {
              if(mode.equals("none"))
                newResult.addChild(new LeafRecordNode(key, evalx + " " + fig.mean()));
              else if(mode.equals("stddev"))
                newResult.addChild(new LeafRecordNode(key, evalx + " " + fig.mean() + " " + fig.stddev()));
              else if(mode.equals("range"))
                newResult.addChild(new LeafRecordNode(key, evalx + " " + fig.mean() + " " + fig.min() + " " + fig.max()));
              else
                throw Exceptions.unknownCase(mode);
            }
          }
        }
        else if(name.equals("flushplot")) {
          // Purpose: call children commands, which might add to the plot.
          // After they return, send the mandate and reset the plot.
          // Arguments: none
          localEnv.getCmdEnv().flushPlot();
          newResult = result;
        }
        else if(name.equals("plottime") || name.equals("plothist") || name.equals("plotscatter")) {
          // Purpose: add the double values to the plotter.
          // Arguments: lots
          String[] names = new String[] {"xcol", "ycol", "zcol", "wcol"};
          names = ListUtils.append(names, GnuPlotter.Plot.propertyNames);
          parser.setNames(names).parse(bindings);
          
          // Figure out which plot we want to use
          String plotKey = result.getDescription(RecordNode.DescriptionType.human).replaceAll("\t", " ");
          GnuPlotter plotter = localEnv.getPlotter();
          GnuPlotter.Plot plot;
               if(name.equals("plotscatter")) plot = plotter.getScatter();
          else if(name.equals("plottime"))    plot = plotter.getTimeSeries();
          else if(name.equals("plothist"))    plot = plotter.getHistogram();
          else throw Exceptions.unknownCase;
          plot.setProperties(parser);

          // Columns to plot
          int xcol = parser.getInt("xcol", 0);
          int ycol = parser.getInt("ycol", 1);
          int zcol = parser.getInt("zcol", 2);
          int wcol = parser.getInt("wcol", 3);

          // Add the points
          int numGoodPoints = 0;
          for(RecordNode node : result.getChildren()) {
            double[] p = StrUtils.doubleSplit(RecordNodeUtils.getPrimaryValue(node));
            assert p.length > 0;
            double x = ListUtils.get(p, xcol, Double.NaN);
            double y = ListUtils.get(p, ycol, Double.NaN);
            double z = ListUtils.get(p, zcol, Double.NaN);
            double w = ListUtils.get(p, wcol, Double.NaN);
            if(name.equals("plotscatter")) { // (x, y) 2D or (x, y, z) 3D
              if(xcol < p.length && ycol < p.length && zcol < p.length) {
                if(plot.addPoint(plotKey, x, y, z)) numGoodPoints++;
              }
              else if(xcol < p.length && ycol < p.length) {
                if(plot.addPoint(plotKey, x, y)) numGoodPoints++;
              }
            }
            else if(name.equals("plottime")) { // (value) 1D or (time, value) 2D or (time, value, value) 3D or (time, value, +dvalue, -dvalue) 4D
              if(xcol < p.length && ycol < p.length && zcol < p.length && wcol < p.length) {
                if(plot.addPoint(plotKey, x, y, z, w)) numGoodPoints++;
              }
              else if(xcol < p.length && ycol < p.length && zcol < p.length) {
                if(plot.addPoint(plotKey, x, y, z)) numGoodPoints++;
              }
              else if(xcol < p.length && ycol < p.length) {
                if(plot.addPoint(plotKey, x, y)) numGoodPoints++;
              }
              else if(xcol < p.length) {
                if(plot.addPoint(plotKey, x)) numGoodPoints++;
              }
            }
            else if(name.equals("plothist")) { // (value) 1D
              if(xcol < p.length) {
                if(plot.addPoint(plotKey, x)) numGoodPoints++;
              }
            }
          }
          newFullResult.addChild(new LeafRecordNode(name, ""+numGoodPoints));
        }
        else if(name.equals("partialavg")) {
          // Purpose: Computes the partial average of the n data points in front
          // Arguments: window
          parser.setNames("window").parse(bindings);
          int window = parser.getInt("window", Integer.MAX_VALUE);
          // Maintain the partial sum in a window of the given size
          double sum = 0;
          int n = 0; // Number of finite values in the window
          List<RecordNode> children = result.getChildren();
          for(int i = 0; i < children.size(); i++) {
            RecordNode node = children.get(i);
            double x = node.getDoubleValue();
            if(NumUtils.isFinite(x)) { sum += x; n++; }
            if(i-window >= 0) { // Remove 
              double oldx = children.get(i-window).getDoubleValue();
              if(NumUtils.isFinite(oldx)) { sum -= oldx; n--; }
            }
            newFullResult.addChild(node.shallowCopy(node.getKey(), ""+(sum/n)));
          }
        }
        else if(name.equals("sort")) {
          // Purpose: sort the children
          // Arguments: keep only top n, (or if n is negative, bottom -n)
          parser.setNames("n").parse(bindings);
          boolean reverse = false;
          int n = parser.getInt("n", result.numChildren());
          if(n < 0) { n = -n; reverse = true; }
          if(n > result.numChildren()) n = result.numChildren();

          // Sort
          List<Pair<Double, RecordNode>> pairs =
            new ArrayList<Pair<Double, RecordNode>>();
          for(RecordNode node : result.getChildren())
            pairs.add(new Pair<Double, RecordNode>(node.getDoubleValue(), node));
          ListUtils.partialSort(pairs, n,
              reverse ? new Pair.ReverseFirstComparator<Double, RecordNode>()
                      : new Pair.FirstComparator<Double, RecordNode>());

          // Put back
          for(int i = 0; i < n; i++)
            newFullResult.addChild(pairs.get(i).getSecond());
        }
        else
          throw new RuntimeException("Unknown command: " + name);
      }

      // Apply the hint
      return localEnv.applyHint(newResult);
    }
  }

  // The returned RecordNode semantically is a list
  public RecordNode exec(LocalCommandEnv localEnv) {
    return new ExecState(localEnv).exec();
  }

  public RecordNode withoutChildren() {
    return new FuncCommandNode(name, args, null, applyToChildren);
  }
}
