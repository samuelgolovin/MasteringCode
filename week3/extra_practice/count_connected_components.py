# extra practice problem 2

# Count Connected Components

# Given an undirected graph, count the number of connected
# components using DFS.
# Input: Adjacency list.
# Expected result: 2 connected components.

# Graph: (A -- B -- C)  (D -- E)
graph_connected_components = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D']
}

def count_connected_components(graph):
    visited = set()
    connected_components_count = 0

    def dfs(node, graph):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, graph)

    for node in graph:
        if node in visited:
            continue
        else:
            dfs(node, graph)
            connected_components_count += 1

    return connected_components_count

print(graph_connected_components)
print(count_connected_components(graph_connected_components))

graph_disconnected = {
    'A': [],
    'B': [],
    'C': [],
}
# Expected: 3 connected components (each node is isolated)
print(graph_disconnected)
print(count_connected_components(graph_disconnected))

graph_single_component = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
# Expected: 1 connected component
print(graph_single_component)
print(count_connected_components(graph_single_component))

graph_empty = {}
# Expected: 0 connected components
print(graph_empty)
print(count_connected_components(graph_empty))


