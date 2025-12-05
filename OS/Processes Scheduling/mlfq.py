from collections import deque
import heapq

# -----------------------------------------
# Helper: Compute metrics after scheduling
# -----------------------------------------
def compute_metrics(processes):
    for process in processes:
        # TAT = Turnaround Time = Completion Time - Arrival Time
        process["tat"] = process["ct"] - process["at"]
        # WT = Waiting Time = Turnaround Time - Burst Time
        process["wt"] = process["tat"] - process["bt"]
        # RR = Response Ratio = (Waiting Time + Burst Time) / Burst Time
        process["rr"] = round((process["wt"] + process["bt"]) / process["bt"], 2)

    average_turnaround_time = sum(process["tat"] for process in processes) / len(processes)
    average_waiting_time = sum(process["wt"] for process in processes) / len(processes)

    return average_turnaround_time, average_waiting_time


# --------------------------------------------------
# MLQ Scheduling (each queue strictly separated)
# --------------------------------------------------
def MLQ(processes, queue0_quantum):
    # Separate processes into their assigned queues
    queue_0_processes = [process for process in processes if process["queue"] == 0]
    queue_1_processes = [process for process in processes if process["queue"] == 1]
    queue_2_processes = [process for process in processes if process["queue"] == 2]

    current_time = 0

    # --- Queue 0: Round Robin (with quantum = queue0_quantum) ---
    round_robin_queue = deque(queue_0_processes)
    while round_robin_queue:
        current_process = round_robin_queue.popleft()
        execution_time = min(queue0_quantum, current_process["rem"])
        current_time = max(current_time, current_process["at"]) + execution_time
        current_process["rem"] -= execution_time

        if current_process["rem"] == 0:
            current_process["ct"] = current_time
        else:
            round_robin_queue.append(current_process)

    # --- Queue 1: Round Robin (with quantum = 8) ---
    round_robin_queue = deque(queue_1_processes)
    while round_robin_queue:
        current_process = round_robin_queue.popleft()
        execution_time = min(8, current_process["rem"])
        current_time = max(current_time, current_process["at"]) + execution_time
        current_process["rem"] -= execution_time

        if current_process["rem"] == 0:
            current_process["ct"] = current_time
        else:
            round_robin_queue.append(current_process)

    # --- Queue 2: Shortest Remaining Time First (SRTF) ---
    ready_queue = []
    queue_2_processes = sorted(queue_2_processes, key=lambda process: process["at"])
    process_index = 0

    while process_index < len(queue_2_processes) or ready_queue:
        if not ready_queue:
            current_time = max(current_time, queue_2_processes[process_index]["at"])

        # Add all processes that have arrived to the ready queue
        while process_index < len(queue_2_processes) and queue_2_processes[process_index]["at"] <= current_time:
            heapq.heappush(ready_queue, (queue_2_processes[process_index]["rem"], queue_2_processes[process_index]))
            process_index += 1

        remaining_time, current_process = heapq.heappop(ready_queue)
        current_time += 1
        current_process["rem"] -= 1

        if current_process["rem"] == 0:
            current_process["ct"] = current_time
        else:
            heapq.heappush(ready_queue, (current_process["rem"], current_process))

    average_turnaround_time, average_waiting_time = compute_metrics(processes)
    return processes, average_turnaround_time, average_waiting_time


# --------------------------------------------------
# MLFQ Scheduling
# --------------------------------------------------
def MLFQ(processes, queue0_quantum):
    current_time = 0
    high_priority_queue = deque()  # Queue 0: Highest priority
    medium_priority_queue = deque()  # Queue 1: Medium priority
    low_priority_queue = []  # Queue 2: Lowest priority (uses heap for SRTF)

    # Sort processes by arrival time
    processes = sorted(processes, key=lambda process: process["at"])
    next_process_index = 0

    def add_arrivals():
        """Add all processes that have arrived to the highest priority queue"""
        nonlocal next_process_index
        while next_process_index < len(processes) and processes[next_process_index]["at"] <= current_time:
            high_priority_queue.append(processes[next_process_index])
            next_process_index += 1

    # Continue until all processes are processed
    while next_process_index < len(processes) or high_priority_queue or medium_priority_queue or low_priority_queue:
        add_arrivals()

        # ------------ Queue 0: Round Robin (Highest Priority) ------------
        if high_priority_queue:
            current_process = high_priority_queue.popleft()
            execution_time = min(queue0_quantum, current_process["rem"])
            current_time += execution_time
            current_process["rem"] -= execution_time

            add_arrivals()

            if current_process["rem"] > 0:
                # Process not finished, move to lower priority queue
                medium_priority_queue.append(current_process)
            else:
                # Process completed
                current_process["ct"] = current_time
            continue

        # ------------ Queue 1: Round Robin with quantum 8 (Medium Priority) ------------
        if medium_priority_queue:
            current_process = medium_priority_queue.popleft()
            execution_time = min(8, current_process["rem"])
            current_time += execution_time
            current_process["rem"] -= execution_time

            add_arrivals()

            if current_process["rem"] > 0:
                # Process not finished, move to lowest priority queue
                heapq.heappush(low_priority_queue, (current_process["rem"], current_process))
            else:
                # Process completed
                current_process["ct"] = current_time
            continue

        # ------------ Queue 2: Shortest Remaining Time First (Lowest Priority) ------------
        if low_priority_queue:
            remaining_time, current_process = heapq.heappop(low_priority_queue)
            current_time += 1
            current_process["rem"] -= 1

            add_arrivals()

            if current_process["rem"] > 0:
                # Process not finished, put back in queue
                heapq.heappush(low_priority_queue, (current_process["rem"], current_process))
            else:
                # Process completed
                current_process["ct"] = current_time
            continue

        current_time += 1  # CPU is idle, advance time

    average_turnaround_time, average_waiting_time = compute_metrics(processes)
    return processes, average_turnaround_time, average_waiting_time


# --------------------------------------------------
# Example Input
# --------------------------------------------------

processes = [
    {"pid": "P1", "at": 0, "bt": 18, "rem": 18, "queue": 0},
    {"pid": "P2", "at": 2, "bt": 5,  "rem": 5,  "queue": 1},
    {"pid": "P3", "at": 4, "bt": 12, "rem": 12, "queue": 2},
    {"pid": "P4", "at": 6, "bt": 7,  "rem": 7,  "queue": 0},
]

# ---------------------------------------
# Run MLQ
# ---------------------------------------
mlq_result, mlq_average_turnaround_time, mlq_average_waiting_time = MLQ(
    [process.copy() for process in processes], queue0_quantum=6
)

print("\n---- MLQ RESULTS ----")
print("PID | AT | BT | CT | TAT | WT | RR")
for process in mlq_result:
    print(process["pid"], process["at"], process["bt"], process["ct"], process["tat"], process["wt"], process["rr"])
print("Average TAT:", mlq_average_turnaround_time)
print("Average WT:", mlq_average_waiting_time)

# ---------------------------------------
# Run MLFQ
# ---------------------------------------
mlfq_result, mlfq_average_turnaround_time, mlfq_average_waiting_time = MLFQ(
    [process.copy() for process in processes], queue0_quantum=6
)

print("\n---- MLFQ RESULTS ----")
print("PID | AT | BT | CT | TAT | WT | RR")
for process in mlfq_result:
    print(process["pid"], process["at"], process["bt"], process["ct"], process["tat"], process["wt"], process["rr"])
print("Average TAT:", mlfq_average_turnaround_time)
print("Average WT:", mlfq_average_waiting_time)