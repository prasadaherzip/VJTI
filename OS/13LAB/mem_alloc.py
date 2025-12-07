def ff(bloc,pros):
    free = bloc[:]              #copy block
    alloc = [-1] * len(pros)    #initialize alloc list to [-1,-1,-1] lenght of process block

    for i in range(len(pros)):      #length of processes list
        for j in range(len(free)):  #length of free block list
            if free[j]>=pros[i]:
                alloc[i]=j+1        #in the alloc index change val to +1 of the free block index
                free[j]=0           #mark free block index to 0
                break
    return alloc

def wf(bloc,pros):
    free = bloc[:]
    alloc=[-1]*len(pros)

    for i in range(len(pros)):
        lrgst_idx = None        #index of largest block
        lrgst_size = -1         #size of largest block

        for j in range(len(free)):      #to find the biggest block for the process
            if free[j] >= pros[i] and free[j] > lrgst_size:
                lrgst_size = free[j]
                lrgst_idx = j
        
        if lrgst_idx is not None:
            alloc[i] = lrgst_idx + 1
            free[lrgst_idx] = 0     #marks the block as used
    
    return alloc

def bf(bloc,pros):
    free = bloc[:]
    alloc = [-1]*len(pros)
    
    for i in range(len(pros)):
        req = pros[i]
        best_idx = None
        best_size = None
        for j in range(len(free)):
            if free[j]>=req:
                if best_size is None or free[j] < best_size:
                    best_size = free[j]
                    best_idx = j

        if best_idx is not None:
            alloc[i] = best_idx + 1
            free[best_idx] -= req

    return alloc


if __name__=="__main__":
    bloc=[400,200,100,500,300]
    pros=[212,417,112,426]

    print("Available blocks are [400,200,100,500,300]")
    print ("Processes to be allocated are [212,417,112,426]")
    print("Indexes of occupied blocks by processes in First Fit", ff(bloc,pros))
    print("Indexes of occupied blocks by processes in Worst Fit", wf(bloc,pros))
    print("Indexes of occupied blocks by processes in Best Fit", bf(bloc,pros))

