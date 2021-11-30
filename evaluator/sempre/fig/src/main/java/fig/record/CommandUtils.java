package fig.record;

import fig.basic.*;
import java.util.*;

/**
 * Utilities for parsing commands.
 */
public class CommandUtils {
  public static CommandNode parse(String line, CommandEnv cmdEnv) {
    // Apply macros
    line = substituteMacro(line, cmdEnv.getGlobalEnv());
    // Remove extra whitespace
    line = line.replaceAll("\\s+", " ").trim();

    if(line.equals("")) return FuncCommandNode.noOpCmd;

    // Try parsing it as various things
    CommandNode cmd;
    if((cmd = parseDefineMacro(line)) != null)   return cmd;
    if((cmd = parseRecordCommand(line)) != null) return cmd;

    throw new RuntimeException("Can't parse: " + line);
  }

  // Applies to macros $foo(a,b,c) or commands !bar(a,b,c) calls
  // Return: a list of
  //  - prefix ($ or ! or !!)
  //  - name of macro or command,
  //  - arguments if success or null if failure
  // initChar is either $ for macros or ! for commands
  // Start parsing at position i in string s
  private static List<String> parseCall(String[] prefixes, String s, IntRef iRef) {
    int i = (iRef == null ? 0 : iRef.value); // Starting position
    List<String> args = new ArrayList();

    // Extract the prefix
    for(String prefix : prefixes) {
      if(s.substring(i).startsWith(prefix)) {
        args.add(prefix);
        i += prefix.length();
        break;
      }
    }
    if(args.size() == 0) return null; // No prefix found

    // Extract the name
    int j = i;
    while(j < s.length() && Character.isLetterOrDigit(s.charAt(j))) j++;
    if(i == j) return null; // No name found
    args.add(s.substring(i, j));
    i = j;

    // Get the arguments if they exist
    int indent = 1;
    if(i < s.length() && s.charAt(i) == '(') {
      // Find the closing brace (but if see open paren, then increase indent)
      j = i;
      do {
        j = StrUtils.indexOfIgnoreEscaped(s, "()", j+1);
        if(j == -1) return null; // No matching brace
        if(s.charAt(j) == '(') indent++;
        else indent--;
      } while(indent > 0);
      // Get the arguments between ( and )
      args.addAll(StrUtils.splitIgnoreEscaped(s.substring(i+1, j), ","));
      i = j+1;
    }
    if(iRef != null) iRef.value = i;

    //System.out.println(StrUtils.join(args, " ||| " ));

    return args;
  }

  private static String substituteMacro(String line, GlobalEnv globalEnv) {
    // Max out to prevent infinite loops
    for(int t = 0; t < 10; t++) {
      String newLine = substituteMacroOnePass(line, globalEnv);
      if(newLine.equals(line)) return line;
      line = newLine;
    } 
    return line;
  }

