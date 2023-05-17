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
    'B' : (255,255,255) #Branco
}

FPS = 15

#Tamanhos
WIDTH = 700
HEIGHT = 800
SIZE = 20

#Fonte para título
title_font = pygame.font.Font('freesansbold.ttf', 50)

#Fonte para texto normal
txt_font = pygame.font.Font('freesansbold.ttf', 25)