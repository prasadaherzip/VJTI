def bellman_ford(n, edges, source):
    # Initialize distances and parents
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[source] = 0

    # Relax edges (n-1) times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("\nGraph contains a NEGATIVE WEIGHT CYCLE!")
            return None, None

    return dist, parent


def get_path(parent, node):
    path = []
    while node != -1:
        path.append(node)
        node = parent[node]
    return path[::-1]


# -------- INPUT --------
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

directed = int(input("Is the graph directed? (1 = Yes, 0 = No): "))

edges = []

print("Enter edges (u v weight):")
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    if directed == 0:
        edges.append((v, u, w))


source = int(input("Enter source node: "))


# -------- RUN --------
dist, parent = bellman_ford(n, edges, source)


# -------- OUTPUT --------
if dist is not None:
    print("\nNode   Distance   Path")
    for i in range(n):
        if dist[i] == float('inf'):
            print(f"{source} -> {i}   INF   No path")
        else:
            path = get_path(parent, i)
            print(f"{source} -> {i}   {dist[i]}   {' '.join(map(str, path))}")