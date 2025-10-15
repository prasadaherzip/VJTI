#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

// Structure to hold process information and scheduling metrics
struct Process {
    string id;
    int burstTime;      // BT: Time required for execution
    int waitingTime;    // WT: Time spent waiting in the ready queue
    int turnaroundTime; // TAT: Time from arrival to completion (BT + WT)
    int responseTime;   // RT: Time from arrival until first execution (WT for FCFS)
    double penaltyRatio;  // PR: Ratio of TAT to BT (TAT / BT)
};

// Function to simulate FCFS and calculate all metrics
void calculateFCFS(vector<Process>& processes) {
    if (processes.empty()) {
        return;
    }

    int n = processes.size();
    
    // --- 1. Calculate Individual Metrics (WT, TAT, RT, PR) ---
    
    // The completion time of the previous process is needed to determine the WT of the current process.
    int completionTime = 0;
    
    // FCFS assumes arrival time = 0 for all, and they are processed in input order.
    
    for (int i = 0; i < n; ++i) {
        // WT calculation: The waiting time of the current process is the completion time of the previous one.
        // For the first process, waiting time is 0.
        processes[i].waitingTime = completionTime;
        
        // RT calculation: For non-preemptive algorithms like FCFS, Response Time = Waiting Time.
        processes[i].responseTime = processes[i].waitingTime;

        // TAT calculation: Turnaround Time = Burst Time + Waiting Time
        processes[i].turnaroundTime = processes[i].burstTime + processes[i].waitingTime;
        
        // PR calculation: Penalty Ratio = Turnaround Time / Burst Time
        processes[i].penaltyRatio = (double)processes[i].turnaroundTime / processes[i].burstTime;

        // Update completion time for the next process
        completionTime += processes[i].burstTime;
    }

    // --- 2. Calculate Averages ---
    
    double totalWT = 0;
    double totalTAT = 0;
    double totalRT = 0;
    double totalPR = 0;

    for (const auto& p : processes) {
        totalWT += p.waitingTime;
        totalTAT += p.turnaroundTime;
        totalRT += p.responseTime;
        totalPR += p.penaltyRatio;
    }

    double avgWT = totalWT / n;
    double avgTAT = totalTAT / n;
    double avgRT = totalRT / n;
    double avgPR = totalPR / n;
    
    // Completion Time of the last process is the total completion time (TCT) of the system
    double totalCompletionTime = completionTime;
    // Throughput: Number of processes / Total Completion Time
    double throughput = (double)n / totalCompletionTime;


    // --- 3. Output Results ---

    cout << "\n=======================================================\n";
    cout << "  FCFS SCHEDULING RESULTS (Assuming Arrival Time = 0)  \n";
    cout << "=======================================================\n";
    
    // Set precision for floating point numbers
    cout << fixed << setprecision(6);

    // Print header
    cout << setw(10) << "PROCESS"
         << setw(15) << "BURST TIME"
         << setw(15) << "WAITING TIME"
         << setw(20) << "TURNAROUND TIME"
         << setw(18) << "RESPONSE TIME"
         << setw(18) << "PENALTY RATIO" << endl;
    
    // Print individual process data
    for (const auto& p : processes) {
        cout << setw(10) << p.id
             << setw(15) << p.burstTime
             << setw(15) << p.waitingTime
             << setw(20) << p.turnaroundTime
             << setw(18) << p.responseTime
             << setw(18) << p.penaltyRatio << endl;
    }

    cout << "\n-------------------------------------------------------\n";
    cout << "Average Waiting Time -- " << avgWT << endl;
    cout << "Average Turnaround Time -- " << avgTAT << endl;
    cout << "Average Response Time -- " << avgRT << endl;
    cout << "Average Penalty Ratio -- " << avgPR << endl;
    cout << "Throughput -- " << throughput << " (processes per unit time)" << endl;
    cout << "-------------------------------------------------------\n";
}

int main() {
    // F) INPUT
    int numProcesses;
    
    cout << "Enter the number of processes -- ";
    // Use the provided input value (3) directly for simulation demonstration
    numProcesses = 3; 
    cout << numProcesses << endl;

    vector<Process> processes(numProcesses);

    // Hardcoded input based on the experiment description:
    vector<int> burstTimes = {24, 3, 3}; 

    for (int i = 0; i < numProcesses; ++i) {
        processes[i].id = "P" + to_string(i);
        processes[i].burstTime = burstTimes[i];

        cout << "Enter Burst Time for Process " << i << " -- " << processes[i].burstTime << endl;
    }

    // Simulate the FCFS algorithm and display results
    calculateFCFS(processes);

    return 0;
}
