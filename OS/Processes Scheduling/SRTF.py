n = int(input("Enter number of processes: "))

pid = []
at  = []
bt  = []

for i in range(n):
    pid.append(int(input("Enter PID: ")))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

rt  = bt[:]          # remaining time
ct  = [0]*n
tat = [0]*n
wt  = [0]*n
done = [0]*n

time = 0
completed = 0

# ---- SRTF logic ----
while completed < n:
    idx = -1
    mn = 100000

    # find process with shortest remaining time
    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if rt[i] < mn:
                mn = rt[i]
                idx = i

    if idx == -1:       # no process arrived
        time += 1
        continue

    # execute for 1 unit of time
    rt[idx] -= 1
    time += 1

    # if process finishes
    if rt[idx] == 0:
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        done[idx] = 1
        completed += 1

# ---- Output ----
print("\nPID AT BT CT TAT WT")
for i in range(n):
    print(pid[i], at[i], bt[i], ct[i], tat[i], wt[i])