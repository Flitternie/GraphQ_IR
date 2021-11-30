package fig.servlet;

import java.util.*;
import fig.basic.*;

/**
 * Implements a three queues of items to call update() on.
 * Basic strategy:
 * When we refresh an item,
 * Things that are immediately displayed go in high priority.
 * Things that could be displayed (like probing new entries) go in medium priority.
 * Children go in low priority.
 */
public class UpdateQueue {
  public static class Priority {
    private int value;

    private Priority(int value) { this.value = value; }
    
    public Priority next() {
      if(this == HIGH) return MED;
      if(this == MED) return LOW;
      return LOW;
    }

    public String toString() { return ""+value; }

    public static Priority HIGH = new Priority(0);
    public static Priority MED = new Priority(1);
    public static Priority LOW = new Priority(2);
  }

  private LinkedList<Item> queues[];
  private IdentityHashMap<Item, Priority> priorities; // Which queue does an item go in
  // Set of enqueued items; make sure we don't enqueue something twice; cleared
  // once in a while.
  private Set<Item> enqueuedItems;

  public UpdateQueue() {
    this.queues = new LinkedList[3];
    for(int i = 0; i < 3; i++)
      this.queues[i] = new LinkedList<Item>();
    this.priorities = new IdentityHashMap<Item, Priority>();
    this.enqueuedItems = new HashSet();
  }

  // Return total number of items in a queue
  public synchronized int queueSize() {
    int sum = 0;
    for(int i = 0; i < 3; i++)
      sum += queues[i].size();
    return sum;
  }

  private int priorityToIndex(Priority priority) {
    if(priority == Priority.HIGH) return 0;
    if(priority == Priority.MED) return 1;
    if(priority == Priority.LOW) return 2;
    throw Exceptions.unknownCase;
  }

  private Priority indexToPriority(int i) {
    if(i == 0) return Priority.HIGH;
    if(i == 1) return Priority.MED;
    if(i == 2) return Priority.LOW;
    throw Exceptions.unknownCase;
  }

  private synchronized void removeItem(Item item) {
    Priority priority = priorities.remove(item);
    if(priority != null)
      queues[priorityToIndex(priority)].remove(item);
  }

  public synchronized void enqueue(Item item, Priority priority) {
    if(enqueueHelper(item, priority))
      if(ServletLogInfo.logUpdates)
        ServletLogInfo.logs("UpdateQueue(+" + priority + ") " + item.getTrail().toDisplayString());
  }

  // Return if there was a modification to the queue
  private synchronized boolean enqueueHelper(Item item, Priority priority) {
    if(item.isDead) return false; // Skip dead items
    // Don't do this because we want to preempt lower priority things
    //if(enqueuedItems.contains(item)) return false; // Already enqueued 
    enqueuedItems.add(item);
    Priority oldPriority = priorities.get(item);
    if(oldPriority == priority) return false; // No change
    removeItem(item);
    queues[priorityToIndex(priority)].addLast(item);
    priorities.put(item, priority);
    return true;
  }

  public synchronized void merge(UpdateQueue queue) {
    for(int i = 0; i < 3; i++) {
      for(Item item : queue.queues[i])
        enqueueHelper(item, indexToPriority(i));
    }
  }

  public synchronized Pair<Item, Priority> dequeue() {
    for(int i = 0; i < 3; i++) {
      if(queues[i].size() == 0) continue;
      Item item = queues[i].removeFirst();
      Priority priority = priorities.remove(item);
      if(ServletLogInfo.logUpdates)
        ServletLogInfo.logs("UpdateQueue(-" + indexToPriority(i) + ") " + item.getTrail().toDisplayString());
      return new Pair<Item, Priority>(item, priority);
    }
    return null;
  }

  public synchronized void clearEnqueued() { enqueuedItems.clear(); }

  public String toString() {
    return String.format("UpdateQueue(%d/%d/%d items)",
        queues[0].size(), queues[1].size(), queues[2].size());
  }
}
