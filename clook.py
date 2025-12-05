def clook( req, head, direc=1, min=0, max=199):
    reqs = sorted(req)

    left = [r for r in reqs if r < head]
    right =[r for r in reqs if r >= head]

    seek_order = []

    if direc == 1:
        seek_order.extend(right)
        seek_order.extend(left)   

    elif direc == -1:
        seek_order.extend(left[::-1])
        seek_order.extend(right[::-1])
    
    else:
        raise ValueError("DIRECTION MUST BE 1 OR -1")
    
    #compute seek distance
    total_seek = 0
    curr = head
    for track in seek_order:
        total_seek += abs(track-curr)
        curr = track

    return seek_order, total_seek

if __name__ == "__main__":
    req = [95,180,34,119,11,123,62,64]
    head = 50
    
    order, total =  clook(req, head, direc = 1, min=0, max=199)
    print("C-LOOK (to right, and go to right request end)")
    print("Order:", order)
    print("Total Seek:", total)
    print()

    order, total =  clook(req, head, direc = -1, min=0, max=199)
    print("C-LOOK (to left, and go to left request end)")
    print("Order:", order)
    print("Total Seek:", total)
    print()