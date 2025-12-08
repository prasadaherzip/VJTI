def fifo(pages, frames_count):
    frames = [-1] * frames_count   # -1 means empty frame
    queue = []                     # stores the order of inserted pages (FIFO)
    hits = 0
    misses = 0

    for p in pages:

        # if page already in frame → HIT
        if p in frames:
            hits = hits + 1

        else:   # MISS
            misses = misses + 1

            # if an empty frame exists
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = p
                queue.append(p)
            else:
                # remove the oldest page based on FIFO rule
                old = queue.pop(0)
                old_idx = frames.index(old)
                frames[old_idx] = p
                queue.append(p)

        print("Page:", p, "Frames:", frames)

    hit_ratio = float(hits) / (hits + misses)

    print("\nTotal Hits   =", hits)
    print("Total Misses =", misses)
    print("Hit Ratio    =", hit_ratio)

    return hits, misses, hit_ratio


# Example usage
PAGES = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
FRAMES = 4

fifo(PAGES, FRAMES)