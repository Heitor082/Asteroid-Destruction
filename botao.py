import pygame

class Botao():
    def __init__(self, x, y, frame, index, largura, altura, valor_do_botao):
        self.x = x
        self.y = y
        self.frame = frame
        self.index = index
        self.largura = largura
        self.altura = altura
        self.valor_do_botao = valor_do_botao
        self.valor = 0

    def desenhar(self, tela):
        self.botao_frame = self.frame[int(self.index)]
        self.botao_frame_ampliado = pygame.transform.scale(self.botao_frame, (self.largura, self.altura))
        tela.blit(self.botao_frame_ampliado, (self.x, self.y))
        
    def verificar_clique(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse = pygame.mouse.get_pos()
            rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
            if rect.collidepoint(self.mouse):
                self.index += 0.50
                if self.index > 4:
                    self.index = 4
                    self.valor = self.valor_do_botao
                    
        if event.type == pygame.MOUSEBUTTONUP:
            self.index = 0
            