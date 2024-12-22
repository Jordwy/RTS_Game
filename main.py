import pygame
import sys
from core.config import ScreenSetting
from core.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((ScreenSetting.WIDTH, ScreenSetting.HEIGHT))
    pygame.display.set_caption("My RTS Game")

    clock = pygame.time.Clock()
    game = Game(screen)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        game.draw()

        pygame.display.flip()
        clock.tick(ScreenSetting.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
