import pygame
import random

# Define some constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 80

# Create a Pygame window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a class to represent a block
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.surface.fill(color)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

# Create a list of blocks
blocks = []
for i in range(4):
    for j in range(4):
        block = Block(i * BLOCK_SIZE, j * BLOCK_SIZE, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        blocks.append(block)

# Start the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the blocks
    for block in blocks:
        block.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
