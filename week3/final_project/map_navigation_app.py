import pygame
import sys
import heapq

from simple_map_navigation_utils import (Cities, Edge, CircularLinkedList,
dijkstra, dfs, )

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font(None, 25)

cities = Cities()


dijkstra_graph = {}

for city in cities.cities:
    dijkstra_graph[city.name] = city.neighbors
start_vertex = cities.selected_city
shortest_distances = dijkstra(dijkstra_graph, start_vertex)

dfs_order = []
dfs('A', set(), dfs_order, cities.graph)
cll = CircularLinkedList()

for node in dfs_order:
    cll.append(node)

selected_city = cll.head

print(cll.head.data)
##cll.display()
##print(dfs_order)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            neighbors = cities.get_neighbors(mouse_pos)
            cities.add_city(pygame.mouse.get_pos(), neighbors)
            cities.update_edges()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                selected_city = selected_city.next
                cities.set_selected_city(selected_city.data)

    # Fill the screen with a color (RGB)
    screen.fill((220, 220, 220))

    for edge in cities.edges:
        pygame.draw.line(screen, 'black', edge.start_pos, edge.end_pos, 3)

    for city in cities.cities:
        if city.selected:
            pygame.draw.circle(screen, 'green', city.position, 15)
        else:
            pygame.draw.circle(screen, 'red', city.position, 15)
        screen.blit(city.text, city.text_rect)
    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
