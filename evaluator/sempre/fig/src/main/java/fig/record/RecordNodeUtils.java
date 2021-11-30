package fig.record;

import fig.basic.*;
import java.io.*;
import java.util.*;
import java.rmi.*;
import java.rmi.server.*;

public class RecordNodeUtils {
  // Either for printing or displaying
  public static void sendRecordNodetoReceiver(RecordNode record,
      ReceiverInterface receiver) throws RemoteException {
    sendRecordNodetoReceiverHelper(record, receiver, 0, false);
  }
  public static void sendRecordNodetoReceiverHelper(RecordNode record,
      ReceiverInterface receiver, int indent, boolean displayRoot) throws RemoteException {
    if(displayRoot) {
      receiver.printOut(StrUtils.repeat("  ", indent));
      receiver.printOut(record.getDescription(RecordNode.DescriptionType.human)+"\n");
    }
    for(RecordNode child : record.getChildren())
      sendRecordNodetoReceiverHelper(child, receiver, indent+(displayRoot?1:0), true);
  }
  public static void writeRecordNode(RecordNode record, String path, boolean append) {
    PrintWriter out = append ?
      IOUtils.openOutAppendHard(path) :
      IOUtils.openOutHard(path);
    writeRecordNodeHelper(record, out, 0, false);
    out.close();
  }
  public static void writeRecordNodeHelper(RecordNode record,
      PrintWriter out, int indent, boolean displayRoot) {
    if(displayRoot) {
      out.print(StrUtils.repeat("\t", indent));
      out.print(record.getDescription(RecordNode.DescriptionType.machine)+"\n");
    }
    for(RecordNode child : record.getChildren())
      writeRecordNodeHelper(child, out, indent+(displayRoot?1:0), true);
  }

  // Jam one more key/value pair into this record node
  public static RecordNode appendKeyValue(RecordNode node, String key, String value) {
    return node.shallowCopy(node.getKey(), node.getValue() + "\t" + getDescription(key, value, RecordNode.DescriptionType.human));
  }
  // The new key/value becomes the main one
  public static RecordNode prependKeyValue(RecordNode node, String key, String value) {
    return node.shallowCopy(key, value + "\t" +
        getDescription(node.getKey(), node.getValue(), RecordNode.DescriptionType.human));
  }

  // Get a numeric value to compare (ignore everything after the tab)
  public static double getDoubleValue(RecordNode node) {
    return Utils.parseDoubleEasy(getPrimaryValue(node));
  }
  // Because each node has only one key/value and we'd like to have more,
  // we kind of hack it by putting the others in value after a tab.
  // Primary ignores the stuff after the tab.
  public static String getPrimaryValue(RecordNode node) {
    String s = node.getValue();
    if(s == null) return null;
    int i = s.indexOf('\t');
    if(i != -1) s = s.substring(0, i);
    return s;
  }

  public static String getDescription(String key, String value, RecordNode.DescriptionType type) {
    if(type == RecordNode.DescriptionType.machine)
      return key + (value == null ? "" : "\t"+value);
    else if(type == RecordNode.DescriptionType.human) {
      if(key == null) return value == null ? "" : value; // Print value if key is null
      return key + (value == null ? "" : "="+value); // Otherwise, print key
    }
    else
      throw Exceptions.unknownCase;
  }
}
