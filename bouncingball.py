import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("bouncing_ball.gif")
b_rect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    b_rect = b_rect .move(speed)
    if b_rect.left < 0 or b_rect.right > width:
        speed[0] = -speed[0]
    if b_rect.top < 0 or b_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, b_rect)
    pygame.display.flip()