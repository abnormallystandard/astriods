import sys
import pygame
from constants import *
from player import *
from astroids import *
from astroidfield import *
from circleshape import *
from shot import *
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Astroids.containers = (updatable, drawable, astroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for up in updatable:
            up.update(dt)
        for asteroid in astroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()
        # Framerate 60
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()