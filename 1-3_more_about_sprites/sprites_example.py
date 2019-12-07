# Pygame.template - skeleton for a new project

#!/bin/bash

import pygame
import random
import os # biblioteca para mexer com os caminhos do sistema operacional 

WIDTH = 800
HEIGHT = 600
FPS = 30

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# set up assets folders 
# OBS: assets é um termo de desenvolvimento de jogo para arte e sons que vai no seu jogo. 
# OBS2: __file__ é uma nomenclatura em python de sabe o caminho (path) do sistema até o arquivo definido na variável game_folder. Por exemplo:
    # Windows: "C:\Users\chris\Documents"
    # Linux: "/User/chris/Documents"
# garantindo que independente do sistema operacional, o python pegará o caminho do sistema de forma correta.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img") # junta o caminho definido em game_folder, com a pasta img


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert() # carrega a imagem para o pygame (lembrando que imagens tbm é superficie).
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() # pega a área retângular da superficie (a partir daqui, se tronou um retângulo, tendo acesso a todos os métodos do módulo rect do pygame)
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # o centro do retângulo ficará no centro da tela
        self.y_speed = 5


    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed # incrementa a velocidade ao eixo y
        if self.rect.bottom > HEIGHT - 200: # se a parte inferior do retângulo da imagem for maior que a altura da tela (HEIGHT) menos 200:
        	self.y_speed = -5
        if self.rect.top < 200: # se a parte superior do retângulo da imagem (top do retângulo) for menor que 200: 
        	self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# inicializa o pygame e cria a janela    
pygame.init() 
pygame.mixer.init() # inicializa os métodos para audio
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # cria a largura e altura da janela do jogo
pygame.display.set_caption("My Game") # define o nome na aba da janela
clock = pygame.time.Clock() # armazena a classe Clock (relogio) a variáve clock

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


# game loop 
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # checagem caso feche a janela 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    #update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen) # desenha todas as sprites do grupo
    # *after* drawing everything, flip de display
    pygame.display.flip()