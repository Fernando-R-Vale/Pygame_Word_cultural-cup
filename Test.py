# importa a biblioteca para poder usar ao longo do código
import pygame
import time
# Função tela campo

def Campo(tela, largura, altura):
    # configurando imagem
    tamanho = (640,400)
    imagem_original = pygame.image.load('Imagens/campo.jpeg').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,0))

    #atualizando tela
    return imagem

def empate(tela, largura, altura):
    # configurando imagem
    tamanho = (640,560)
    imagem_original = pygame.image.load('Imagens/empate.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,0))

    #atualizando tela
    return imagem

def Vitoriadireita(tela, largura, altura):
    # configurando imagem
    tamanho = (640,560)
    imagem_original = pygame.image.load('Imagens/jog 2.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,0))

    #atualizando tela
    return imagem

def Vitoriaesquerda(tela, largura, altura):
    # configurando imagem
    tamanho = (640,560)
    imagem_original = pygame.image.load('Imagens/jog 1.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,0))

    #atualizando tela
    return imagem

def Band_vermelha(tela, largura, altura):
    tamanho = (64,64)
    imagem_original = pygame.image.load('Imagens/bandeira vermelha.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (largura, altura))
    return imagem

def band_azul(tela, largura, altura):
    tamanho = (64,64)
    imagem_original = pygame.image.load('Imagens/bandeira azul.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (largura, altura))
    return imagem

def band_verde(tela, largura, altura):
    tamanho = (64,64)
    imagem_original = pygame.image.load('Imagens/bandeira verde.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (largura, altura))
    return imagem

def band_preta(tela, largura, altura):
    tamanho = (64,64)
    imagem_original = pygame.image.load('Imagens/bandeira preta.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (largura, altura))
    return imagem

def Caixa():
    tamanho = (640,160)
    imagem_original = pygame.image.load('Imagens/caixa.png').convert_alpha()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,400))
    return imagem

def escreve(texto, tela, largura, altura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 20)
    texto = fonte.render(texto, True, (0,0,0))
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (largura, altura)
    tela.blit(texto, texto_retangulo)

# textinho das alternativas

def escreve_alternativas(texto, tela, largura, altura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 16)
    texto = fonte.render(texto, True, (0,0,0))
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (largura, altura)
    tela.blit(texto, texto_retangulo)

def Caixa_de_alternativas():
    pygame.draw.rect(tela, (212, 253, 0), (50, 435, 200, 50))
    pygame.draw.rect(tela, (212, 253, 0), (50,500,200, 50))
    pygame.draw.rect(tela, (212, 253, 0), (375,435,200, 50))
    pygame.draw.rect(tela, (212, 253, 0), (375,500,200, 50))
def questão_1():
    escreve('Quem foi o jogador mais jovem a ganhar uma Copa do Mundo?', tela, 320, 420)
    escreve_alternativas('1- Pelé - 17 anos', tela, 150, 460)
    escreve_alternativas('2- M.Baldivieso - 13 anos', tela, 150, 525)
    escreve_alternativas('3- G.Martinelli - 21 anos', tela, 475, 460)
    escreve_alternativas('4- Ronaldo - 17 anos', tela, 475, 525)
def questão_3():
    escreve("Quantos jogadores tem em um jogo de futebol", tela, 320, 420)
    escreve_alternativas('1- 15', tela, 150, 460)
    escreve_alternativas('2- 18', tela, 150, 525)
    escreve_alternativas('3- 21', tela, 475, 460)
    escreve_alternativas('4- 22', tela, 475, 525)
def questão_2():
    escreve('Qual o jogador com maior valor de mercado?', tela, 320, 420)
    escreve_alternativas('1- Vinicius Junior', tela, 150, 460)
    escreve_alternativas('2- Kylian Mbappé', tela, 150, 525)
    escreve_alternativas('3- Jude Bellingham', tela, 475, 460)
    escreve_alternativas('4- Luis Díaz', tela, 475, 525)
def questão_4():
    escreve('Quem ganhou a copa o mundo de 2010', tela, 320, 420)
    escreve_alternativas('1- Alemanha', tela, 150, 460)
    escreve_alternativas('2- França', tela, 150, 525)
    escreve_alternativas('3- Espanha', tela, 475, 460)
    escreve_alternativas('4- EUA', tela, 475, 525)
def escreveteladeentrade(texto, tela, largura, altura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 26)
    texto = fonte.render(texto, True, (0,0,0))
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (largura // 2, altura)
    tela.blit(texto, texto_retangulo)

def abrir_tela_de_entrada(tela):
    # configurando imagem
    tamanho = (640,560)
    imagem_original = pygame.image.load('Imagens/tela de inicio.png').convert()
    imagem = pygame.transform.scale(imagem_original, tamanho)

    # mostrando imagem
    tela.blit(imagem, (0,0))

    # configurando texto
    escreveteladeentrade('Pressione espaço para iniciar o jogo…', tela, 640, 20)

    #atualizando tela
    pygame.display.flip()
    sair_tela_entrada = False
    while not sair_tela_entrada:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN:
            sair_tela_entrada = event.key == pygame.K_SPACE
    return imagem
# inicializa a biblioteca
def Indicar_Jogador1():
    pygame.draw.rect(tela, (37, 110, 5), (0, 370, 640, 30))
    escreve('Jogador 1',tela, 50, 385)
def Indicar_Jogador2():
    pygame.draw.rect(tela, (37, 110, 5), (0, 370, 640, 30))
    escreve('Jogador 2',tela, 50, 385)


pygame.init()
# define constantes
tela_tamanho = (640, 560)
pausa = 60
relogio = pygame.time.Clock()
# constantes de cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# define tamanho e título da janela gráfica do jogo
tela = pygame.display.set_mode(tela_tamanho)
pygame.display.set_caption('Telejogo by Infoweb')
# # iniciando o loop de jogo
# fim_do_jogo = False
# while not fim_do_jogo:
#     # essa forma é melhor de dar um intervalo no jogo
#     relogio.tick(pausa)

#     # eventos de teclado, mouse, joistique, e outros
#     # são obtidos na função pygame.event.get()
#     for event in pygame.event.get():
#         # foi evento de saída do jogo
#         if event.type == pygame.QUIT:
#             fim_do_jogo = True
sair_do_joguinho = True

Jogador_esquerda = 0
Jogador_direita = 0
while sair_do_joguinho:
    abrir_tela_de_entrada(tela)
    time.sleep(1/2)
    tela.fill((22, 180, 20))
    escreveteladeentrade('Aperte 1, 2, 3 ou 4 para responder as questões',tela, 640, 270)
    escreveteladeentrade('Vence o jogador com a maior', tela, 640, 180)
    escreveteladeentrade('quantidade de respostas corretas', tela, 640, 220)
    escreveteladeentrade('Aperte espaço para continuar', tela, 640, 400)
    pygame.display.flip()
    sair_tela_entrada = False
    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sair_tela_entrada = True
    time.sleep(1/2)


    #



    Campo(tela, 640, 400)
    Caixa()
    band_azul(tela, 37, 80)
    band_preta(tela, 200, 240)
    band_preta(tela, 545, 240)
    band_preta(tela, 200, 80)
    band_preta(tela, 370, 240)
    band_preta(tela, 370, 80)
    band_preta(tela, 485 ,100)
    band_preta(tela, 97, 220)
    Caixa_de_alternativas()
    Indicar_Jogador1()
    questão_1()

    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    band_verde(tela, 37, 80)
                    Jogador_esquerda += 1
                    sair_tela_entrada = True
                elif event.key == pygame.K_2:
                    Band_vermelha(tela, 37, 80)
                    sair_tela_entrada = True
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 37, 80)
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 37, 80)

    pygame.display.flip()

    time.sleep(1/2)

    #prx questão

    band_azul(tela, 545, 240)


    Caixa_de_alternativas()
    Indicar_Jogador2()

    questão_1()

    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    band_verde(tela, 545, 240)
                    sair_tela_entrada = True
                    Jogador_direita += 1
                elif event.key == pygame.K_2:
                    Band_vermelha(tela, 545, 240)
                    sair_tela_entrada = True
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 545, 240)
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 545, 240)

    pygame.display.flip()
    time.sleep(1/2)

    # proxima questão

    Caixa()
    band_azul(tela, 200, 80)

    Caixa_de_alternativas()
    Indicar_Jogador1()
    questão_2()

    pygame.display.flip()

    sair_tela_entrada = False

    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Band_vermelha(tela, 200, 80)
                    sair_tela_entrada = True
                elif event.key == pygame.K_2:
                    band_verde(tela, 200, 80)
                    sair_tela_entrada = True
                    Jogador_esquerda += 1
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 200, 80)
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 200, 80)

    pygame.display.flip()

    time.sleep(1/2)

    #Prox questão

    band_azul(tela, 370, 240)
    Indicar_Jogador2()

    pygame.display.flip()

    sair_tela_entrada = False

    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Band_vermelha(tela, 370, 240)
                    sair_tela_entrada = True
                elif event.key == pygame.K_2:
                    band_verde(tela, 370, 240)
                    sair_tela_entrada = True
                    Jogador_direita += 1
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 370, 240)
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 370, 240)

    pygame.display.flip()
    time.sleep(1/2)
    #Proxima questão

    Caixa()
    band_azul(tela, 370, 80)
    Indicar_Jogador1()
    Caixa_de_alternativas()

    questão_3()

    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 370, 80)
                elif event.key == pygame.K_2:
                    Band_vermelha(tela, 370, 80)
                    sair_tela_entrada = True
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 370, 80)
                elif event.key == pygame.K_4:
                    band_verde(tela, 370, 80)
                    Jogador_esquerda += 1
                    sair_tela_entrada = True

    pygame.display.flip()
    time.sleep(1/2)

    # proxima questão

    band_azul(tela, 200, 240)
    Caixa_de_alternativas()
    Indicar_Jogador2()
    questão_3()

    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 200, 240)
                elif event.key == pygame.K_2:
                    Band_vermelha(tela, 200, 240)
                    sair_tela_entrada = True
                elif event.key == pygame.K_3:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 200, 240)
                elif event.key == pygame.K_4:
                    band_verde(tela, 200, 240)
                    Jogador_esquerda += 1
                    sair_tela_entrada = True

    pygame.display.flip()
    time.sleep(1/2)


    # Quuestão


    band_azul(tela, 485 ,100)
    Caixa()
    Caixa_de_alternativas()
    questão_4()
    Indicar_Jogador1()
    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Band_vermelha(tela, 485 ,100)
                    sair_tela_entrada = True
                elif event.key == pygame.K_2:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 485 ,100)
                elif event.key == pygame.K_3:
                    band_verde(tela, 485 ,100)
                    sair_tela_entrada = True
                    Jogador_esquerda += 1
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 485 ,100)

    pygame.display.flip()
    time.sleep(1/2)


    # Questão

    Indicar_Jogador2()
    band_azul(tela, 97, 220)
    pygame.display.flip()

    sair_tela_entrada = False


    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Band_vermelha(tela, 97, 220)
                    sair_tela_entrada = True
                elif event.key == pygame.K_2:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 97, 220)
                elif event.key == pygame.K_3:
                    band_verde(tela, 97, 220)
                    Jogador_direita += 1
                    sair_tela_entrada = True
                elif event.key == pygame.K_4:
                    sair_tela_entrada = True
                    Band_vermelha(tela, 97, 220)

    pygame.display.flip()
    time.sleep(1/2)
    if Jogador_direita > Jogador_esquerda:
        Vitoriadireita(tela,640,560)
    elif Jogador_direita < Jogador_esquerda:
        Vitoriaesquerda(tela,640,560)
    elif Jogador_esquerda == Jogador_direita:
        empate(tela,640,560)
    escreveteladeentrade("Precione espaço para reiniciar", tela, 640, 20)
    pygame.display.flip()
    sair_tela_entrada = False
    while not sair_tela_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_tela_entrada = True
                sair_do_joguinho = False
                pygame.quit()
                exit()
            # foi evento de saída do jogo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sair_tela_entrada = True
