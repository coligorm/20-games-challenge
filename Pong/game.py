import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            self.screen.fill((34, 43, 68))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            
            pygame.display.update()
            self.clock.tick(30)
        

Game().run()