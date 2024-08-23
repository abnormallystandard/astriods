import pygame
from constants import *
from player import *
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        # Framerate 60
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()