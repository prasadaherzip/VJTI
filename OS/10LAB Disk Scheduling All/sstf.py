def sstf(req, head):
    pending = req[:]        # copy so original is not changed
    order = []
    total = 0
    curr = head

    while pending:
        # find the request closest to curr
        closest = min(pending, key=lambda r: abs(r - curr))

        # service it: add seek, record order, move head, remove from pending
        total += abs(closest - curr)
        order.append(closest)
        curr = closest
        pending.remove(closest)

    return order, total


if __name__ == "__main__":
    req = [95,180,34,119,11,123,62,64]
    head = 50

    order, total = sstf(req, head)
    print("Order:", order)
    print("Total seek:", total)