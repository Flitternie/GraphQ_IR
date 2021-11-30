package fig.servlet;

import java.io.*;

public class FilenameFilterBank {
  // Composition of two filename filters
  public static class Compose implements FilenameFilter {
    public Compose(FilenameFilter f1, FilenameFilter f2) {
      this.f1 = f1;
      this.f2 = f2;
    }
    public boolean accept(File dir, String name) {
      return f1.accept(dir, name) && f2.accept(dir, name);
    }
    private FilenameFilter f1, f2;
  }

  // Match a filename with a regular expression
  public static class Regex implements FilenameFilter {
    public Regex(String match, boolean positive) {
      this.match = match;
      this.positive = positive;
    }
    public boolean accept(File dir, String name) {
      return name.matches(match) == positive;
    }
    private String match;
    private boolean positive;
  }

  // Match by file type
  public static class FileType implements FilenameFilter {
    public FileType(boolean allowFiles, boolean allowDirs) {
      this.allowFiles = allowFiles;
      this.allowDirs = allowDirs;
    }
    public boolean accept(File dir, String name) {
      File path = new File(dir, name);
      if(!allowFiles && path.isFile()) return false;
      if(!allowDirs && path.isDirectory()) return false;
      return true;
    }
    private boolean allowFiles, allowDirs;
  }

  public static FilenameFilter onlyDir() { return new FileType(false, true); }
  public static FilenameFilter onlyFile() { return new FileType(true, false); }
}
