#include <bits/stdc++.h>
using namespace std;

struct Process {
    int pid;    // Process ID 
    int at;     // Arrival Time 
    int bt;     // Burst Time 
    int rt;     // Remaining Time 
    int wt;     // Waiting Time 
    int tat;    // Turnaround Time 
};

void roundRobin(vector<Process>& proc, int n, int quantum) {
    queue<int> readyQueue;
    int time = 0, completed = 0;
    vector<bool> inQueue(n, false);

    // Sort processes by arrival time
    sort(proc.begin(), proc.end(), [](Process& a, Process& b) {
        return a.at < b.at;
    });

    // Push first process 
    readyQueue.push(0);
    inQueue[0] = true;

    while (completed != n) {
        if (readyQueue.empty()) {
            // No process is in queue, jump to next arrival
            for (int i = 0; i < n; i++) {
                if (proc[i].rt > 0) {
                    time = proc[i].at;
                    readyQueue.push(i);
                    inQueue[i] = true;
                    break;
                }
            }
        }

        int i = readyQueue.front();
        readyQueue.pop();

        // Process runs
        if (proc[i].rt >= quantum) {
            time += quantum;
            proc[i].rt -= quantum;
        } else {
            // Process finishes 
            time += proc[i].rt;
            proc[i].rt = 0;
            completed++;

            // Turnaround time = finish time - arrival time
            proc[i].tat = time - proc[i].at;

            // Waiting time = turnaround - burst
            proc[i].wt = proc[i].tat - proc[i].bt;
        }

        // Add newly arrived processes to the ready queue
        for (int j = 0; j < n; j++) {
            if (proc[j].rt > 0 && proc[j].at <= time && !inQueue[j]) {
                readyQueue.push(j);
                inQueue[j] = true;
            }
        }

        // If current process not finished, push it back 
        if (proc[i].rt > 0)
            readyQueue.push(i);
    }
}

int main() {
    int n, quantum;
    cout << "Enter number of processes: ";
    cin >> n;
    vector<Process> proc(n);

    for (int i = 0; i < n; i++) {
        proc[i].pid = i + 1;
        cout << "Enter Arrival Time for Process " << i + 1 << ": ";
        cin >> proc[i].at;
        cout << "Enter Burst Time for Process " << i + 1 << ": ";
        cin >> proc[i].bt;
        proc[i].rt = proc[i].bt;
        proc[i].wt = 0;
        proc[i].tat = 0;
    }

    cout << "Enter Time Quantum: ";
    cin >> quantum;

    roundRobin(proc, n, quantum);

    float totalWT = 0, totalTAT = 0;

    cout << "\nPID\tAT\tBT\tWT\tTAT\n";

    for (int i = 0; i < n; i++) {
        totalWT += proc[i].wt;
        totalTAT += proc[i].tat;
        cout << proc[i].pid << "\t"
             << proc[i].at << "\t"
             << proc[i].bt << "\t"
             << proc[i].wt << "\t"
             << proc[i].tat << "\n";
    }

    cout << "\nAverage Waiting Time = " << totalWT / n;
    cout << "\nAverage Turnaround Time = " << totalTAT / n << "\n";

    return 0;
}