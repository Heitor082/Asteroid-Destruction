import pygame

class Jogador():
    def __init__(self, x, y, largura, altura, velocidade, index, frame):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.atirando = False

    def desenhar(self, tela):
        self.jogador_atirando_frame = self.frame[int(self.index)]
        self.jogador_atirando_frame_ampliado = pygame.transform.scale(self.jogador_atirando_frame, (self.largura, self.altura))
        tela.blit(self.jogador_atirando_frame_ampliado, (self.x, self.y))