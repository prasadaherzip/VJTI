import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    distances[source] = 0
    pq = [(0, source)]

    while pq:
        dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, parent


def get_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


# -------- INPUT --------
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

directed = int(input("Is the graph directed? (1 = Yes, 0 = No): "))

graph = {i: [] for i in range(n)}

print("Enter edges (u v weight):")
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    if directed == 0:
        graph[v].append((u, w))


source = int(input("Enter source node: "))


# -------- RUN --------
distances, parent = dijkstra(graph, source)


# -------- OUTPUT --------
print("\nNode   Distance   Path")
for node in range(n):
    path = get_path(parent, node)
    print(f"{source} -> {node}   {distances[node]}   {' '.join(map(str, path))}")