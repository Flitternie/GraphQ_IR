package fig.basic;

public class LispTree extends AbstractLispTree<LispTree> {
  protected LispTree newTree() { return new LispTree(); }
  public static LispTree proto = new LispTree();
}
