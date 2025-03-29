import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))
        print('Setup End')

        print('Loop Start')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    running = False
                    pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()




