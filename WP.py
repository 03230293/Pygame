import pygame, random

# Define the game constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a list of words for the puzzle
words = ["APPLE", "BANANA", "CAT", "DOG", "ELEPHANT"]

# Create a 10x10 grid to store the puzzle letters
grid = [["-" for i in range(10)] for j in range(10)]

# Randomly place the words in the grid
def generate_puzzle():
    for word in words:
        # Choose a random starting position for the word
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        # Check if the word can be placed at the starting position
        if can_place_word(word, row, col):
            # Place the word in the grid
            for letter in word:
                grid[row][col] = letter
                col += 1

# Check if a word can be placed at a given position in the grid
def can_place_word(word, row, col):
    # Check if the word goes out of bounds
    if row + len(word) > 10:
        return False

    # Check if the word collides with any other words in the grid
    for i in range(len(word)):
        if grid[row][col + i] != "-":
            return False

    return True

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Generate the puzzle
generate_puzzle()

# Start the game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game logic

    # Draw the puzzle grid
    for i in range(10):
        for j in range(10):
            if grid[i][j] != "-":
                pygame.draw.rect(screen, BLUE, (i * 32, j * 32, 32, 32))

    # Render the screen
    pygame.display.flip()

    # Limit the framerate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()