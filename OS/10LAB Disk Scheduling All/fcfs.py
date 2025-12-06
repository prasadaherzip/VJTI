def fcfs(req,head):
    order = req

    total = 0
    curr = head

    for track in order:
        total+=abs(track-curr)
        curr=head
    return order,total

if __name__=="__main__":
    req = [95,180,34,119,11,123,62,64]
    head = 50

    order,total= fcfs(req,head)
    print(order,total)

