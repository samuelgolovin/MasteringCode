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


start = 'A'
end = 'C'
shortest_distance, path = cities.dijkstra(start, end)
print(f"Shortest distance: {shortest_distance}")
print(f"Path: {' -> '.join(path)}")

start = 'A'
end = 'B'
shortest_distance, path = cities.dijkstra(start, end)
print(f"Shortest distance: {shortest_distance}")
print(f"Path: {' -> '.join(path)}")



selected_city_start, selected_city_end = cities.update_traversal('A', 'A')

shortest_distance, path = cities.dijkstra(selected_city_start.data, selected_city_end.data)
print(f"Shortest distance: {shortest_distance}")
print(f"Path: {' -> '.join(path)}")


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            cities.add_city(pygame.mouse.get_pos())
            selected_city_start, selected_city_end = cities.update_traversal(selected_city_start.data, selected_city_end.data)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                if event.key == pygame.K_LEFT:
                    selected_city_start = selected_city_start.prev
                    cities.set_selected_start(selected_city_start.data)
                if event.key == pygame.K_RIGHT:
                    selected_city_start = selected_city_start.next
                    cities.set_selected_start(selected_city_start.data)
                if event.key == pygame.K_a:
                    selected_city_end = selected_city_end.prev
                    cities.set_selected_end(selected_city_end.data)
                if event.key == pygame.K_d:
                    selected_city_end = selected_city_end.next
                    cities.set_selected_end(selected_city_end.data)

                shortest_distance, path = cities.dijkstra(selected_city_start.data, selected_city_end.data)

                for city in cities.cities:
                    city.in_path = False
                for node in path:
                    for city in cities.cities:
                        if node == city.name:
                            city.in_path = True

                for edge in cities.edges:
                    edge.selected = False
                for edge in cities.edges:
                    if edge.start.in_path and edge.end.in_path:
                        edge.selected = True


    

    # Fill the screen with a color (RGB)
    screen.fill((220, 220, 220))

    for edge in cities.edges:
        if edge.selected:
            pygame.draw.line(screen, 'purple', edge.start_pos, edge.end_pos, 5)
        else:
            pygame.draw.line(screen, 'black', edge.start_pos, edge.end_pos, 3)

    for city in cities.cities:
        if city.selected_start and city.selected_end:
            pygame.draw.circle(screen, 'blue', city.position, 20)
        elif city.selected_start:
            pygame.draw.circle(screen, 'green', city.position, 18)
        elif city.selected_end:
            pygame.draw.circle(screen, 'red', city.position, 18)
        else:
            if city.in_path:
                pygame.draw.circle(screen, 'purple', city.position, 10)
            else:
                pygame.draw.circle(screen, 'black', city.position, 14)
        screen.blit(city.text, city.text_rect)
    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
