# extra practice problem 7

# Hamiltonian Cycle Detection

# Check if a Hamiltonian cycle exists in a given graph (visits every vertex exactly once and returns to the starting vertex).
# Input: Adjacency list of an undirected graph.
# Hint: Use backtracking with visited nodes.

# Graph: A -- B -- C
#        |         |
#        D ---------
graph_hamiltonian_cycle = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

def detect_hamiltonian_cycle(graph):
    def dfs(node, start, path):
        if len(path) == len(graph):
            if start in graph[node]:
                path.append(start)
                return True
            return False
        for neighbor in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                if dfs(neighbor, start, path):
                    return True
                path.pop()
        return False

    for start_node in graph:
        if dfs(start_node, start_node, [start_node]):
            return True
    return False

# Test the improved function
result = detect_hamiltonian_cycle(graph_hamiltonian_cycle)
if result:
    print("Hamiltonian cycle exists.")
else:
    print("Hamiltonian cycle does not exist.")

graph_example_fail = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': ['C']
}
result = detect_hamiltonian_cycle(graph_example_fail)
if result:
    print("Hamiltonian cycle exists.")
else:
    print("Hamiltonian cycle does not exist.")
