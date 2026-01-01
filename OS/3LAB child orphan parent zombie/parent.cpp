#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unistd.h>
#include <sys/wait.h>

// Simple bubble sort
void sortVector(std::vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (vec[j] > vec[j + 1]) {
                std::swap(vec[j], vec[j + 1]);
            }
        }
    }
}

int main() {
    // 1. Accept an array of integers
    int n;
    std::cout << "[Parent] Enter number of integers: ";
    std::cin >> n;

    std::vector<int> numbers(n);
    std::cout << "[Parent] Enter " << n << " integers: ";
    for (int i = 0; i < n; i++) {
        std::cin >> numbers[i];
    }

    // 2. Parent process sorts the array
    std::cout << "[Parent] Sorting the array...\n";
    sortVector(numbers);
    
    std::cout << "[Parent] Sorted array is: ";
    for(int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n[Parent] Forking a child process...\n";

    // 3. Create a child process
    pid_t pid = fork();

    if (pid < 0) {
        // Fork failed
        std::cerr << "Fork failed!" << std::endl;
        return 1;
    } else if (pid == 0) {
        // -------- This is the CHILD process --------
        std::cout << "[Child] Process created. Preparing to execute new program...\n";

        // 4. Prepare arguments for EXECVE
        std::vector<std::string> arg_strings;
        arg_strings.push_back("./child"); // program name

        for (int num : numbers) {
            arg_strings.push_back(std::to_string(num));
        }

        // Convert to char* const argv[]
        std::vector<char*> argv;
        for (const auto& s : arg_strings) {
            argv.push_back(const_cast<char*>(s.c_str()));
        }
        argv.push_back(nullptr); // NULL-terminated

        // 5. Use EXECVE to load and run the new program
        execve("./child", argv.data(), nullptr);

        // If execve returns, an error occurred.
        perror("execve failed");
        exit(1);

    } else {
        // -------- This is the PARENT process --------
        std::cout << "[Parent] Waiting for child process (PID: " << pid << ") to finish.\n";

        // Wait for child to terminate
        wait(NULL);

        std::cout << "[Parent] Child process has finished. Parent is exiting.\n";
    }

    return 0;
}