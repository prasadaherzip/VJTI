bloc = [400,200,100,500,300]     # memory blocks
pros = [212,417,112,426]         # process sizes

free = bloc[:]                  # copy of blocks
alloc = [-1] * len(pros)        # allocation result

print("Blocks   :", bloc)
print("Processes:", pros)
print("------------------------")

for i in range(len(pros)):
    best_size = None
    best_idx = None

    for j in range(len(bloc)):
        if free[j] >= pros[i]:
            if best_size is None or free[j] < best_size:
                best_size = free[j]
                best_idx = j

    if best_idx is not None:
        alloc[i]=best_idx+1
        free[best_idx]=0

print(bloc)
print(pros)
print(alloc)