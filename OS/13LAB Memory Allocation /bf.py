def bf(bloc, pros):
    free = bloc[:]                  # copy of blocks
    alloc = [-1] * len(pros)        # result: block number or -1

    for i in range(len(pros)):
        best_idx = None
        best_size = None

        # find smallest block that can fit req
        for j in range(len(free)):
            if free[j] >= pros[i]:
                if best_size is None or free[j] < best_size:
                    best_size = free[j]
                    best_idx = j

        # allocate (one-use: mark block as unusable)
        if best_idx is not None:
            alloc[i] = best_idx + 1   # 1-based block number
            free[best_idx] = 0        # block used up completely

    return alloc

if __name__=="__main__":
    bloc=[400,200,100,500,300]
    pros=[212,417,112,426]
    print(bf(bloc,pros))