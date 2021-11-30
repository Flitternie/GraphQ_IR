package fig.servlet;

import java.io.*;
import java.util.*;
import fig.basic.*;

public class FileUtils {
	public static class TraverseSpec {
		public TraverseSpec(FilenameFilter retFilter, FilenameFilter descendFilter) {
			this.retFilter = retFilter;
			this.descendFilter = descendFilter;
		}
		public static TraverseSpec allowAll() { return new TraverseSpec(null, null); }
		public static TraverseSpec allowOnlyFiles() { return new TraverseSpec(FilenameFilterBank.onlyFile(), null); }
		public static TraverseSpec matchExt(String ext) {
			return new TraverseSpec(new FilenameFilterBank.Regex(".*\\."+ext, true), null);
		}
		private FilenameFilter retFilter, descendFilter;
	}

	public static List<String> getChildren(String basePath, int depth, TraverseSpec spec) {
		return getChildren(basePath, "", depth, spec);
	}

	// retFilter - specifies which files we want to return
	// descendFilter - specifies which files we want to descend down into
	public static List<String> getChildren(String basePath, String dir, int depth, TraverseSpec spec) {
		List<String> childDirs = new ArrayList<String>();
		getChildren(basePath, childDirs, dir, depth, spec);
		return childDirs;
	}

	private static void getChildren(String basePath, List<String> childDirs, String dir, int depth, TraverseSpec spec) {
		// If depth = -1, go to bottom
		if(depth == 0) return;

		// dir is relative to basePath
		// Return directories also relative to basePath
		String[] childNames = new File(basePath, dir).list();
		if(childNames == null) return;
		for(String childName : childNames) {
			String childDir = StrUtils.isEmpty(dir) ? childName : new File(dir, childName).toString();
			//WebState.logs("DIR " + childDir);
			if(spec.retFilter == null || spec.retFilter.accept(new File(basePath), childDir))
				childDirs.add(childDir);
			if(new File(basePath, childDir).isDirectory() &&
					(spec.descendFilter == null || spec.descendFilter.accept(new File(basePath), childDir)))
				getChildren(basePath, childDirs, childDir, depth-1, spec);
		}
	}

	public static String getExt(String file) {
		int i = file.lastIndexOf('.');
		if(i == -1) return "";
		return file.substring(i+1);
	}

	public static boolean isDirectory(String path) {
		return new File(path).isDirectory();
	}
	
	public static boolean isFile(String path) {
		return new File(path).isFile();
	}
}
