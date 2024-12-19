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

# Checking all of the nodes (for personal reference)
for node in graph_dfs:
    print("Node: ", node)
    for neighbor in graph_dfs[node]:
        print("Neighbor: ", neighbor)

print()
print()
print("DFS Example: ")

def dfs(node, graph):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs(neighbor, graph)

visited = set()

dfs('A', graph_dfs)
