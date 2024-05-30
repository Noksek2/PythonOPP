import pygame
from pygame.locals import *
from GameText import *

class GameButton():
    def __init__(self,win,txt,x,y,w=50,h=50):
        self.state='idle'
        self.win=win
        self.rect=(x,y,w,h)
        self.rect2=(x+2,y+2,w,h)
        self.txt=GameText(win,txt,(0,0,0),(x,y+h/2-15))
        self.fn=None
    def handle(self,event):
        if event.type==MOUSEBUTTONDOWN or event.type==MOUSEMOTION:
            mpos=pygame.mouse.get_pos()
            if Rect(self.rect).collidepoint(mpos):
                if  event.type==MOUSEMOTION:self.state='over'
                else:self.state='push'
            else:self.state='idle'
            
        elif event.type==MOUSEBUTTONUP:self.state='idle'

        if self.state=='push' and self.fn is not None:self.fn.call()
    def draw(self):
        if self.state=='idle':
            pygame.draw.rect(self.win,(0,0,0),self.rect2)
            pygame.draw.rect(self.win,(150,150,150),self.rect)
        elif self.state=='over':
            pygame.draw.rect(self.win,(0,0,0),self.rect2)
            pygame.draw.rect(self.win,(100,100,100),self.rect)
        else:
            pygame.draw.rect(self.win,(50,50,50),self.rect2)
        self.txt.draw()
