bloc=[400,200,100,500,300]
pros=[212,417,112,426]

free = bloc[:]
alloc = [-1]*len(pros)

for i in range(len(pros)):
    lrgst_idx= None
    lrgst_size= -1

    for j in range(len(bloc)):
        if free[j] >= pros[i] and free[j] > lrgst_size:
            lrgst_size = free[j]
            lrgst_idx = j
    
    if lrgst_idx is not None:
        alloc[i]=lrgst_idx+1
        free[lrgst_idx] = 0

print(pros)
print(bloc)
print(alloc)