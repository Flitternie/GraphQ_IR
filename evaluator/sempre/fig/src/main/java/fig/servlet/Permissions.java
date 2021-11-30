package fig.servlet;

import java.io.*;

public class Permissions {
  public Permissions(boolean canDo, File accessRootDir) {
    this.canModify = canDo;
    this.canExecute = canDo;
    this.accessRootDir = accessRootDir;
  }

  public void checkCanModify() throws MyException {
    if(!canModify) throw new MyException("Can't modify");
  }

  public void checkCanExecute() throws MyException {
    if(!canExecute) throw new MyException("Can't execute");
  }

  public String toString() {
    return String.format("modify = %s, execute = %s, access from %s",
      canModify, canExecute, accessRootDir);
  }

  public boolean canModify; // Can modify anything
  public boolean canExecute; // Execute arbitrary commands
  public File accessRootDir; // Can only view files starting from here
}
