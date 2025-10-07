#include <iostream>
#include <vector>
#include <string>

int main(int argc, char* argv[]) {
    // argc is the argument count
    // argv is the array of C-style string arguments

    std::cout << "--------------------------------------------------\n";
    std::cout << "[New Program] Hello! I am the new program loaded by execve.\n";
    
    // argv[0] is the program name, so the numbers start at argv[1].
    if (argc <= 1) {
        std::cout << "[New Program] No numbers were passed to me.\n";
        return 1;
    }

    std::cout << "[New Program] Displaying the array in reverse order: ";
    
    // Loop backwards from the last argument to the first number
    for (int i = argc - 1; i >= 1; --i) {
        std::cout << argv[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "[New Program] My job is done . Exiting.\n";
    std::cout << "--------------------------------------------------\n";

    return 0;
}