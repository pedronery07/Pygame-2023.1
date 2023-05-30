# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
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
        window = pygame.display.set_mode((500, 400))
        pygame.display.set_caption('GAME OVER! :(')
        # ----- Inicia estruturas de dados
        game = True
        # ----- Inicia assets
        font = pygame.font.SysFont(None, 48)
        text = font.render('GAME', True, (250, 0, 0))
        text2 = font.render('OVER', True, (250, 0, 0))
        text3 = font.render("Pressione qualquer tecla", True, (250, 250, 250))
        text4 = font.render("para sair", True, (250, 250, 250))
        # ===== Loop principal =====
        while game:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = False
                # ----- Gera saída
            window.fill((0, 0, 0))  # Preenche com a cor preta
            window.blit(text, (190, 115))
            window.blit(text2, (195,165))
            window.blit(text3, (50, 280))
            window.blit(text4, (180, 320))
            
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador
            
            if event.type == pygame.KEYUP:
                pygame.quit()

pygame.quit() 
state = QUIT
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
