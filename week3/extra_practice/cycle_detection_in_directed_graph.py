# extra practice problem 3

# Cycle Detection in Directed Graphs

# Cycle Detection in Directed Graphs

# Write a function to detect whether a directed graph contains a cycle using DFS.
# Input: Adjacency list.
# Key Hint: Use a "visited" array and a "recursion stack."
# Expected result: Cycle exists in the graph.

# Graph: A --> B --> C --> A
#        D --> E
graph_cycle_directed = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['E'],
    'E': []
}

def detect_cycle(graph):
    visited = set()
    stack = set()
    def dfs(node):
        
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        stack.remove(node)

    for i in graph:
        if i not in visited:
            if dfs(i):
                return True

    return False


if detect_cycle(graph_cycle_directed) == True:
    print("Cycle exists in graph")
else:
    print("Cycle does not exist in graph")

graph_no_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['E'],
    'E': []
}
# Expected: "Cycle does not exist in graph"
if detect_cycle(graph_no_cycle) == True:
    print("Cycle exists in graph")
else:
    print("Cycle does not exist in graph")

graph_mixed = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],  # Cycle here
    'D': ['E'],
    'E': []
}
# Expected: "Cycle exists in graph"
if detect_cycle(graph_mixed) == True:
    print("Cycle exists in graph")
else:
    print("Cycle does not exist in graph")
