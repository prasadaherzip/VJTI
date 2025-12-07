def wf(bloc,pros):
    free = bloc[:]
    alloc = [-1]*len(pros)

    for i in range(len(pros)):
        lrgst_idx = None
        lrgst_size = -1

        for j in range(len(free)):
            if free[j] >= pros[i] and free[j] > lrgst_size:
                lrgst_size = free[j]
                lrgst_idx = j

        if lrgst_idx is not None:
            alloc[i] = lrgst_idx + 1
            free[lrgst_idx] = 0

    return alloc

if __name__=="__main__":
    bloc=[400,200,100,500,300]
    pros=[212,417,112,426]
    print(wf(bloc,pros))