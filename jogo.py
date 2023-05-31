# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from os import path
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, IMG_DIR
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chuva do Milhão')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        pygame.init()
        window = pygame.display.set_mode((600, 700))
        pygame.display.set_caption('GAME OVER! :(')
        # ----- Inicia estruturas de dados
        game = True
        # ----- Inicia assets
        font = pygame.font.SysFont(None, 48)
        background2 = pygame.image.load(path.join(IMG_DIR, 'game_over.png')).convert()
        text2 = font.render("Pressione qualquer tecla", True, (255, 0, 0))
        text3 = font.render("para sair", True, (255, 0, 0))
        # ===== Loop principal =====
        while game:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = False
                # ----- Gera saída
            window.fill((255, 255, 255))  # Preenche com a cor branca
            # Carrega imagem da tela final
            window.blit(background2,(180, 100))
            window.blit(text2, (100, 350))
            window.blit(text3, (220, 400))
            
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador
            
            if event.type == pygame.KEYUP:
                pygame.quit()

pygame.quit() 
state = QUIT
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
