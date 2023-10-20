import pygame

pygame.init()

# Create a screen.
screen = pygame.display.set_mode((400, 300))

# Draw a rectangle on the screen.
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

# Update the screen.
pygame.display.flip()

# Wait for the user to press the Enter key.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()
   