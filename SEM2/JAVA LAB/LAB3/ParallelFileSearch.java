import java.io.*;
import java.util.concurrent.*;

public class ParallelFileSearch {

    // Function to count occurrences of search text in a file
    public static int countOccurrences(File file, String searchText) {
        int count = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;

            while ((line = br.readLine()) != null) {
                int index = 0;

                while ((index = line.indexOf(searchText, index)) != -1) {
                    count++;
                    index += searchText.length();
                }
            }

        } catch (IOException e) {
            System.out.println("Error reading file: " + file.getName());
        }

        return count;
    }

    // Recursive function to traverse directories
    public static void searchDirectory(File dir, String searchText, ExecutorService executor) {

        File[] files = dir.listFiles();
        if (files == null) return;

        for (File file : files) {

            if (file.isDirectory()) {
                searchDirectory(file, searchText, executor);
            }

            else {
                executor.submit(() -> {

                    int count = countOccurrences(file, searchText);

                    if (count > 0) {
                        System.out.println("File: " + file.getAbsolutePath() +
                                " | Count: " + count);
                    }

                });
            }
        }
    }

    public static void main(String[] args) {

        if (args.length != 2) {
            System.out.println("Usage: java ParallelFileSearch <directory_path> <search_text>");
            return;
        }

        String directoryPath = args[0];
        String searchText = args[1];

        File dir = new File(directoryPath);

        if (!dir.exists() || !dir.isDirectory()) {
            System.out.println("Invalid directory path.");
            return;
        }

        ExecutorService executor = Executors.newFixedThreadPool(4);

        searchDirectory(dir, searchText, executor);

        executor.shutdown();

        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            System.out.println("Execution interrupted.");
        }

        System.out.println("Search Completed.");
    }
}