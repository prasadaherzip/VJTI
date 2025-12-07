def ff(bloc,pros):
    free=bloc[:]              #copy block
    alloc = [-1] * len(pros)    #initialize alloc list to [-1,-1,-1] lenght of process block

    for i in range(len(pros)):      #length of processes list
        for j in range(len(free)):  #length of free block list
            if free[j]>=pros[i]:
                alloc[i]=j+1        #in the alloc index change val to +1 of the free block index
                free[j]=0           #mark free block index to 0
                break
    return alloc

if __name__=="__main__":
    bloc=[400,200,100,500,300]
    pros=[212,417,112,426]
    print(ff(bloc,pros))

