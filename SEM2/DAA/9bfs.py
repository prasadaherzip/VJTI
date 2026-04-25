from collections import deque

class Graph:
    def __init__(self, vertices, directed=False):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def bfs(self, start, visited):
        queue = deque()
        queue.append(start)
        visited[start] = True

        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

    def bfs_full(self, start):
        visited = [False] * self.V
        all_components = []
        total_nodes = 0

        # BFS from starting node
        if not visited[start]:
            comp = self.bfs(start, visited)
            all_components.append(comp)
            total_nodes += len(comp)

        # Handle disconnected components
        for i in range(self.V):
            if not visited[i]:
                comp = self.bfs(i, visited)
                all_components.append(comp)
                total_nodes += len(comp)

        return all_components, total_nodes


# -------- USER INPUT --------
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

type_graph = input("Is the graph directed? (y/n): ")
directed = True if type_graph.lower() == 'y' else False

g = Graph(n, directed)

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting node for BFS: "))

# -------- BFS --------
components, total = g.bfs_full(start)

# -------- OUTPUT --------
print("\nBFS Traversal:")

for idx, comp in enumerate(components):
    print(f"Component {idx + 1}: {comp}")

print("Total nodes visited:", total)