#include <iostream> 
#include <unistd.h>
#include <sys/types.h>
using namespace std;

// Simple bubble sort function
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

    pid_t pid = fork();  // create child processping parent alive for 20 seconds..." << endl;
//         cout << "[Parent] Run 'ps -el | grep zombie' in another terminal to see child as zombie.\n";

//         // Parent sleeps while child is already finished

    if (pid < 0) {
        cout << "Fork failed!" << endl;
        return 1;
    }
    else if (pid == 0) {
        // -------- Child Process --------
        cout << "\n[Child] PID: " << getpid() << ", Parent PID: " << getppid() << endl;
        sortArray(arr, n);
        cout << "[Child] Sorted array: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;
        cout << "[Child] Exiting now...\n";
    }
    else {
        // -------- Parent Process --------
        cout << "\n[Parent] PID: " << getpid() << ", Child PID: " << pid << endl;
        sortArray(arr, n);
        cout << "[Parent] Sorted array: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;

        cout << "\n[Parent] Not calling wait(), keeping parent alive for 20 seconds..." << endl;
        cout << "[Parent] Run 'ps -el | grep zombie' in another terminal to see child as zombie.\n";

        // Parent sleeps while child is already finished → zombie state
        sleep(20);

        cout << "[Parent] Now exiting. Zombie will be cleaned up by init.\n";
    }

    return 0;

}
