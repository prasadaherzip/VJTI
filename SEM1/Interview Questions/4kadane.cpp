#include <iostream>
#include <climits>
using namespace std;

int main() {
    int arr[] = {2, 3, -8, 7, -1, 2, 3};
    int n = sizeof(arr)/sizeof(arr[0]);

    int max_sum = arr[0], current_sum = arr[0];

    for (int i = 1; i < n; i++) {
        current_sum = max(arr[i], current_sum + arr[i]);
        max_sum = max(max_sum, current_sum);
    }

    cout<< "Max Subarray Sum: " << max_sum <<endl;
    return 0;
}