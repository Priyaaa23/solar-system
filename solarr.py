import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants for the simulation
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
SUN_COLOR = (255, 255, 0)
PLANET_COLORS = [
    (0, 0, 255), (255, 0, 0), (0, 255, 0),
    (128, 128, 128), (255, 165, 0), (139, 69, 19),
    (255, 192, 203), (173, 255, 47)
]  # Different colors for each planet
PLANET_RADII = [30, 15, 20, 25, 10, 18, 22, 28]  # Radii of planets
PLANET_DISTANCES = [150, 200, 250, 300, 350, 400, 450, 500]  # Distances from the Sun
PLANET_SPEEDS = [0.005, 0.003, 0.002, 0.0015, 0.004, 0.0025, 0.0037, 0.001]  # Orbital speeds

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Main simulation loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # Draw the Sun
    pygame.draw.circle(screen, SUN_COLOR, (WIDTH // 2, HEIGHT // 2), 50)

    # Simulate and draw planets
    for i in range(len(PLANET_COLORS)):
        angle = pygame.time.get_ticks() * PLANET_SPEEDS[i]
        x = int(WIDTH // 2 + math.cos(angle) * PLANET_DISTANCES[i])
        y = int(HEIGHT // 2 + math.sin(angle) * PLANET_DISTANCES[i])
        pygame.draw.circle(screen, PLANET_COLORS[i], (x, y), PLANET_RADII[i])

    pygame.display.flip()
    clock.tick(60)
