import pygame
from pygame import Vector2 as vector

WIDTH, HEIGHT = 800, 600

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (200, 30, 30),
    "green": (30, 200, 30),
    "blue": (30, 30, 200)
}

maxEnemies = 20
enemySpawnInterval = 200