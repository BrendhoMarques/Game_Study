import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.spriteload = pygame.image.load('./asset/player1.png')

        # Verificando as dimensões da sprite sheet
          # Altura total da sprite sheet (126)
        self.speed = 5  # Pode ajustar a velocidade do player conforme necessário

    def update(self):
        pass

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        pass
# sprite = pg.game
