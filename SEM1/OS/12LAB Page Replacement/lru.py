pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
frames = []
size = 4
faults = 0
print("Pages -> Frames")

for p in pages:
    if p not in frames:
        if len(frames) == size:
            frames.pop(0)
        frames.append(p)
        faults += 1
    else:
        frames.remove(p)
        frames.append(p)
    print(p,"->",frames)
print("Total fault",faults)
print("Fault Ratio = ", faults/len(pages))
print("Hit Ratio = ", (len(pages)-faults)/len(pages))