def dfs(node, graph, visited):
    visited.add(node)              # mark visited first
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)


# Input
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, n + 1)}   # 1-based indexing

graph_type = input("Directed graph? (yes/no): ").lower()

print("Enter edges:")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    if graph_type == "no":
        graph[v].append(u)

start = int(input("Enter starting node: "))

visited = set()
count = 0

print("\nDFS Traversal:")

# Start from given node
if start not in visited:
    print("Component:", end=" ")
    before = len(visited)
    dfs(start, graph, visited)
    count += len(visited) - before
    print()

# Handle disconnected components
for node in graph:
    if node not in visited:
        print("Component:", end=" ")
        before = len(visited)
        dfs(node, graph, visited)
        count += len(visited) - before
        print()

print("\nTotal nodes visited:", count)
