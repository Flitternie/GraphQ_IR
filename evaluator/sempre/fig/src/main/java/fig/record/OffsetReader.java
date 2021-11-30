package fig.record;

import java.io.*;
import fig.basic.*;

/**
 * A wrapper around BufferedReader.  Supports the following functionality:
 *  - Get/set the current character offset.
 *  - Read a line at a time, but also peek at the next line.
 */
public class OffsetReader {
  private String path;
  private BufferedReader reader;
  private int offset; // Logical offset (which is between currLine and nextLine)
  private String nextLine; // Lookahead

  public OffsetReader(String path) throws IOException { this(path, 0); }
  public OffsetReader(String path, int offset) throws IOException {
    this.path = path;
    this.reader = IOUtils.openIn(path);
    this.offset = 0;
    this.nextLine = doesNotExist;
    setOffset(offset);
  }

  public void close() throws IOException { reader.close(); }
  public boolean closeEasy() { return IOUtils.closeEasy(reader); }

  public String readLine() throws IOException {
    if(nextLine == doesNotExist) nextLine = reader.readLine();
    String currLine = nextLine;
    nextLine = reader.readLine();
    offset += numChars(currLine);
    return currLine;
  }
  public String peekNextLine() { return nextLine; }

  // Assue newline is one character
  public static int numChars(String line) {
    return line == null || line == doesNotExist ? 0 : line.length()+1;
  }

  public void setOffset(int newOffset) throws IOException {
    if(offset == newOffset) return; // No change
    if(newOffset > offset) { // Skip forward
      // Physical offset is after nextLine, (logical) offset is before
      int physicalOffset = offset+numChars(nextLine);
      if(newOffset < physicalOffset)
        throw new RuntimeException(
          String.format(
            "Attempted to seek to a position that is not the beginning of a line: %d<%d<%d",
            offset, newOffset, physicalOffset));
      reader.skip(newOffset - physicalOffset);
    }
    else if(newOffset < offset) { // Skip backward
      // This is rather expensive for character streams
      // since we have to scan the file one character at a time
      // Future: implement an byte-based version
      reader.close();
      this.reader = IOUtils.openIn(path);
      reader.skip(newOffset);
    }
    offset = newOffset;
    nextLine = doesNotExist;
  }

  public int getOffset() { return offset; }
  public String getPath() { return path; }

  // null is reserved for end of file
  private static final String doesNotExist = "doesNotExist";
}