  private static String substituteMacroOnePass(String line, GlobalEnv globalEnv) {
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < line.length();) {
      // Do macro substitution if there is one
      IntRef iRef = new IntRef(i);
      List<String> args = parseCall(new String[] {"$"}, line, iRef);
      if(args != null) {
        String var = args.get(1); // Macro name
        String val = globalEnv.getVar(var); // Body of the macro
        if(val == null) throw new RuntimeException("Variable undefined: " + var);
        val = expandMacro(val, args.subList(2, args.size()));
        sb.append(val);
        i = iRef.value;
      }
      else {
        // Just chug along the string
        sb.append(line.charAt(i));
        i++;
      }
    }
    return sb.toString();
  }

  private static String expandMacro(String s, List<String> args) {
    StringBuilder buf = new StringBuilder();
    int i = 0;
    while(true) {
      int j = s.indexOf('\\', i);
      if(j == -1) j = s.length();
      buf.append(s.substring(i, j));
      if(j == s.length()) break;
      i = j;

      // Get the number after \
      j++;
      while(j < s.length() && Character.isDigit(s.charAt(j))) j++;
      if(i+1 < j) { // If there is a number after the slash
        int argIndex = Integer.parseInt(s.substring(i+1, j))-1;
        if(argIndex < args.size()) buf.append(args.get(argIndex));
      }
      else
        buf.append(s.substring(i, j));
      i = j;
    }
    return buf.toString();
  }

  private static boolean isEndOfChain(String s) {
    return s.equals("}") || s.equals("/");
  }

  /**
   * Converts a string into a command node.
   * The syntax is a bit weird, is tailored towards long deep structures.
   * Two adjustments that we make by default, which are aesthetically not
   * so nice but make life easier for the user.
   *  - Flatten all filter commands that have a filter command as its child.
   *    This is a bit unpleasant; see isFilterNodeStr.
   *  - Any leaf filter command automatically gets a removeChildren attached
   *    at the end (so that we don't get lots of output).
   */
  public static CommandNode parseRecordCommand(String line) {
    // Assume tokens are nicely space separated
    List<String> tokens = StrUtils.splitIgnoreEscaped(line, " ");
    CommandNode rootCmd = new CombineCommandNode(CombineCommandNode.CombineType.COMPOSE);
    CommandNode parentCmd = rootCmd; // Node to attach to
    List<CommandNode> pivotCmds = ListUtils.newList(rootCmd);
    String lastLabel = null;
    final CommandNode leafCmd = FuncCommandNode.identityCmd;

    for(int k = 0; k < tokens.size(); k++) {
      String s = tokens.get(k);
      java.util.regex.Matcher m;
      CommandNode cmd = null; // Node that we're going to build
      List<String> args; // Used if the token is a command

      boolean isEndOfChain = k+1 == tokens.size() || isEndOfChain(tokens.get(k+1));
      boolean flatten = false;

      // Create new pivot
      if((m = StrUtils.match("(.)?\\{", s)).matches()) {
        CombineCommandNode.CombineType type =
          CombineCommandNode.parseCombineType(m.groupCount() >= 1 ? m.group(1) : null);
        cmd = new CombineCommandNode(type);
        pivotCmds.add(cmd);
      }
      // Jump to pivot
      else if(s.equals("/")) {
        parentCmd = ListUtils.getLast(pivotCmds);
        continue;
      }
      // Jump to pivot ; weird thing is the node after this will be attached
      // at the same level as the things inside
      else if(s.equals("}")) {
        parentCmd = ListUtils.removeLast(pivotCmds);
        continue;
      }
      else if(s.equals("?")) // Keep only distinct keys at the first level
        cmd = FuncCommandNode.childKeysCmd;
      else if(s.equals("..")) // Keep distinct keys at all levels
        cmd = FuncCommandNode.keySkeletonCmd;
      else if(s.equals("...")) // Keep everything
        cmd = FuncCommandNode.identityCmd;
      // A (function) command (starts with ! or !!)
      else if((args = parseCall(new String[] {"!!", "!"}, s, null)) != null) {
        boolean applyToChildren = args.get(0).length() > 1; // if !!
        // Remove any escape characters
        for(int i = 2; i < args.size(); i++)
          args.set(i, args.get(i));
        cmd = new FuncCommandNode(args.get(1), args.subList(2, args.size()), leafCmd, applyToChildren);
      }
      // Set label to replace key
      else if((m = StrUtils.match("'(.*)'", s)).matches()) {
        lastLabel = m.group(1);
        continue;
      }
      // A filter command
      else {
        // Match key = value
        Matcher keyMatcher, valueMatcher;
        if((m = StrUtils.match("([^=<>]+)(<=|>=|<|>|==)(.+)", s)).matches()) {
          // Match key, numeric comparison on value
          keyMatcher = getMatcher(m.group(1));
          valueMatcher = new NumMatcher(m.group(2), m.group(3));
        }
        else if((m = StrUtils.match("([^=]+)=(.+)", s)).matches()) {
          // Match key and value
          keyMatcher = getMatcher(m.group(1));
          valueMatcher = getMatcher(m.group(2));
        }
        else if((m = StrUtils.match("=(.+)", s)).matches()) {
          // Match value
          keyMatcher = AllMatcher.matcher;
          valueMatcher = getMatcher(m.group(1));
        }
        else if((m = StrUtils.match("(.+)", s)).matches()) {
          // Match key
          keyMatcher = getMatcher(s);
          valueMatcher = AllMatcher.matcher;
        }
        else
          throw new RuntimeException("Bad filter string: " + s);

        cmd = new FilterCommandNode(
            new RecordNodeMatcher(keyMatcher, valueMatcher),
            isEndOfChain ? FuncCommandNode.withoutChildrenCmd : leafCmd);

        // Flatten by default (now that could change if we removeFinalFlatten())
        flatten = true;
      }

      boolean labelSpecified = lastLabel != null;

      // If specified label, then don't flatten (can always flatten manually)
      if(labelSpecified) flatten = false;

      // Now we have the command cmd that we are basically going to add
      // as the child of parentCmd.  However, there might be some
      // postprocessing we need to do.
      List<CommandNode> cmds = new ArrayList<CommandNode>(); // Youngest to oldest
      cmds.add(cmd);
      if(!StrUtils.isEmpty(lastLabel))
        cmds.add(new FuncCommandNode("key",
          Collections.singletonList(lastLabel),
          ListUtils.getLast(cmds), true));
      if(flatten)
        cmds.add(new FuncCommandNode("flatten",
          labelSpecified ? Collections.singletonList("append") : Collections.EMPTY_LIST,
          ListUtils.getLast(cmds), false));
      if(parentCmd != null) cmds.add(parentCmd);

      // Extend path down tree
      for(int i = 1; i < cmds.size(); i++) {
        if(FuncCommandNode.isImmutableCmd(cmds.get(i)))
          throw new RuntimeException("Can't add children to " + cmds.get(i));
        cmds.get(i).addChild(cmds.get(i-1));
      }
      parentCmd = cmds.get(0); // Youngest
      //if(rootCmd == null) // Set root for the first time
        //rootCmd = ListUtils.getLast(cmds);

      lastLabel = null;
    }

    return removeFinalFlatten(rootCmd);
  }

  // Remove all flatten command nodes with exactly one filter node descendent.
  // This is probably a weird generalization,
  // but in the future, we might want to do other types of processing
  // on the command structure that needs global information.
  private static CommandNode removeFinalFlatten(CommandNode cmd) {
    // Remove the flatten if the number of descendent filter nodes is 1.
    if(cmd instanceof FuncCommandNode &&
        ((FuncCommandNode)cmd).getName().equals("flatten") &&
        numDescendentFilterNodes(cmd, new IntRef(0)) == 1)
      return (CommandNode)((FuncCommandNode)cmd).getChild();

    CommandNode newCmd = (CommandNode)cmd.withoutChildren();
    for(RecordNode childCmd : cmd.getChildren()) {
      newCmd.addChild(removeFinalFlatten((CommandNode)childCmd));
    }
    return newCmd;
  }
  // Return the number of times a filter node appears
  private static int numDescendentFilterNodes(CommandNode cmd, IntRef count) {
    if(cmd != null) {
      if(cmd instanceof FilterCommandNode) count.value++;
      for(RecordNode childCmd : cmd.getChildren())
        numDescendentFilterNodes((CommandNode)childCmd, count);
    }
    return count.value;
  }

  private static Matcher getMatcher(String s) {
    java.util.regex.Matcher m;
    // Match everything
    if(s.equals("*")) return AllMatcher.matcher;
    // Regular expression
    if((m = java.util.regex.Pattern.compile("/([^,]+)/").matcher(s)).matches())
      return new RegexMatcher(m.group(1));
    // List of things to match
    if((m = java.util.regex.Pattern.compile("\\{([^}]*)\\}").matcher(s)).matches()) {
      OrMatcher matcher = new OrMatcher();
      for(String t : StrUtils.splitIgnoreEscaped(m.group(1), ","))
        matcher.addMatcher(getMatcher(t));
      return matcher;
    }
    // Must match exactly this string
    return new ExactMatcher(s);
  }

  public static CommandNode parseDefineMacro(String line) {
    java.util.regex.Pattern p = java.util.regex.Pattern.compile("(\\w+)\\s*:=\\s*(.*)");
    java.util.regex.Matcher m = p.matcher(line);
    if(!m.matches()) return null;
    return new FuncCommandNode("define",
        ListUtils.newList(m.group(1), m.group(2)), FuncCommandNode.identityCmd, false);
  }
}
