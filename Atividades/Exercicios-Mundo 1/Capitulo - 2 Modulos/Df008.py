import pygame
pygame.init()

pygame.mixer.music.load('D:\Gustavo\Visual Studio CODE\ProjetoCursoEmvideo\Python\Atividades\Exercicios-Mundo 1\Capitulo - 2 Modulos\Midia\musica.mp3')
pygame.mixer.music.play()

input()
pygame.event.wait()
