import pygame
from pygame.locals import *

class MyButton():
    def __init__(self,win,loc,upimg,downimg):
        self.window=win
        self.loc=loc
        self.imgup=pygame.image.load(upimg)
        self.imgdown=pygame.image.load(downimg)

        self.rect=self.imgup.get_rect()
        self.rect[0]=loc[0]
        self.rect[1]=loc[1]
        self.state='idle'

    def handleEvent(self,obj):
        if obj.type not in (MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN):
            return False
        pointRect=self.rect.collidepoint(obj.pos)
        if self.state=='idle':
            if obj.type==MOUSEBUTTONDOWN and pointRect:
                self.state='armed'

        elif self.state=='armed':
            if obj.type==MOUSEBUTTONUP and pointRect:
                self.state='idle'
                return True
            if obj.type==MOUSEMOTION and (not pointRect):
                self.state='disarmed'

        elif self.state=='disarmed':
            if pointRect:
                self.state='armed'
            elif obj.type==MOUSEBUTTONUP:
                self.state='idle'
    def draw(self):
        if self.state=='armed':
            self.window.blit(self.imgdown,self.loc)
        else:
            self.window.blit(self.imgup,self.loc)
