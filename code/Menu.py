import pygame
from pygame import Surface
from pygame import Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.const import COLOR_BLUE, COLOR_WHITE

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/7392521.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        pygame.mixer_music.load('./asset/Fx 3.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Night', COLOR_BLUE, ((WIN_WIDTH/2), 70))
            self.menu_text(50, 'Divine ', COLOR_BLUE, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
