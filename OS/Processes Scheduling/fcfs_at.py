def fcfs_at(pid,at,bt):
    n = len(pid)

    #sort processes by arrival time
    for i in range(n):
        for j in range(i+1,n):
            if at[j]<at[i]:             #swap higher with lower
                at[i], at[j] = at[j], at[i]
                bt[i], bt[j] = bt[j], bt[i]
                pid[i], pid[j] = pid[j], pid[i]

    ct = [0] * n
    tat = [0] * n
    wt = [0] * n

    time = 0

    for i in range(n):
        if time<at[i]:     #if cpu idle assign time to next at
            time = at[i]

        time = time + bt[i] #cpu runs process
        ct[i]= time         #time stored to ct

    for i in range(n):      #normal calc
        tat[i] = ct[i]-at[i]
        wt[i] = tat[i]-bt[i]

    print("PID | AT | BT | CT | TAT | WT")
    print("-----------------------------------")
    for i in range(n):
        print(pid[i], " |", at[i], " |", bt[i], " |", ct[i], " |", tat[i], " |", wt[i])

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print("\nAverage WT :", avg_wt)
    print("Average TAT:", avg_tat)

    return ct, tat, wt

if __name__=="__main__":
    pid = [1, 2, 3, 4]
    at  = [0, 1, 2, 3]
    bt  = [5, 3, 8, 6]

    ct, wt, tat = fcfs_at(pid, at, bt)
    print("ct:",ct)
    print("tat:",tat)
    print("wt:",wt)