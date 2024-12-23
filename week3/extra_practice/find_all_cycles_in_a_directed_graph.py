# extra practice problem 6

# Find All Cycles in a Directed Graph

# Given a directed graph, find all the cycles.
# Input: Adjacency list.
# Hint: Use backtracking to explore cycles.

# Graph: A --> B --> C --> A
#               D --> E --> D
graph_find_all_cycles = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}

def find_all_cycles(graph):
    def dfs(node, start, path):
        if node in path:
            if node == start:
                cycles.append(path[path.index(node):])
            return

        path.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, start, path)
        path.pop()

    cycles = []
    for node in graph:
        dfs(node, node, [])
    return cycles


result = find_all_cycles(graph_find_all_cycles)
print("Cycles found: ")
for cycle in result:
    print(" -> ".join(cycle))

graph_example_fail = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A'],  # Forms a cycle A -> C -> A
    'D': ['B']   # Forms a cycle D -> B -> D
}

result = find_all_cycles(graph_example_fail)
print("Cycles found: ")
for cycle in result:
    print(" -> ".join(cycle))
