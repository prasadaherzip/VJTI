def roundrobin(proc,tq=2):
    res,prevtime,time,curr,queue,gantt,order={},-1,0,0,[],[0],[] 
    #res=completion times
    #prevtime=to track all processes that arrived after previous process and by current time
    #time=current working time
    #curr=process under consideration from process queue
    #queue=process queue (updated considering arrival time)
    #gantt=endtime for each time quantum
    #order=order for gantt chart
    while curr==0 or curr < len(queue):
        queue=queue[:-1]+[(x,proc[x][0]) for x in proc if proc[x][1]<=time and proc[x][1]>prevtime]+queue[-1:]
        #the last appended process is one that just got pre-empted, it should come after those that arrived during it
        prevtime=time

        if len(queue) == 0:
            pass
        elif queue[curr][1] > tq:
            queue.append((queue[curr][0],queue[curr][1]-tq))
            time+=tq
        else:
            time+=queue[curr][1]
            res[queue[curr][0]]=time #process burst complete

        gantt.append(time)
        order.append(queue[curr][0])
        curr+=1 #go to next process
    return res,gantt,order #res gives completion time, gantt gives time values for gantt chart, order gives order in which processes were taken

#expected format for proc parameter - {"p1":[CBT,AT],...}
p={"p1":[9,0],"p2":[5,1],"p3":[12,2],"p4":[3,4],"p5":[7,6],"p6":[4,7]}

output=roundrobin(p,3)
print(output[0]) #prints completion time list
#output[1] and output[2] used for gantt chart
#TAT,WT etc calculated by direct formula