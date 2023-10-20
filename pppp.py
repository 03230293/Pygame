# Import pygame and random modules
import pygame
import random

# Initialize pygame
pygame.init()

# Define the screen size and color
screen = pygame.display.set_mode([550, 200])
screen.fill((0, 0, 0))

# Define the dice size and color
dice_size = 50
dice_color = (255, 255, 255)

# Define a function to draw a dice on the screen
def draw_dice(x, y, face):
    # Draw a square for the dice body
    pygame.draw.rect(screen, dice_color, (x, y, dice_size, dice_size))
    # Draw circles for the dice dots
    if face == 1:
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size // 2, y + dice_size // 2), 5)
    elif face == 2:
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size // 4, y + dice_size // 4), 5)
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size * 3 // 4, y + dice_size * 3 // 4), 5)
    elif face == 3:
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size // 4, y + dice_size // 4), 5)
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size // 2, y + dice_size // 2), 5)
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size * 3 // 4, y + dice_size * 3 // 4), 5)
    elif face == 4:
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size // 4, y + dice_size // 4), 5)
        pygame.draw.circle(screen, (0, 0, 0), (x + dice_size * 3 // 4, y + dice_size * 3 // 4), 5)

# //