package fig.record;

import java.io.*;
import java.util.*;
import fig.basic.*;

/*
 * A mandate consists of commands and files that
 * the server sends to the client to be run.
 */
public class Mandate implements Serializable {
  private final static int serialVersionUID = 42;
  private final static String tmpTag = "#<TMP>#";
  private boolean cleanup;
  
  // Encapsulates a file; name/contents may contain tmpTag,
  // which needs to be replaced
  public static class FileBundle implements Serializable {
    private final static int serialVersionUID = 42;

    public final String path;
    // Exactly of the following is non-null
    public final String charContents;
    public final byte[] byteContents;
    public final boolean containsFileRef;

    public FileBundle(String path, String charContents, boolean containsFileRef) {
      this.path = path;
      this.charContents = charContents;
      this.byteContents = null;
      this.containsFileRef = containsFileRef;
    }
    public FileBundle(String path, byte[] byteContents) {
      this.path = path;
      this.charContents = null;
      this.byteContents = byteContents;
      this.containsFileRef = false;
    }
    public FileBundle(String path, File byteSource) {
      this.path = path;
      try {
        InputStream in = new FileInputStream(byteSource);
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        IOUtils.copy(in, out);
        this.charContents = null;
        this.byteContents = out.toByteArray();
        this.containsFileRef = false;
      } catch(IOException e) {
        throw new RuntimeException(e);
      }
    }
    public FileBundle(String path, List charContentsList, boolean containsFileRef) {
      this.path = path;
      this.charContents = StrUtils.join(charContentsList, "\n")
        + (charContentsList.size() > 0 ? "\n" : "");
      this.byteContents = null;
      this.containsFileRef = containsFileRef;
    }

    public String getActualPath(File tempDir) {
      return path.replaceAll(tmpTag, tempDir.toString());
    }
    private String getActualCharContents(File tempDir) {
      if(containsFileRef)
        return charContents.replaceAll(tmpTag, tempDir.toString());
      return charContents;
    }

    public void writeContents(File tempDir) {
      String path = getActualPath(tempDir);
      if(charContents != null) {
        // Write characters (but replacing file references appropriately)
        PrintWriter out = IOUtils.openOutHard(path);
        out.print(getActualCharContents(tempDir));
        out.close();
      }
      else if(byteContents != null) {
        // Write raw bytes
        try {
          OutputStream out = new FileOutputStream(path);
          out.write(byteContents);
          out.close();
        } catch(IOException e) {
          throw new RuntimeException("Failed to write to " + path);
        }
      }
      else
        throw new RuntimeException("Both byte and char contents can't be emptpy");
    }

    public void delete(File tempDir) {
      new File(getActualPath(tempDir)).delete();
    }
  }

  private List<String> commands;
  private List<FileBundle> files;
  private List<Mandate> mandates;

  public List<FileBundle> getFiles() { return files; }

  public Mandate(boolean cleanup) {
    this.cleanup = cleanup;
    this.commands = new ArrayList<String>();
    this.files = new ArrayList<FileBundle>();
    this.mandates = new ArrayList<Mandate>();
  }

  public String tempifyFileName(String name) {
    // TODO: make returned files unique?
    if(name == null) return tmpTag;
    return tmpTag+"/"+name;
  }

  public void setCleanup(boolean cleanup) { this.cleanup = cleanup; }

  public void addCommand(String cmd) { commands.add(cmd); }
  // The path is typically returned by tempifyFileName
  public void addFile(FileBundle file) { files.add(file); }
  public void addMandate(Mandate mandate) { mandates.add(mandate); }

  public void execute(String baseTempDir) {
    if(commands.size() > 0) {
      // Create a temporary directory 
      File tempDir = new File(baseTempDir, "tmp."+(new Random()).nextInt(10000000));
      tempDir.mkdir();

      // Write the files
      for(FileBundle file : files)
        file.writeContents(tempDir);

      // Run the commands
      for(String cmd : commands)
        Utils.systemHard(cmd.replaceAll(tmpTag, tempDir.toString()));

      // Cleanup
      if(cleanup) {
        for(FileBundle file : files)
          file.delete(tempDir);
        tempDir.delete();
      }
    }

    // Recurse on children
    for(Mandate child : mandates) child.execute(baseTempDir);
  }

  public static final Mandate empty = new Mandate(true);
}
