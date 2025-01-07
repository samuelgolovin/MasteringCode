import pygame
import heapq

pygame.font.init()
font = pygame.font.Font(None, 25)


class City:
    def __init__(self, name, position, neighbors, selected=False):
        self.name = name
        self.position = position
        self.neighbors = neighbors
        self.selected = selected
        self.in_path = False

        self.text = font.render(self.name, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.position))
class Edge:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.selected = False

class Cities:
    def __init__(self):
        self.edges = set()
        self.cities = []
        self.graph = {
            'A': {'pos': (100, 100), 'neighbors': [(60, 'B'), (80, 'C')]},
            'B': {'pos': (160, 100), 'neighbors': [(60, 'A'), (100, 'C')]},
            'C': {'pos': (100, 180), 'neighbors': [(80, 'A'), (100, 'B')]},
        }

        self.selected_city = 'A'

        for node in self.graph:
            if node == self.selected_city:
                self.cities.append(City(node, self.graph[node]['pos'], self.graph[node]['neighbors'], selected=True))
            else:
                self.cities.append(City(node, self.graph[node]['pos'], self.graph[node]['neighbors']))


        self.update_edges()

        self.cycler = self.alphabet_cycler()


    def add_city(self, position, neighbors, selected=False):
        name = next(self.cycler)
        city = City(name, position, neighbors, selected)
        self.graph[name] = {'pos': position, 'neighbors': neighbors}
        print(city.name, city.neighbors)
        self.cities.append(city)

    def get_neighbors(self, mouse_pos):
        # queue = [(name, distance)]
        queue = []
        for node in self.graph:
            heapq.heappush(queue, (pygame.Vector2(self.graph[node]['pos']).distance_to(mouse_pos), node))

        result = []
        result.append(heapq.heappop(queue))
        result.append(heapq.heappop(queue))

        return result

    def set_selected_city(self, city_name):
        for city in self.cities:
            if city.name == city_name:
                city.selected = True
            else:
                city.selected = False
        

    def alphabet_cycler(self):
        alphabet = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
        while True:
            for letter in alphabet:
                yield letter

    def get_traversal_list(self):
        dfs_order = []
        dfs('A', set(), dfs_order, self.graph)




    def update_edges(self):
        visited = set()
        self.edges.clear()
        
        for node in self.graph:
            for neighbor in self.graph[node]['neighbors']:
                edge = (node, neighbor[1])
                if edge not in visited:
                    self.edges.add(Edge(self.graph[node]['pos'], self.graph[neighbor[1]]['pos']))
                    visited.add(edge)
                    visited.add((neighbor[1], node))  # Add the reverse edge to avoid duplicates




class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        current = self.head
        if self.head:
            while True:
                nodes.append(current.data)
                current = current.next
                if current == self.head:
                    break
        print(" -> ".join(map(str, nodes)))






def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for weight, neighbor in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances






def dfs(node, visited, array, graph):
    if node in visited:
        return
    array.append(node)
    visited.add(node)

    for neighbor in graph[node]['neighbors']:
        dfs(neighbor[1], visited, array, graph)
        


