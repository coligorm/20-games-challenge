import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, asset):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.asset = asset
        self.velocity = [1, 1]
        
    def update(self, movement):
        frame_movement = (movement[0], movement[1])
        self.pos[0] += frame_movement[0] * 5
        self.pos[1] += frame_movement[1] * 5
        
        # Screen boundary check
        if self.pos[1] > 0 and self.pos[1] < self.game.screen.get_height() - self.size[1]:
            self.asset.x = self.pos[0]
            self.asset.y = self.pos[1]
        elif self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] > self.game.screen.get_height() - self.size[1]:
            self.pos[1] = self.game.screen.get_height() - self.size[1]
    
    def render(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.asset)
