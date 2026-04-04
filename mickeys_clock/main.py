import pygame
import sys
from clock import MickeyClock

def main():
    pygame.init()
    screen = pygame.display.set_caption("Mickey's Clock")
    screen = pygame.display.set_mode((800, 800))
    clock_logic = MickeyClock()
    fps_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # White background
        clock_logic.update()
        clock_logic.draw(screen)
        
        pygame.display.flip()
        fps_clock.tick(60)

if __name__ == "__main__":
    main()