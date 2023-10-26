import pygame
from sys import exist
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock= pygame.time.clock()
test_surface= pygame.image.load("c:\Users\user\OneDrive\Desktop\ACT101\jpg\bpc 1.jpg")
while True:
    for event in pygame.even.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(200,100))
    pygame.display.update()
    clock.tick(60)
