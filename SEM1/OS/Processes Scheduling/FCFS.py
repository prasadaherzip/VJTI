n = int(input("Enter number of processes: "))

pid = []
at  = []
bt  = []

for i in range(n):
    pid.append(int(input("Enter PID: ")))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

# ---- sort by arrival time (basic logic, no zip/lambda) ----
for i in range(n):
    for j in range(i+1, n):
        if at[i] > at[j]:
            at[i], at[j]   = at[j], at[i]
            bt[i], bt[j]   = bt[j], bt[i]
            pid[i], pid[j] = pid[j], pid[i]

ct  = [0]*n
tat = [0]*n
wt  = [0]*n
rt  = [0]*n
pr  = [0]*n
st  = [0]*n

time = 0

# ---- FCFS calculation ----
for i in range(n):
    st[i]  = max(time, at[i])
    ct[i]  = st[i] + bt[i]
    tat[i] = ct[i] - at[i]
    wt[i]  = tat[i] - bt[i]
    rt[i]  = st[i] - at[i]
    pr[i]  = round(tat[i] / bt[i], 2)
    time   = ct[i]

# ---- Output ----
print("\nPID\tAT\tBT\tCT\tTAT\tWT\tRT\tPR")
for i in range(n):
    print(pid[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t",
          tat[i], "\t", wt[i], "\t", rt[i], "\t", pr[i])