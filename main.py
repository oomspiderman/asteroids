# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((50, 20, 40))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()