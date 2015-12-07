import pygame
from entity import Entity
from ennemy import RedEnnemy, GreenEnnemy
from glob import *
import random

class   Level:
    def __init__(self, filename):
        self.filename = filename
        self.entities = []
        self.green = 0
        self.red = 0
        self.wall = pygame.image.load("wall.bmp")
        self.out = pygame.image.load("out.png")
        with open(filename, "r") as f:
            lines = [l.rstrip("\r\n") for l in f]
            self.maxRed = int(lines[0])
            self.maxGreen = int(lines[1])
            self.w = int(lines[2])
            self.h = int(lines[3])
            self.level = "".join(lines[4:])
            self.level = list(map(lambda x: '0' if x=="v" or x=="r" else x, self.level))

    def getStart(self):
        for j, i in enumerate(self.level):
            if i == 'j':
                self.level[j] = '1'
                return (j % self.w, j // self.h)
        return (0, 0)

    def blit(self, screen):
        for j, i in enumerate(self.level):
            rect = self.wall.get_rect()
            rect.x = (j % self.w) * 15
            rect.y = (j // self.h) * 15
            if i == 's':
                screen.blit(self.out, rect)
            elif i == '0':
                screen.blit(self.wall, rect)
        for e in self.entities:
            e.blit(screen)

    def move(self, perso):
        for e in self.entities:
            e.move(self, perso)
        r = random.randint(0, 1000)
        pos = (random.randint(0, self.w), random.randint(0, self.h))
        while self.canMove(pos) == WALL or pos == perso.getPos():
            pos = (random.randint(0, self.w), random.randint(0, self.h))
        if r < 20:
            self.red += 1
            if self.red <= self.maxRed:
                self.entities.append(RedEnnemy(pos))
        elif r < 40:
            self.green += 1
            if self.green <= self.maxGreen:
                self.entities.append(GreenEnnemy(pos))

    def canMove(self, pos):
        if pos[0] < 0 or pos[0] >= self.w or pos[1] < 0 or pos[1] >= self.h:
            return WALL
        res = self.level[int(pos[0]) + int(pos[1]) * self.w]
        if res == '0':
            return WALL
        elif res == 's':
            return FINISH
        else:
            for e in self.entities:
                if e.getPos() == pos:
                    if type(e).__name__ == "RedEnnemy":
                        return REDENNEMY
                    else:
                        return GREENENNEMY
        return NOTHING
