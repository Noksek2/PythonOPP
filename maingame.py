import pygame
import sys 
from GameText import *
from GameButton import *

pygame.init()
WIN_SIZE=(640,480) 
window=pygame.display.set_mode(WIN_SIZE) 
clock=pygame.time.Clock()
FPS=30


btn=GameButton(window,'BTN',50,50)
while True: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        btn.handle(event)
    window.fill((255,255,255))

    #버튼 그리기
    btn.draw()
    pygame.display.update()
    clock.tick(FPS)
