# extra practice problem 4

# update
# I used BFS to find the shortest path efficiently

# Shortest Cycle in an Undirected Graph

# Given an undirected graph, find the shortest cycle (if any).
# Input: Adjacency list.
# Hint: Use BFS to find the shortest cycle efficiently.

# Expected result: Shortest cycle is A -> D -> C -> A with length 3.

# Graph: A -- B -- C
#        |         |
#        D ---------
graph_shortest_cycle = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

from collections import deque

def find_shortest_cycle(graph):

    def bfs(start):
        visited = {start: 0}
        queue = deque([(start, -1)])

        while queue:
            current_node, parent_node = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[current_node] + 1
                    queue.append((neighbor, current_node))
                elif neighbor != parent_node:
                    return visited[neighbor] + visited[current_node] + 1
        return float('inf')

    shortest_cycle = float('inf')
    for node in graph:
        shortest_cycle = min(shortest_cycle, bfs(node))

    return shortest_cycle




result = find_shortest_cycle(graph_shortest_cycle)
print(result)

graph_no_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': []
}
# Expected output: inf
result = find_shortest_cycle(graph_no_cycle)
print(result)

graph_multiple_cycles = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}
# Expected output: 3 (cycle: A -> B -> C -> A)
result = find_shortest_cycle(graph_multiple_cycles)
print(result)
