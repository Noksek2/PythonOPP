import pygame
from pygame.locals import *

pygame.font.init()
class GameText():
    def __init__(self,win,text,col,pos):
        self.win=win
        self.font=pygame.font.SysFont(None,30)
        self.col=col
        self.set_txt(text)
        self.pos=pos

    def set_txt(self,s):
        self.txtval=s
        self.txtrend=self.font.render(self.txtval,True,self.col)
    def draw(self):
        self.win.blit(self.txtrend,self.pos)
