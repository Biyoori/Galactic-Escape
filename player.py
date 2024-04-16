from settings import *
from entities import Entity

class Player(Entity):
    def __init__(self, pos, sprite) -> None:
        super().__init__(pos, sprite)
        self.rect = sprite.get_frect(topleft = pos)

        #movement
        self.direction = vector()
        self.speed = 200

        self.deathAnimation = self.loadAnimation(0, 8, "Data\Sprites\Explosion.png")

    def input(self):
        keys = pygame.key.get_pressed()

        inputVector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            inputVector.x += 1
        if keys[pygame.K_LEFT]:
            inputVector.x -= 1
        if keys[pygame.K_UP]:
            inputVector.y -= 1
        if keys[pygame.K_DOWN]:
            inputVector.y += 1

        self.direction = inputVector.normalize() if inputVector else inputVector

    def move(self, dt):
        #Movement
        self.pos = self.rect.topleft
        self.rect.topleft += self.direction * self.speed * dt
        #Screen Bounds
        #Left
        if self.rect.left <= 0:
            self.rect.left = 0
        #Right
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        #Up
        if self.rect.top <= 0:
            self.rect.top = 0
        #Down
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
    
    def enemyCollision(self, enemy):
        if self.rect.colliderect(enemy.rect) and not self.isDead:
            self.isDead = True
            enemy.isDead = True
            print('boom')      

    def update(self, dt):
        self.input()
        self.move(dt)
    