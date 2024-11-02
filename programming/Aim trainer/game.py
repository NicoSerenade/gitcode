import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_RADIUS = 30
TARGET_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
FPS = 60
TARGETS_TO_HIT = 10

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Clock
clock = pygame.time.Clock()

# Function to generate random position for the target
def generate_target():
    x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
    return (x, y)

# Function to check if a target is hit
def is_hit(target_pos, mouse_pos):
    distance = ((target_pos[0] - mouse_pos[0]) ** 2 + (target_pos[1] - mouse_pos[1]) ** 2) ** 0.5
    return distance <= TARGET_RADIUS

# Main game function
def main():
    running = True
    hits = 0
    misses = 0
    total_time = 0
    target_pos = generate_target()
    start_time = time.time()

    while running:
        screen.fill(BG_COLOR)
        
        # Draw the target
        pygame.draw.circle(screen, TARGET_COLOR, target_pos, TARGET_RADIUS)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_hit(target_pos, mouse_pos):
                    hits += 1
                    total_time += time.time() - start_time
                    if hits >= TARGETS_TO_HIT:
                        running = False
                    target_pos = generate_target()  # New target
                    start_time = time.time()
                else:
                    misses += 1
        
        # Update screen
        pygame.display.flip()
        
        # Control FPS
        clock.tick(FPS)

    # Show final stats
    if hits > 0:
        avg_time = total_time / hits
    else:
        avg_time = 0
    
    print(f"Game Over! Hits: {hits}, Misses: {misses}, Average Reaction Time: {avg_time:.2f} seconds")

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
