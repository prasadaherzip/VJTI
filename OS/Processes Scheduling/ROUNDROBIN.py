n = int(input("Enter number of processes: "))

pid = []
at  = []
bt  = []

for i in range(n):
    pid.append(int(input("Enter PID: ")))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

tq = int(input("Enter Time Quantum: "))

rt  = bt[:]          # remaining time
ct  = [0]*n
tat = [0]*n
wt  = [0]*n
done = [0]*n

time = 0
completed = 0
queue = []

# add processes that arrive at time 0
for i in range(n):
    if at[i] == 0:
        queue.append(i)

# ---- Round Robin logic ----
while completed < n:

    if not queue:          # CPU idle
        time += 1
        for i in range(n):
            if at[i] == time and i not in queue and done[i] == 0:
                queue.append(i)
        continue

    i = queue.pop(0)       # get next process

    if rt[i] > tq:
        rt[i] -= tq
        time += tq
    else:
        time += rt[i]
        rt[i] = 0
        ct[i] = time
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        done[i] = 1
        completed += 1

    # add newly arrived processes
    for j in range(n):
        if at[j] > time - tq and at[j] <= time and done[j] == 0:
            if j not in queue:
                queue.append(j)

    if rt[i] > 0:
        queue.append(i)

# ---- Output ----
print("\nPID AT BT CT TAT WT")
for i in range(n):
    print(pid[i], at[i], bt[i], ct[i], tat[i], wt[i])