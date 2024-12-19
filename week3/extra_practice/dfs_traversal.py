# extra practice problem 1

#Depth-First Search (DFS) Traversal

#Write a function to perform a DFS traversal of a graph and print the nodes
#in the order they are visited.
#Input: Adjacency list representation of a graph.

# Graph: A -- B
#         |    |
#         D -- C
graph_dfs = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if not provided
    if node in visited:
        return
    visited.add(node)
    print(node)  # Visit the current node
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)

print("DFS Traversal:")
dfs('A', graph_dfs)
