import pygame
from sys import exit
from random import randint
from random import choice
import time
import os
import math

#Dicionario para músicas


# estou iniciando o modulo (nescessário para o modulo começar a funcionar!)
pygame.init()
# Iniciando a fonte (importante para escrever na tela!)
pygame.font.init()

# função responsável por criar a tela, ele abre uma janela externa do programa
class Tela:
    def __init__(self):
        '''Aqui estão sendo definidos as características da janela. Como largura e altura.'''
        self.largura, self.altura = (800, 400)
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        self.fonte = pygame.sysfont.SysFont('arial', 25, False, False)   
        self.fonte_destaque = pygame.sysfont.SysFont('arial', 32, True, False)   
        self.fps = 8
        # define a cor de fundo, na escala RGB, imagino que já conheça, mas se não: você determina a cor em (vermelho, verde, azul)
        # os valores que podem ser passados são de 1 a 255. Exemplo (12, 125, 30)
        self.cor_fundo = (randint(1, 230), randint(1, 230), randint(1, 230))

# classe responsável  por definir elementos que aparecerão na tela.
class Elementos:
    def __init__(self, tipo, cor, coordenadas, mensagem=None):        
        self.tipo = tipo
        self.cor = cor
        self.coordenadas = coordenadas
        self.mensagem = mensagem

# A função cria a tela inicial do programa. Para isso Chama a classe Jogo, responsável por executar o looping principal.
class TelaInicial:
    def __init__(self, jogo):
        self.jogo = jogo
        self.tela = jogo.tela
        # Os "elementos" são 
        elementos = [
            Elementos('texto', (255, 255, 255), (self.tela.largura/2.30, self.tela.altura/2.30), 'Jogar'),
        ]
        # cria efetivamente o looping. 
        self.looping(elementos)
    # Consiste no looping chamado na linha acima. 
    def looping(self, elementos=[]):
        seletor = 0
        while True:
            # analisa todos os eventos que ocorrem na janela, como teclas pressionadas e se o botão de fechar a janela foi pressionado.
            for event in pygame.event.get():
                # caso o bt fechar a janela for pressionado, fechará a janela.
                if event.type == pygame.WINDOWCLOSE:
                    # Encerra o código rapidamente
                    pygame.quit()
                    exit()
                # detecta as teclas pressionadas e executa funções específicas para cada tecla.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if seletor == 0:
                            seletor = len(elementos) - 1
                        else:
                            seletor -= 1
                    elif event.key == pygame.K_DOWN:
                        if seletor == len(elementos) - 1:
                            seletor = 0
                        else:
                            seletor += 1
                    elif event.key == pygame.K_SPACE:
                        self.jogo.loopingJogo()

            # util para posicionar os itens na lista elementos na tela.
            # Enumerate retorna a posição do elemento e o próprio elemento.
            for n, elemento in enumerate(elementos):
                if elemento.tipo == 'texto':
                    if seletor == n:
                        self.tela.janela.blit(self.tela.fonte_destaque.render(elemento.mensagem, True, elemento.cor), elemento.coordenadas)
                    else:
                        self.tela.janela.blit(self.tela.fonte.render(elemento.mensagem, True, elemento.cor), elemento.coordenadas)                                     
            
            # Atualiza a tela.
            pygame.display.flip()
            # preenche a tela com uma cor específica, nesse caso, cor_fundo
            self.tela.janela.fill(self.tela.cor_fundo)
            # Determina a quantidade de fps da tela.
            pygame.time.Clock().tick(20)


