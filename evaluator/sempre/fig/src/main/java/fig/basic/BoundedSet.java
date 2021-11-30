package fig.basic;

import java.util.*;

/**
 * A bounded set maintains at most K items.
 * Keeps the ones with the highest values.
 */
public class BoundedSet<T> {
  // priority = -value, so the smallest value things get booted first
  PriorityQueue<T> queue;
  int capacity;

  public BoundedSet(int capacity) {
    this.capacity = capacity;
    this.queue = new PriorityQueue(capacity+1);
  }

  public void add(T x, double value) {
    if(queue.size() < capacity || value > -queue.getPriority())
      queue.add(x, -value);
    // Maintain capacity
    while(queue.size() > capacity) queue.next();
  }

  // Return in decreasing value
  public List<T> removeAll() {
    List<T> list = new ArrayList();
    while(queue.hasNext())
      list.add(queue.next());
    Collections.reverse(list);
    return list;
  }
}

