import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group     = pygame.sprite.Group()
    drawable_group      = pygame.sprite.Group()
    asteroids_group     = pygame.sprite.Group()
 
    Player.containers        = (updatable_group,drawable_group)
    Asteroid.containers      = (asteroids_group,drawable_group, updatable_group)
    AsteroidField.containers = (updatable_group)

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    af = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        screen.fill("black")

        for player in drawable_group:
            player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
