import pygame
from pygame.locals import *
from pathlib import Path
import sys
pygame.init()
WIN_SIZE=(640,480)
window=pygame.display.set_mode(WIN_SIZE)
clock=pygame.time.Clock()
ballX=WIN_SIZE[0]/2;
ballY=WIN_SIZE[1]/2;
FPS=30
BASE_PATH=Path(__file__).resolve().parent
pathToBall=BASE_PATH/'images/download.jpg'
ballImg=pygame.image.load(pathToBall)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keyTuple=pygame.key.get_pressed()
    if keyTuple[pygame.K_LEFT]:ballX-=5
    if keyTuple[pygame.K_RIGHT]: ballX += 5
    if keyTuple[pygame.K_UP]: ballY -= 5
    if keyTuple[pygame.K_DOWN]: ballY += 5

    ballRect=pygame.Rect(ballX, ballY,30,30)
    window.fill((160,230,140))
    window.blit(ballImg, ballRect)
    pygame.display.update()
    clock.tick(FPS)