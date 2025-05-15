
/**
 * FileBackupUtility.java
 * Author: Jeremy Tarkington
 *
 * A reusable utility to copy a file or folder to a backup location with a timestamp.
 * Supports:
 * - File or directory backup
 * - Automatic timestamped folder creation
 * - Simple CLI usage or import into other projects
 */

import java.io.*;
import java.nio.file.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FileBackupUtility {

  public static void main(String[] args) {
    if (args.length < 2) {
      System.out.println("Usage: java FileBackupUtility <source_path> <destination_root>");
      System.exit(1);
    }

    Path source = Paths.get(args[0]);
    Path destRoot = Paths.get(args[1]);

    if (!Files.exists(source)) {
      System.err.println("Source does not exist: " + source);
      System.exit(1);
    }

    String timestamp = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss").format(new Date());
    Path backupPath = destRoot.resolve("backup_" + timestamp);

    try {
      if (Files.isDirectory(source)) {
        copyDirectory(source, backupPath);
      } else {
        Files.createDirectories(backupPath);
        Files.copy(source, backupPath.resolve(source.getFileName()), StandardCopyOption.REPLACE_EXISTING);
      }

      System.out.println("Backup completed: " + backupPath.toAbsolutePath());
    } catch (IOException e) {
      System.err.println("Backup failed: " + e.getMessage());
    }
  }

  public static void copyDirectory(Path sourceDir, Path targetDir) throws IOException {
    Files.walk(sourceDir).forEach(sourcePath -> {
      try {
        Path targetPath = targetDir.resolve(sourceDir.relativize(sourcePath));
        if (Files.isDirectory(sourcePath)) {
          Files.createDirectories(targetPath);
        } else {
          Files.copy(sourcePath, targetPath, StandardCopyOption.REPLACE_EXISTING);
        }
      } catch (IOException e) {
        throw new UncheckedIOException("Error copying file: " + sourcePath, e);
      }
    });
  }
}
