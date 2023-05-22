import pygame
import time
import random
from config import WIDTH, HEIGHT, cores, background_color, title_font, txt_font, formas,topo_esquerdo_x,topo_esquerdo_y,play_height,play_width,tam_bloco, Peça, s_height, s_width 
from assets import theme_song

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

#Funções para colocar texto na tela
def text_objects(text,color,size):
    if size == "small":
        textSurface = txt_font.render(text,True,color)
    elif size == "medium":
        textSurface = txt_font.render(text,True,color)
    elif size == "large":
        textSurface = txt_font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message(msg,color,gameDisplay,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#Função da tela inicial
clock = pygame.time.Clock()
def game_intro():
    
    intro = True

    pygame.mixer.music.play(-1)

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    quit()

        gameDisplay.fill(background_color)
        message("Bem-vindo ao Tetris !!!", cores['VD'], gameDisplay, -100,  "large")
        
        message("O objetivo do jogo é obter máxima pontuação por meio do posicionamento de blocos na tela", cores['R'], gameDisplay, -30)
        
        message("Cada linha completada será liberada, sendo possível liberar mais de uma linha ao mesmo tempo.", cores['AZ'], gameDisplay ,10)
        
        message("Se não for mais possível inserir blocos na tela, a rodada e contagem de pontos irá acabar.", cores['AM'], gameDisplay,  50)
        
        message("Pressione ENTER para iniciar ou ESPAÇO para sair", cores['VM'], gameDisplay,80)

        pygame.display.update()
        clock.tick(5)

#Funções que criam o grid do jogo
def cria_grid(posicao_fixa = {}):
    grid = []
    for a in range(20):
        linha = []
        for b in range(10):
            bloco = (0,0,0)
            linha.append(bloco)
        grid.append(linha)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in posicao_fixa:
                c = posicao_fixa[(j, i)]
                grid[i][j] = c
    
    return grid

def seleciona_forma():
    escolha = Peça(5,0,random.choice(formas))
    return escolha

def desenha_grid(superficie, grid):
    x0 = topo_esquerdo_x
    y0 = topo_esquerdo_y

    for i in range(len(grid)):
        #20 colunas
        pygame.draw.line(superficie, cores['CI'], (x0, y0+i*tam_bloco), (x0 + play_width, y0+i*tam_bloco))
        for j in range(len(grid[i])):
            #10 linhas
            pygame.draw.line(superficie, cores['CI'], (x0 + j*tam_bloco, y0), (x0 + j*tam_bloco, y0+ play_width, play_height))

def desenha_janela(superficie,grid):
    superficie.fill(background_color)
    
    pygame.font.init()
    
    titulo = title_font.render('Tetris',1,(255,255,255))

    superficie.blit(titulo,(topo_esquerdo_x + play_width/2 - titulo.get_width()/2,30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(superficie, grid[i][j], (topo_esquerdo_x + j*tam_bloco, topo_esquerdo_y + i*tam_bloco, tam_bloco, tam_bloco), 0)

    pygame.draw.rect(superficie, (255,0,0), (topo_esquerdo_x, topo_esquerdo_y, play_width, play_height), 4)

    desenha_grid(superficie,grid)

    pygame.display.update()              

def converte_forma(forma):
    posicoes = []
    formato = forma.forma[forma.rotation % len(forma.forma)]

    for i, line in enumerate(formato):
        linha = list(line)
        for j, column in enumerate(linha):
            if column == '0':
                posicoes.append((forma.x + j, forma.y + i))

    for i, pos in enumerate(posicoes):
        posicoes[i] = (pos[0] - 2, pos[1] - 4)

def valida_posicao(forma, grid):
    pos_validas = []
    for i in range(20):
        for j in range(10):
            # Uma peça não pode ocupar o espaço de outra
            # Para a posição ser válida, a cor da posição deve ser igual à cor do background(preta)
            if grid[i][j] == background_color:
                pos_validas.append((j, i))
    
    # Converte as posições válidas de listas com sublistas em listas sem sublistas
    # Exemplo: [[(0, 1)], [(2, 3)], [(4, 5)]] -> [(0, 1), (2, 3), (4, 5)] 
    pos_validas_sem_sublistas = []
    for sublist in pos_validas:
        for item in sublist:
            pos_validas_sem_sublistas.append(item)
    pos_validas = pos_validas_sem_sublistas

    formatado = converte_forma(forma)

    for pos in formatado:
        if pos not in pos_validas:
            # Formatos nascem fora da tela (posição negativa)
            # É necessário checar quando a peça for visível ao jogador e, então, pos[1] > -1 
            if pos[1] > -1:
                # Retorna Falso quando o jogador tentar ultrapassar os limites laterais da tela
                return False
    
    return True

def valida_altura(pos_validas):
    for p in pos_validas:
        x,y = p
        if y < 1:
            return True
        else:
            return False

def principal():

    posicao_fixa = {}

    grid = cria_grid(posicao_fixa)

    muda_peça = False
    jogo_aberto = True
    peça = seleciona_forma()
    proxima_peça = seleciona_forma()
    relogio = pygame.time.Clock()
    queda = 0 
    velocidade_de_queda = 0.27

    while jogo_aberto:
        grid = cria_grid(posicao_fixa)
        queda += clock.get_rawtime()
        clock.tick()

        if queda/1000 > velocidade_de_queda:
            queda = 0
            peça.y += 1
            if not(valida_posicao(peça,grid)) and peça.y > 0:
                peça.y -= 1
                muda_peça = True

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                jogo_aberto = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    peça.x -= 1
                    if not(valida_posicao(peça,grid)):
                        peça.x += 1
                if e.key == pygame.K_RIGHT:
                    peça.x += 1
                    if not (valida_posicao(peça,grid)):
                        peça.x -= 1
                if e.key == pygame.K_DOWN:
                    peça.y -= 1
                    if not (valida_posicao(peça,grid)):
                        peça.y += 1
                if e.key == pygame.K_UP:
                    peça.rotação += 1
                    if not(valida_posicao(peça,grid)):
                        peça -= 1
        
                
        forma_pos = converte_forma(peça)

        for i in range(len(forma_pos)):
            x, y = forma_pos[i]
            if y > -1:
                grid[y][x] = peça.color
        
        if muda_peça:
            for pos in forma_pos:
                p = (pos[0], pos[1])
                posicao_fixa[p] = peça.color
            peça = proxima_peça
            proxima_peça = seleciona_forma
            muda_peça = False

        desenha_janela(win,grid)

        if valida_altura(posicao_fixa):
            jogo_aberto = False
    
    pygame.display.quit()

def menu_principal(win):
    principal(win)
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
menu_principal(win)