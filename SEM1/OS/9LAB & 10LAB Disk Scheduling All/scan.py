
req = [95,180,34,119,11,123,62,64]
head = 50
min=0
max=199
direction=0

reqs=[]
reqs = sorted(req)

print("Request order is :", req)
print("Sorted requests are: ", reqs)
print("Read currently at: ", head)
direction= int(input("Enter direction of service (1=right, -1=left): \n"))

seek_order = []

left = [r for r in reqs if r < head]
right = [r for r in reqs if r >= head]

if direction == 1:
    seek_order.extend(right)
    seek_order.append(max)
    seek_order.extend(left[::-1])

elif direction == -1:
    seek_order.extend(left[::-1])
    seek_order.append(min)
    seek_order.extend(right)

else:
    print("invalid direction")

total = 0
curr = head

for i in range(len(seek_order)):
    total += abs(seek_order[i]-curr)
    curr = seek_order[i]

if direction == 1:
    print("SCAN seek order when right servicing", seek_order)
    print("Total Head Movement", total)
elif direction == -1:
    print("SCAN seek order when left servicing", seek_order)
    print("Total Head Movement:", total)



