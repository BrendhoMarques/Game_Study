import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


# -----------------------
# Classe Level
# -----------------------
class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # Evento de sair do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Limpa a tela
            self.window.fill((0, 0, 0))

            # Atualiza e desenha cada fundo
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()
            # clock.tick(60)
