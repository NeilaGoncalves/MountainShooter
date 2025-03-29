import pygame

class Game:
    def __init__(self):
        self.window = None  # Inicializa a janela como None

    def run(self):  # Remove a vírgula desnecessária
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # Usa self.window
        print('Setup End')

        print('Loop Start')
        running = True
        while running:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    running = False  # Sai do loop
                    pygame.quit()  # Fecha o Pygame

# Criando e executando o jogo
if __name__ == "__main__":
    game = Game()
    game.run()


