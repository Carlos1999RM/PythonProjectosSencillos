import pygame
import heapq

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Pac-Man configuraciones
pacman_size = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Fantasmas configuraciones
ghost_size = 20
ghost_speed = 2
ghost_positions = [[50, 50], [500, 50], [50, 300]]  # Fantasmas en posiciones iniciales

# Puntos (comida) configuraciones
food_size = 10
food_positions = []

# Laberinto (paredes)
block_size = 40
maze = [
    "11111111111111111111",
    "10000000001100000001",
    "10111101111101111101",
    "10100000000000000101",
    "10101111111111110101",
    "10100000000000000101",
    "11111111111111111111",
]

# Convertir el laberinto en posiciones de bloques
walls = []
for row_idx, row in enumerate(maze):
    for col_idx, cell in enumerate(row):
        if cell == "1":
            walls.append(pygame.Rect(col_idx * block_size, row_idx * block_size, block_size, block_size))
        elif cell == "0":
            food_positions.append([col_idx * block_size + block_size // 3, row_idx * block_size + block_size // 3])

# Convertir el laberinto en una matriz para A*
def create_grid(maze):
    grid = []
    for row in maze:
        grid.append([1 if cell == '0' else 0 for cell in row])
    return grid

grid = create_grid(maze)

# Reloj
clock = pygame.time.Clock()

# Heurística de A* (distancia de Manhattan)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Algoritmo A* para encontrar el camino más corto
def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 1:
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

    # Reconstruir el camino
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.reverse()
    return path

# Función para mover fantasmas usando A*
def move_ghost(grid, ghost_pos, pacman_pos):
    start = (ghost_pos[1] // block_size, ghost_pos[0] // block_size)
    goal = (pacman_pos[1] // block_size, pacman_pos[0] // block_size)
    path = a_star_search(grid, start, goal)
    
    if path and len(path) > 1:
        next_step = path[1]
        return [next_step[1] * block_size, next_step[0] * block_size]
    
    return ghost_pos

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control de teclas
    keys = pygame.key.get_pressed()
    pacman_new_x, pacman_new_y = pacman_x, pacman_y
    if keys[pygame.K_LEFT]:
        pacman_new_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_new_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_new_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_new_y += pacman_speed

    # Comprobar colisiones con paredes antes de mover a Pac-Man
    pacman_rect = pygame.Rect(pacman_new_x, pacman_new_y, pacman_size, pacman_size)
    if pacman_rect.collidelist(walls) == -1:
        pacman_x, pacman_y = pacman_new_x, pacman_new_y

    # Comprobar si Pac-Man ha comido la comida
    for food in food_positions[:]:
        if (pacman_x < food[0] + food_size and
                pacman_x + pacman_size > food[0] and
                pacman_y < food[1] + food_size and
                pacman_y + pacman_size > food[1]):
            food_positions.remove(food)

    # Mover fantasmas hacia Pac-Man usando A*
    for idx, ghost_pos in enumerate(ghost_positions):
        ghost_positions[idx] = move_ghost(grid, ghost_pos, (pacman_x, pacman_y))

    # Comprobar colisiones con fantasmas
    for ghost_pos in ghost_positions:
        ghost_rect = pygame.Rect(ghost_pos[0], ghost_pos[1], ghost_size, ghost_size)
        if pacman_rect.colliderect(ghost_rect):
            print("¡Te atraparon los fantasmas! Game Over.")
            running = False

    # Comprobar si Pac-Man ha ganado
    if len(food_positions) == 0:
        print("¡Ganaste! Has comido toda la comida.")
        running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Dibujar laberinto (paredes)
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Dibujar Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x + pacman_size // 2, pacman_y + pacman_size // 2), pacman_size // 2)

    # Dibujar comida
    for food in food_positions:
        pygame.draw.rect(screen, WHITE, (food[0], food[1], food_size, food_size))

    # Dibujar fantasmas
    for ghost_pos in ghost_positions:
        pygame.draw.rect(screen, RED, (ghost_pos[0], ghost_pos[1], ghost_size, ghost_size))

    # Actualizar pantalla
    pygame.display.flip()

    # Control de FPS
    clock.tick(30)

# Salir de Pygame
pygame.quit()
