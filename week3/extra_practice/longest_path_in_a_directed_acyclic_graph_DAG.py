# extra practice problem 5

# Longest Path in a Directed Acyclic Graph (DAG)

# Write a function to compute the longest path in a weighted DAG.
# Input: Weighted adjacency list and the number of vertices.
# Hint: Perform a topological sort first, then compute the longest path.

# Graph: A --> B --> C --> F
#        |     |
#        D --> E
graph_longest_path = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': [],
    'F': []
}

from collections import deque

def find_longest_path(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    print(in_degree)

    queue = deque([node for node in graph if in_degree[node] == 0])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    dist = {node: float('-inf') for node in graph}
    dist[topological_order[0]] = 0

    for node in topological_order:
        for neighbor in graph[node]:
            dist[neighbor] = max(dist[neighbor], dist[node] + 1)

    longest_path = max(dist.values())
    return longest_path

result = find_longest_path(graph_longest_path)
print(result)
