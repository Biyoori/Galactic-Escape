from entities import Entity
from settings import *

class Enemy(Entity):
    def __init__(self, pos, sprite) -> None:
        super().__init__(pos, sprite)
        self.rect = sprite.get_frect(topleft = pos)

        #Movement
        self.direction = vector(0,1)
        self.speed = 250

        self.deathAnimation = self.loadAnimation(0, 8, "Data\Sprites\Explosion.png")

    def move(self, dt):
        self.pos = self.rect.topleft
        if not self.isDead:
            self.rect.topleft += self.direction * self.speed * dt

    def update(self, dt):
        self.move(dt)