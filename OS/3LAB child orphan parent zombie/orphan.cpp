#include <iostream>
#include <unistd.h>
#include <sys/types.h>
using namespace std;

// Simple bubble sort
void sortArray(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;
    cout << "Enter number of integers: ";
    cin >> n;

    int arr[n];
    cout << "Enter integers: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    pid_t pid = fork();  // create child process

    if (pid < 0) {
        cout << "Fork failed!" << endl;
        return 1;
    }
    else if (pid == 0) {
        // -------- Child Process --------
        cout << "\n[Child] PID: " << getpid() << ", Parent PID: " << getppid() << endl;
        cout << "[Child] Sleeping for 10 seconds to allow parent to exit...\n";
        sleep(10);  // wait so parent can die first

        cout << "[Child] After sleep, new Parent PID: " << getppid() << endl;
        cout << "[Child] Now performing sorting...\n";

        sortArray(arr, n);
        cout << "[Child] Sorted array: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;

        cout << "[Child] Exiting now.\n";
    }
    else {
        // -------- Parent Process --------
        cout << "\n[Parent] PID: " << getpid() << ", Child PID: " << pid << endl;
        cout << "[Parent] Sorting array...\n";
        sortArray(arr, n);

        cout << "[Parent] Sorted array: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;

        cout << "[Parent] Exiting immediately so that child becomes orphan.\n";
        // Parent exits quickly
    }

    return 0;
}