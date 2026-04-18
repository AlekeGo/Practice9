import pygame
from clock import MickeyClock


pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

hand_image = pygame.image.load("images/mickey_hand.png").convert_alpha()
hand_image = pygame.transform.scale(hand_image, (120, 120))

mickey_clock = MickeyClock(screen, hand_image)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    mickey_clock.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()