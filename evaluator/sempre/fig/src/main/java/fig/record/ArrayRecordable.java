package fig.record;

// Useful tool for recording arrays
public class ArrayRecordable<T> implements Recordable {
  private T[] array;
  private String indexLabel;
  private String valueLabel;

  public ArrayRecordable(T[] array, String indexLabel, String valueLabel) {
    this.array = array;
    this.indexLabel = indexLabel;
    this.valueLabel = valueLabel;
  }
  
  public void record(Object arg) {
    if(array.length == 0) return;
    if(array[0] instanceof Recordable) {
      for(int i = 0; i < array.length; i++)
        Record.addEmbed(indexLabel, ""+i, array[i]);
    }
    else {
      Record.setStruct(indexLabel, valueLabel);
      for(int i = 0; i < array.length; i++)
        Record.add(""+i, array[i]);
    }
  }
}
