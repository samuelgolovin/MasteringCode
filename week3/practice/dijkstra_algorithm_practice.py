import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Example usage
weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}
print(dijkstra(weighted_graph, 'B')) # Output: {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 7}
