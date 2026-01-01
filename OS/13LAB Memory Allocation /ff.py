bloc=[400,200,100,500,300]
pros=[212,417,112,426]

free = bloc[:]
alloc = [-1]*len(pros)

for i in range(len(pros)):      #check process size 
    for j in range(len(bloc)):      #inside the block array
        if free[j] >= pros[i]:
            alloc[i] = j+1
            free[j]=0
            break

print(alloc)