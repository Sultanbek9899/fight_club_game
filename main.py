import pygame


class Game():
    def __init__(self):
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500


    def run_game(self):
        pygame.init()
        size = [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]
        screen  = pygame.display.set_mode(size)
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    active = False

if __name__ == "__main__":
    game = Game()
    game.run_game()


