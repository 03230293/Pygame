import Pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
def roll_die():
    return random.randint(1, 6)
while True:
    # Get the rolled number.
    rolled_number = roll_die()

    # Display the die image.
    screen.blit(die_image, (100, 100))

    # Display the rolled number.
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(str(rolled_number), True, (0, 0, 0))
    screen.blit(text, (200, 200))

    # Update the display.
    pygame.display.flip()

    # Check if the user wants to quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
