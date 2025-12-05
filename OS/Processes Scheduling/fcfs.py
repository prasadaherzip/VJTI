# P1, P2, P3, P4, P5 - Processes
# 0, 1, 2, 3, 4 - Arrival Times
# 8, 4, 3, 5,2 - Burst Times
# 2 TIME QUANTUM
# 3,1,5,2,4 priority (lower number higher priority)  

#given
arrival_time = [0,1,2,3,4]
burst_time = [8,4,3,5,2]
processes = ['P1','P2','P3','P4','P5']

#to find
completion_time = []
turnaround_time=[]
waiting_time = []
response_time =[]

n = len(processes)
time = 0

for i in range(n):
    if time < arrival_time[i]:
        time = arrival_time[i]
    time+= burst_time[i]
    completion_time.append(time)

    tat = completion_time[i]-arrival_time[i]
    wt = tat-burst_time[i]
    rt = wt

    turnaround_time.append(tat)
    waiting_time.append(wt)
    response_time.append(rt)

print(" P0 | AT | BT | CT | TAT | WT | RT |")
for i in range(n):
    print(processes[i], arrival_time[i], burst_time[i],completion_time[i], turnaround_time[i], waiting_time[i], response_time[i])

print("Average Turnaround Time = ",(sum(turnaround_time)/n))
print("Average Waiting Time = ",(sum(waiting_time)/n))
print("Average Response Time = ",(sum(response_time)/n))

