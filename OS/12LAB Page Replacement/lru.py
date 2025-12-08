def lru(pages, frames_count):
    frames = [-1] * frames_count     # empty frames
    recent = {}                      # stores last used time of each page
    hits = 0
    misses = 0
    time = 0                         # simple counter to mark recency

    for p in pages:
        time = time + 1              # increase time on each reference

        # HIT
        if p in frames:
            hits = hits + 1
            recent[p] = time         # update last used time

        else:   # MISS
            misses = misses + 1

            # empty frame exists
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = p
                recent[p] = time

            else:
                # find LRU page (smallest recent time)
                lru_page = None
                lru_time = None

                for f in frames:
                    if lru_time is None or recent[f] < lru_time:
                        lru_time = recent[f]
                        lru_page = f

                # replace LRU page
                replace_idx = frames.index(lru_page)
                frames[replace_idx] = p
                recent[p] = time

        print("Page:", p, "Frames:", frames)

    hit_ratio = float(hits) / (hits + misses)

    print("\nTotal Hits   =", hits)
    print("Total Misses =", misses)
    print("Hit Ratio    =", hit_ratio)

    return hits, misses, hit_ratio


# Example usage
PAGES = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
FRAMES = 4

lru(PAGES, FRAMES)