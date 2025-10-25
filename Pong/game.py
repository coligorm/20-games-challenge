import sys
import pygame

from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        
        # Toggle movement for up or down
        self.movement1 = [False, False]
        self.movement2 = [False, False]
        
        player1_pos = (self.screen.get_width() * 0.05, self.screen.get_height() // 2)
        player2_pos = (self.screen.get_width() * 0.95, self.screen.get_height() // 2)
        
        # Create paddle
        paddle1 = pygame.Rect(player1_pos[0], player1_pos[1], 4, self.screen.get_height() // 8)
        paddle2 = pygame.Rect(player2_pos[0], player2_pos[1], 4, self.screen.get_height() // 8)
        pygame.draw.rect(self.screen, (255, 255, 255), paddle1)
        pygame.draw.rect(self.screen, (255, 255, 255), paddle2)
        
        self.player1 = PhysicsEntity(self, 'player1', player1_pos, (4, self.screen.get_height() // 8), paddle1)
        self.player2 = PhysicsEntity(self, 'player2', player2_pos, (4, self.screen.get_height() // 8), paddle2)
        
    def run(self):
        while True:
            self.screen.fill((34, 43, 68))
            
            divider = pygame.Rect((self.screen.get_width() // 2) - 2, 0, 4, self.screen.get_height())
            pygame.draw.rect(self.screen, (255, 255, 255), divider)
            
            self.player1.update((0, self.movement1[1] - self.movement1[0]))
            self.player1.render(self.screen)
            self.player2.update((0, self.movement2[1] - self.movement2[0]))
            self.player2.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                    # Player 1
                    if event.key == pygame.K_w:
                        self.movement1[0] = True
                    if event.key == pygame.K_s:
                        self.movement1[1] = True
                    # Player 2
                    if event.key == pygame.K_UP:
                        self.movement2[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement2[1] = True
                        
                if event.type == pygame.KEYUP:
                    # Player 1
                    if event.key == pygame.K_w:
                        self.movement1[0] = False
                    if event.key == pygame.K_s:
                        self.movement1[1] = False
                    # Player 2
                    if event.key == pygame.K_UP:
                        self.movement2[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement2[1] = False
            
            pygame.display.update()
            self.clock.tick(30)
        

Game().run()