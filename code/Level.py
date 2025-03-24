import random
import sys

import pygame
from pygame import Surface
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        # Adicionando o fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # Criando o jogador e adicionando à lista de entidades
        player = EntityFactory.get_entity('Player1', (100, 100))  # Defina uma posição inicial para o jogador
        if player:
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:

            # Loop de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            # Limpa a tela
            self.window.fill((0, 0, 0))

            # Atualiza o movimento das entidades
            for ent in self.entity_list:
                ent.move()

            # Desenha as entidades
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

            # Exibe informações no canto superior esquerdo
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 100 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            # Atualiza a tela
            pygame.display.flip()
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Comic Sans MS', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
