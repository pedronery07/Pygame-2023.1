import pygame

pygame.init()

#cores
background_color = (0,0,0)
cores = {
    'C': (0, 255, 255),  # Ciano
    'AZ': (0, 0, 255),  # Azul
    'L': (255, 165, 0),  # Laranja
    'AM': (255, 255, 0),  # Amarelo
    'VD': (0, 255, 0),  # Verde
    'R': (128, 0, 128),  # Roxo
    'VM': (255, 0, 0),  # Vermelho
    'B' : (255,255,255), # Branco
    'CI': (128, 128, 128) # Cinza
}


#FORMATOS DOS BLOCOS
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....',],
      ['.....',
       '..0..',
       '..00.',
       '...0.',
       '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....',],
      ['.....',
       '..0..',
       '.00..',
       '.0...',
       '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
       '0000.',
       '.....',
       '.....',
       '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..00.',
       '..0..',
       '..0..',
       '.....'],
       ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
         '..0..',
         '..0..',
         '.00..',
         '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..0..',
       '..0..',
       '..00.',
       '.....'],
       ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
         '.00..',
         '..0..',
         '..0..',
         '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..0..',
       '..00.',
       '..0..',
       '.....'],
       ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
         '..0..',
         '.00..',
         '..0..',
         '.....']]

formas = [S, Z, I, O, J, L, T]
cores_formas = [cores['VD'], cores['VM'], cores['C'], cores['AM'], cores['L'], cores['AZ'], cores['R']]


class Peça:
    def inicio (self,x,y,forma):
        self.x = x
        self.y = y 
        self.forma = forma
        self.cores = cores_formas[formas.index(forma)] #Acha a posição da forma escolhida na lista de formas e passa para a lista com as cores das formas
        self.rotação = 0 #Posição inicial da forma, que consegue ser rotacionada posteriormente

FPS = 15

#Tamanhos
WIDTH = 1200
HEIGHT = 750
s_width = 800
s_height = 600
play_width = 300 #300 // 10 => 30 width por bloco
play_height = 600 #500 // 20 => 30 height por bloco
tam_bloco = 30

topo_esquerdo_x = (s_width - play_width) // 2
topo_esquerdo_y = s_height - play_height

#Fonte para título
title_font = pygame.font.Font('freesansbold.ttf', 50)

#Fonte para texto normal
txt_font = pygame.font.Font('freesansbold.ttf', 25)