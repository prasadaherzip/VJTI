#FCFS

#Processes = [ arrival_time, burst_time(), pid]

def fcfs(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort()
    while process_list != []:
        if process_list[0] >= t:
            t+=1
            continue
        else:
            process = process+list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t
            tt = ct = process[0] 


if __name__ == "__main__":
    process_list = [[2,6,"P1"],[5,2,"P2"],[1,8,"P3"],[0,3,"P4"],[4,4,"P5"]]
    fcfs(process_list)
