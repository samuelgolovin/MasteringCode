import pygame
import heapq

pygame.font.init()
font = pygame.font.Font(None, 25)


class City:
    def __init__(self, name, position, neighbors, selected_start=False, selected_end=False):
        self.name = name
        self.position = position
        self.neighbors = neighbors
        self.selected_start = selected_start
        self.selected_end = selected_end
        self.in_path = False

        self.text = font.render(self.name, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.position))
class Edge:
    def __init__(self, start_pos, end_pos, start, end):
        self.start = start
        self.end = end
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
                self.cities.append(City(node, self.graph[node]['pos'], self.graph[node]['neighbors'], selected_start=True, selected_end=True))
            else:
                self.cities.append(City(node, self.graph[node]['pos'], self.graph[node]['neighbors']))


        self.update_edges()

        self.cycler = self.alphabet_cycler()

##        self.add_city((300, 300))
##        self.add_city((400, 300))
##        self.add_city((300, 400))
##        self.add_city((300, 300))
##        self.add_city((20, 300))
##        self.add_city((300, 20))


    def add_city(self, position, selected=False):
        if len(self.cities) < len('DEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()=+`~[];,./{}|:"<>?ABC'):
            name = next(self.cycler)
            neighbors = self.get_neighbors(position)
            city = City(name, position, neighbors, selected)
            
            self.cities.append(city)
            self.update_graph(name, position, neighbors)
            self.update_edges()
        else:
            print("Limit reached")

    def update_graph(self, name, position, neighbors):
        self.graph[name] = {'pos': position, 'neighbors': neighbors}

        for distance, neighbor in neighbors:
            if neighbor in self.graph:
                self.graph[neighbor]['neighbors'].append((distance, name))
            else:
                self.graph[neighbor] = {'pos': None, 'neighbors': [(distance, name)]}

    def get_neighbors(self, mouse_pos):
        # queue = [(name, distance)]
        queue = []
        for node in self.graph:
            heapq.heappush(queue, (pygame.Vector2(self.graph[node]['pos']).distance_to(mouse_pos), node))

        result = []
        result.append(heapq.heappop(queue))
        result.append(heapq.heappop(queue))
        return result
        

    def alphabet_cycler(self):
        alphabet = 'DEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()=+`~[];,./{}|:"<>?ABC'
        while True:
            for letter in alphabet:
                yield letter

    def get_traversal_list(self, ):
        dfs_order = []
        dfs('A', set(), dfs_order, self.graph)

    def set_selected_start(self, name):
        for city in self.cities:
            if city.name == name:
                city.selected_start = True
##                print(city.name + " has been selected")
            else:
                city.selected_start = False

    def set_selected_end(self, name):
##        print("input: ", name)
        for city in self.cities:
##            print("city: ", city.name)
            if city.name == name:
                city.selected_end = True
##                print(city.name + " has been selected")
            else:
                city.selected_end = False

    def update_traversal(self, current_start, current_end):
        traverse_start_order = []
        dfs(current_start, set(), traverse_start_order, self.graph)
        tso_cll = CircularLinkedList()

        for node in traverse_start_order:
            tso_cll.append(node)

        selected_city_start = tso_cll.head

        traverse_end_order = []
        dfs(current_end, set(), traverse_end_order, self.graph)
        teo_cll = CircularLinkedList()

        for node in traverse_end_order:
            teo_cll.append(node)

        selected_city_end = teo_cll.head

        return selected_city_start, selected_city_end



    def update_edges(self):
        visited = set()
        self.edges.clear()
        
        for node in self.graph:
            self.graph[node]['neighbors'].sort(key=lambda x: x[0])
            for neighbor in self.graph[node]['neighbors']:
                edge = (node, neighbor[1])
                if edge not in visited:
                    for city in self.cities:
                        if city.name == node:
                            current_city = city
                        if city.name == neighbor[1]:
                            current_neighbor = city
                    self.edges.add(Edge(self.graph[node]['pos'], self.graph[neighbor[1]]['pos'], current_city, current_neighbor))
                    visited.add(edge)
                    visited.add((neighbor[1], node))  # Add the reverse edge to avoid duplicates

    def dijkstra(self, start, end):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        predecessors = {vertex: None for vertex in self.graph}
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for weight, neighbor in self.graph[current_vertex]['neighbors']:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()

        return distances[end], path




class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            new_node.prev = current
            self.head.prev = new_node
            

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
        


