# Shortest Job First (Non-Preemptive Scheduling)

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.wt = 0
        self.tat = 0
        self.completed = False


def sjf(processes):
    n = len(processes)
    time = 0
    completed = 0
    total_wt = 0
    total_tat = 0

    while completed != n:
        # Find all processes that have arrived and are not completed
        ready = [p for p in processes if p.at <= time and not p.completed]

        if not ready:
            time += 1
            continue

        # Select process with shortest burst time
        current = min(ready, key=lambda x: x.bt)

        time += current.bt
        current.completed = True
        completed += 1

        # Calculate Turnaround and Waiting Time
        current.tat = time - current.at
        current.wt = current.tat - current.bt
        total_wt += current.wt
        total_tat += current.tat

    print("\nPID\tAT\tBT\tWT\tTAT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.wt}\t{p.tat}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")


# --- Example Input ---
n = int(input("Enter number of processes: "))
procs = []
for i in range(n):
    at = int(input(f"Enter Arrival Time for Process {i+1}: "))
    bt = int(input(f"Enter Burst Time for Process {i+1}: "))
    procs.append(Process(i+1, at, bt))

sjf(procs)