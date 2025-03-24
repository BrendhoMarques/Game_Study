# Cores
import pygame

COLOR_BLUE = (14, 0, 205)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

#Velocidade Fundo

EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED ={
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 7,
    'Enemy1': 1,
    'Enemy2': 3,
}

#Tempo de spawn
SPAWN_TIME = 4000

# Opções do menu
MENU_OPTION = ('NEW GAME', 'NEW GAME PLUS', 'SETTINGS', 'SCORE', 'EXIT')

#Player teclas
PLAYER_KEY_UP =  {'Player1':pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1':pygame.K_DOWN}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_RCTRL}

# Largura e altura da tela
WIN_WIDTH = 1280
WIN_HEIGHT = 720
