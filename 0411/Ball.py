import pygame
from pygame.locals import*
import random

class Ball():
    def __init__(self,win,winW,winH):
        self.win=win
        self.winW=winW
        self.winH=winH
        self.image=pygame.image.load('images/ball.png')

        ballRect=self.image.get_rect()
        self.ballW=ballRect.width
        self.ballH = ballRect.height

        self.maxW=winW-self.ballW
        self.maxH=winH-self.ballH

        self.x=random.randint(0,self.maxW)
        self.y = random.randint(0, self.maxH)

        self.xspeed=random.choice([-2,1,1,2])
        self.yspeed=random.choice([-2,1,1,2])
    def update(self):
        if self.x<0 or self.x>=self.maxW:
            self.xspeed=-self.xspeed

        if self.y<0 or self.y>=self.maxH:
            self.yspeed=-self.yspeed

        self.x+=self.xspeed
        self.y+=self.yspeed
    def draw(s):
        s.win.blit(s.image,(s.x,s.y))