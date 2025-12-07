def bf(bloc,pros):
    free = bloc[:]
    alloc = [-1]*len(pros)

    for i in range(len(pros)):
        req = pros[i]
        best_size= None
        best_idx= None
        for j in range(len(free)):
            if free[j]>=req[i]:
                if best_size is None or free[j]<pros[i]:
                    best_size = free[j]
                    best_idx = j
    if best_size is not None:
        alloc[i]= best_idx + 1
        free[best_idx] -= req

if __name__=="__main__":
    bloc=[400,200,100,500,300]
    pros=[212,417,112,426]
    print(bf(bloc,pros))