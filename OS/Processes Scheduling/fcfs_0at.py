#when AT = 0

def fcfs(pid, bt):
    n = len(pid)

    ct = [0]*n  #initialize all to 0 
    tat= [0]*n
    wt = [0]*n

    ct[0]=bt[0]    #first process completes in the same burst time

    for i in range(1,n):
        ct[i] = ct[i-1]+bt[i]

    for i in range(n):
        tat[i]=ct[i]
        wt[i]=tat[i]-bt[i]

    print("PID|BT|CT|TAT|WT")
    print("---------------------------")

    for i in range(n):
        print(pid[i],"|",bt[i],"|",ct[i],"|",tat[i],"|",wt[i])

    avg_wt = sum(wt)/n
    avg_tat = sum(tat)/n

    print("\n Avg WT:", avg_wt)
    print("\n Avg TAT:", avg_tat)

    return ct, tat, wt


if __name__=="__main__":
    pid = [1,2,3,4]
    bt = [5,3,8,6]
    ct, tat, wt = fcfs(pid, bt)
    print("ct:",ct)
    print("tat:",tat)
    print("wt",wt)