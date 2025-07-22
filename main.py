import pygame

from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    pygame.init()

    dt = 0
    pygame.time.Clock().get_fps()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt =pygame.time.Clock().tick(60) / 1000

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