class Jogo:
    #Função de aúdio tocar junto com o game----------------------------------------- Musica()
    def Musica(self):
        # Define o caminho para a pasta de músicas
        diretorio_musicas = 'Atividades/Feira_De_Profissões/Musics'
        # Lista todos os arquivos no diretório
        arquivos_musica = os.listdir(diretorio_musicas)
        # Filtra apenas os arquivos de música
        musicas = [arquivo for arquivo in arquivos_musica if arquivo.endswith(('.mp3', '.wav'))]
        if musicas:  # Verifica se existem músicas na lista
            # Escolhe uma música aleatória
            musica_escolhida = choice(musicas)
            # Carrega e toca a música escolhida
            pygame.mixer.music.load(os.path.join(diretorio_musicas, musica_escolhida))
            pygame.mixer.music.play(-1)  # O -1 faz a música tocar em loop
        else:
            print("Nenhuma música encontrada na pasta.")

    def __init__(self):
        self.tempo = 0
        self.tela = Tela()        
        self.respostas = []
        self.acertos = []
        self.pontuacao = 0
        self.Musica()
        TelaInicial(self)

    def loopingJogo(self):
        # determina as perguntas que serão feitas ao usuário
        self.perguntas = '1)quem é presidente dos Estados Unidos?', '2)Quem auxiliou para a criação de uma maquina para desvendar a ENIGMA?', '3)Quanto é a metade de dois mais dois?'
        # determina as alternativas a serem mostradas 
        self.alternativas = [['A)Adolf Hitler', 'B)Joseph Stalin', 'C)Joe Biden', 'D)Margareth Hamilton'], ['A)Alan Turing', 'B)Robert Boyle', 'C)Albert Einstein', 'D)Nicola Tesla'], ['A)3', 'B)Mickey Mouse/adolf Hitler', 'C)2', 'D)11° setembro']]
        # Define as respostas corretas
        self.respostas = ['C', 'A', 'D']
        
        # Cria um looping que percorre a lista de perguntas.
        for n, pergunta in enumerate(self.perguntas):
            alternativas = self.alternativas[n]
            resposta = self.respostas[n]
            # elemento que indica onde o usuário está selecionando.
            seletor = 0
            # variavel que define se a tela está aberta ou fechada.
            janela_aberta = True
            # utilizado para marcar um tempo e salva-lo.
            contador1 = time.perf_counter()
            # Looping principal, responsável por mostrar as perguntas e receber as respostas. 
            while janela_aberta:
                for event in pygame.event.get():
                    if event.type == pygame.WINDOWCLOSE:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if seletor == 0:
                                seletor = len(alternativas) - 1
                            else:
                                seletor -= 1
                        elif event.key == pygame.K_DOWN:
                            if seletor == len(alternativas) - 1:
                                seletor = 0
                            else:
                                seletor += 1
                        elif event.key == pygame.K_SPACE:
                            for n1, opcao in enumerate(alternativas):
                                if n1 == seletor:
                                    if opcao[0] == resposta:
                                        self.acertos.append(1) 
                                        self.pontuacao += 1
                                    elif opcao[0] == resposta:
                                        self.acertos.append(0)
                                        
                                self.respostas.append(opcao[0])
                                janela_aberta = False
                                        
                cor_texto = (255, 255, 255)
                self.tela.janela.blit(self.tela.fonte.render(pergunta, True, cor_texto), (0,0))
                # elementos
                x = 0
                y = 50
                
                for n2, alternativa in enumerate(alternativas):
                    if seletor == n2:
                        self.tela.janela.blit(self.tela.fonte_destaque.render(alternativa, True, cor_texto), (x,y))
                    else:
                        self.tela.janela.blit(self.tela.fonte.render(alternativa, True, cor_texto), (x, y))
                    y += 50
                                                    
                pygame.display.flip()
                self.tela.janela.fill(self.tela.cor_fundo)
                pygame.time.Clock().tick(20)
            contador2 = time.perf_counter() - contador1
            self.tempo += contador2

            print(f'demorou {contador2} para solucionar questão sua pontuação foi {math.trunc(contador2)} ', n) #=========================
        self.telaFinal()

    def telaFinal(self):
        #Percorrendo a lista de tempo definida em "self.tempo"


        # elementos que aparecerão na tela.
        elementos = [
            Elementos('texto', (255, 255, 255), (0, 0), f'pontuação {(self.pontuacao/self.tempo)*100:.0f}'),
            Elementos('texto', (255, 255, 255), (0, 50), f'insira seu nome ou apelido:'),
            Elementos('texto', (255, 255, 255), (300, 50), ''),
            Elementos('texto', (255, 255, 255), (350, 50), f'Vai se ferrar {self.tempo:.2f}')
        ]
        seletor = 0
        letras = []
        janela = True
        while janela:
            for event in pygame.event.get():
                if event.type == pygame.WINDOWCLOSE:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if seletor == 0:
                            seletor = len(elementos) - 1
                        else:
                            seletor -= 1
                    elif event.key == pygame.K_DOWN:
                        if seletor == len(elementos) - 1:
                            seletor = 0
                        else:
                            seletor += 1
                    elif event.key == pygame.K_SPACE:
                        self.salvar(elementos[2].mensagem, self.pontuacao)
                        Jogo()
                        
                    match event.key:
                        case pygame.K_a:
                            letras.append('a')
                        case pygame.K_b:
                            letras.append('b')
                        case pygame.K_c:
                            letras.append('c')
                        case pygame.K_d:
                            letras.append('d')
                        case pygame.K_e:
                            letras.append('e')
                        case pygame.K_f:
                            letras.append('f')
                        case pygame.K_g:
                            letras.append('g')
                        case pygame.K_h:
                            letras.append('h')
                        case pygame.K_i:
                            letras.append('i')
                        case pygame.K_j:
                            letras.append('j')
                        case pygame.K_k:
                            letras.append('k')
                        case pygame.K_l:
                            letras.append('l')
                        case pygame.K_m:
                            letras.append('m')
                        case pygame.K_n:
                            letras.append('n')
                        case pygame.K_o:
                            letras.append('o')
                        case pygame.K_p:
                            letras.append('p')
                        case pygame.K_q:
                            letras.append('q')
                        case pygame.K_r:
                            letras.append('r')
                        case pygame.K_s:
                            letras.append('s')
                        case pygame.K_t:
                            letras.append('t')
                        case pygame.K_u:
                            letras.append('u')
                        case pygame.K_v:
                            letras.append('v')
                        case pygame.K_w:
                            letras.append('w')
                        case pygame.K_x:
                            letras.append('x')
                        case pygame.K_y:
                            letras.append('y')
                        case pygame.K_z:
                            letras.append('z')
                        case pygame.K_BACKSPACE:
                            try:
                                letras.pop(len(letras) -1)
                            except:
                                pass
                    texto = ''
                    for letra in letras:
                        texto += letra

                    elementos[2].mensagem = texto    
                    

            # elementos que aparecerão na tela.
            for n, elemento in enumerate(elementos):
                if elemento.tipo == 'texto':
                    # posiciona um elemento selecionado na tela. Ele fica em destaque.
                    if seletor == n:
                        self.tela.janela.blit(self.tela.fonte_destaque.render(elemento.mensagem, True, elemento.cor), elemento.coordenadas)
                    # posiciona um elemento não selecionado. Ele não fica em destaque
                    else:
                        self.tela.janela.blit(self.tela.fonte.render(elemento.mensagem, True, elemento.cor), elemento.coordenadas)                                     
            # atualiza a tela
            pygame.display.flip()
            # preenche a tela cor a cor de fundo
            self.tela.janela.fill(self.tela.cor_fundo)
            # limita o fps da tela.
            pygame.time.Clock().tick(20)
        
    # salva de uma maneira simples o conteúdo.
    def salvar(self, nome_usuario, pontuacao):
        with open('placar_lideres.txt', 'a') as file:
            file.write(nome_usuario + ' ' + str(pontuacao) + '\n')

Jogo()

# Kelvyn é um lindo! E é o melhor vice lider em RPG - Segundo o Murilo Santos

