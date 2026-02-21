req = [95,180,34,119,11,123,62,64]
head = 50

reqs = req[:]          # copy request list
seek_order = []

print("Request order is :", req)
print("Read currently at : \n", head)

total = 0
curr = head

while reqs:
    closest = reqs[0]

    for track in reqs:
        if abs(track-curr) < abs(closest-curr):
            closest = track             # all of this gives 1st closest request

    seek_order.append(closest)          #append this closest and then remove it
    total += abs(closest-curr)
    curr = closest
    reqs.remove(closest)            #perform the comparison for next closest

print("------------------------")
print("SSTF seek order :", seek_order)
print("Total Head Movement :", total)