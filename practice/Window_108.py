import pygame
from pygame.locals import *
import sys
pygame.init()
WIN_SIZE=(640,480)
window=pygame.display.set_mode(WIN_SIZE)
clock=pygame.time.Clock()
ballX=WIN_SIZE[0]/2;
ballY=WIN_SIZE[1]/2;
FPS=30
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill((160, 230, 140))
    pygame.display.update()
    clock.tick(FPS)