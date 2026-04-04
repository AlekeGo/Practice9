import pygame
import sys
from player import MusicPlayer

pygame.init()

# окно
WIDTH, HEIGHT = 500, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# создаём плеер
player = MusicPlayer()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                player.play()
            elif event.key == pygame.K_s:  # Stop
                player.stop()
            elif event.key == pygame.K_n:  # Next
                player.next_track()
            elif event.key == pygame.K_b:  # Back
                player.prev_track()
            elif event.key == pygame.K_q:  # Quit
                pygame.quit()
                sys.exit()

    # фон
    screen.fill((230, 230, 230))

    # текущий трек
    track_text = font.render(f"Track: {player.get_current_track_name()}", True, (0, 0, 0))
    screen.blit(track_text, (20, 80))

    pygame.display.flip()
    clock.tick(30)