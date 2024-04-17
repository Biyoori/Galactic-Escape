from settings import *
from utils import loadImage

class Entity:
    def __init__(self, pos, sprite) -> None:
        self.surface = pygame.display.get_surface()
        self.pos = pos
        self.sprite = sprite

        self.currentFrame = 0
        self.isDead = False

    def render(self):
        self.surface.blit(self.sprite, self.pos)

    def loadAnimation(self, startIndex, endIndex, path):
        frameWidth, frameHeight = 32, 32
        frames = []
        spritesheet = loadImage(path)
        for i in range(startIndex * frameWidth, endIndex * frameWidth, frameWidth):
            frame = spritesheet.subsurface((i, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames
    
    def updateAnimation(self, animation):
        self.currentFrame += 0.1
        if self.currentFrame < len(animation):
            self.surface.blit(animation[int(self.currentFrame)], self.pos)
        
