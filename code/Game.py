import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        # print('Setup Start')
        # print('Setup Finish')
        #
        # print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         print('Quitting...')
            #         pygame.quit()
            #         quit()

