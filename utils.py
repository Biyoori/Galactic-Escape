from settings import *
from random import randint

def loadImage(path):
    img = pygame.image.load(path).convert_alpha()
    return img

def spawnEnemies(game, Enemy):
    if len(game.enemyList) < maxEnemies:
        randPos = randint(0, WIDTH)
        enemy = Enemy((randPos, 0), game.assets["enemy"])
        game.enemyList.append(enemy)

def scoreUpdate(game):
    game.scoreText = game.font.render(f"Score: {int(game.score)}", True, colors["white"])
    game.textRect = game.scoreText.get_rect()
    game.textRect.center = (WIDTH-game.textRect.width/2-30, 0+game.textRect.height)
