n = int(input("Enter number of processes: "))

pid = []
at  = []
bt  = []

for i in range(n):
    pid.append(int(input("Enter PID: ")))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

ct  = [0]*n
tat = [0]*n
wt  = [0]*n
done = [0]*n     # 0 = not done, 1 = done

time = 0
count = 0

while count < n:
    idx = -1
    mn = 100000   # very large number

    # find shortest job that has arrived
    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if bt[i] < mn:
                mn = bt[i]
                idx = i

    if idx == -1:     # no process available
        time += 1
        continue

    ct[idx] = time + bt[idx]
    tat[idx] = ct[idx] - at[idx]
    wt[idx] = tat[idx] - bt[idx]

    time = ct[idx]
    done[idx] = 1
    count += 1

print("\nPID AT BT CT TAT WT")
for i in range(n):
    print(pid[i], at[i], bt[i], ct[i], tat[i], wt[i])