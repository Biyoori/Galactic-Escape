from settings import *

from utils import loadImage, spawnEnemies
from player import Player
from enemies import Enemy

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Galactic Escape")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.Clock()
        self.running = True

        self.assets = {
            "player": loadImage("Data\Sprites\Player.png"),
            "enemy": loadImage("Data\Sprites\Enemy.png")
        }

        self.enemyList = []
        self.spawnEvent = pygame.USEREVENT + 1

        self.player = Player((WIDTH/2-32, HEIGHT/2-32), self.assets["player"])

    def run(self):
        pygame.time.set_timer(self.spawnEvent, enemySpawnInterval)

        while self.running:
            dt = self.clock.tick(60) / 1000
            
            self.enemyList = [enemy for enemy in self.enemyList if not enemy.pos[1] > HEIGHT]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == self.spawnEvent:
                    spawnEnemies(game, Enemy)

            self.screen.fill(colors["black"])

            if not self.player.isDead:
                self.player.render()
            else:
                self.player.updateAnimation(self.player.deathAnimation)
            self.player.update(dt)
            #pygame.draw.rect(self.screen, colors["green"], self.player.rect)
            
            for enemy in self.enemyList:
                if not enemy.isDead:
                    enemy.render()
                else:
                    enemy.updateAnimation(enemy.deathAnimation)
                enemy.update(dt)
                self.player.enemyCollision(enemy)
            #pygame.draw.rect(self.screen, colors["red"], self.enemy.rect)
            
            pygame.display.update()

            

            

if __name__ == "__main__":
    game = Game()
    game.run()
        

