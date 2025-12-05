def fcfs(requests, head):
    order = []
    total = 0
    curr = head

    for req in requests:
        order.append(req)
        total += abs(req - curr)
        curr = req

    return order, total


def sstf(requests, head):
    arr = requests.copy()
    order = []
    total = 0
    curr = head

    while arr:
        nearest = min(arr, key=lambda x: abs(x - curr))
        order.append(nearest)
        total += abs(nearest - curr)
        curr = nearest
        arr.remove(nearest)

    return order, total


def scan(requests, head, disk_size):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    order = []

    # Move right side
    for r in right:
        order.append(r)

    # Go to last cylinder
    order.append(disk_size - 1)

    # Then move left
    for l in left:
        order.append(l)

    total = 0
    curr = head
    for req in order:
        total += abs(req - curr)
        curr = req

    return order, total


# ---------------- MAIN PROGRAM ----------------
requests = []
n = int(input("Enter number of disk requests: "))
print("Enter the requests:")
for _ in range(n):
    requests.append(int(input()))

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter total disk size (max cylinder number): "))

print("\n================== RESULTS ==================\n")

fcfs_order, fcfs_move = fcfs(requests, head)
print("FCFS Order:", fcfs_order)
print("FCFS Total Head Movement:", fcfs_move)

sstf_order, sstf_move = sstf(requests, head)
print("\nSSTF Order:", sstf_order)
print("SSTF Total Head Movement:", sstf_move)

scan_order, scan_move = scan(requests, head, disk_size)
print("\nSCAN Order:", scan_order)
print("SCAN Total Head Movement:", scan_move) 
