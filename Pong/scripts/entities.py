import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, asset):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.asset = asset
        
    def update(self, movement):
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
    
    def render(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.asset)
