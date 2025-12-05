def cscan(req, head, direc=1, min=0, max=199): #no end var as we always hit ends anyways in cscan
    reqs = sorted(req)

    left = [r for r in reqs if r < head]
    right = [r for r in reqs if r >= head]

    seek_order= []

    if direc == 1:
        seek_order.extend(right)
        seek_order.append(max)
        seek_order.append(min)
        seek_order.extend(left)
    elif direc == -1:
        seek_order.extend(left[::-1])
        seek_order.append(min)
        seek_order.append(max)
        seek_order.extend(right[::-1])
    else:
        raise ValueError("DIRECTION MUST BE 1 OR -1")
    
    total_seek = 0
    curr = head
    for track in seek_order:
        total_seek += abs(track-curr)
        curr = track

    return seek_order, total_seek
    
if __name__ == "__main__":
    req=[95,180,34,118,11,123,62,64]
    head=50
    print("Direction right")
    order, total = cscan(req, head, direc=1, min=0, max=199)
    print("C-SCAN (counting wrap):")
    print("Order:", order)
    print("Total Seek:", total)
    print()

    print("Direction left")
    order, total = cscan(req, head, direc=-1, min=0, max=199)
    print("C-SCAN (counting wrap):")
    print("Order:", order)
    print("Total Seek:", total)
    print()