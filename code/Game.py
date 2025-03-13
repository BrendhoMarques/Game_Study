import pygame
from code.Menu import Menu, MENU_OPTION
from code.Level import Level
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        # print('Setup Start')
        # print('Setup Finish')
        #
        # print('Loop Start')
        global Level
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                Level = Level(self.window, 'Level 1', menu_return)
                level_return = Level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass



