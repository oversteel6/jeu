import pygame
import numpy as np

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
# Taille de la grille
GRID_SIZE = 10

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la Vie avec Fractale")

# Fonction pour initialiser la grille de cellules

def init_grid():
    return np.random.choice([0, 1], size=(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE))

# Fonction pour mettre à jour la grille selon les règles du Jeu de la Vie
def update_grid(grid):

    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbors_sum = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j]
            if grid[i, j] == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors_sum == 3:
                new_grid[i, j] = 1
    return new_grid

# Fonction pour afficher la grille et la fractale
def draw(grid):
    screen.fill(WHITE)

    # Dessiner la fractale (ici, un simple rectangle blanc)
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, WIDTH, HEIGHT))

    # Dessiner les cellules vivantes
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, BLACK, pygame.Rect(j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

# Fonction principale
def main():
    clock = pygame.time.Clock()
    grid = init_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        draw(grid)

        clock.tick(10)  # Ajust vitesse du jeu

    pygame.quit()

if __name__ == "__main__":
    main()
