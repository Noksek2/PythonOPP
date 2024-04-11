import pygame
from pygame.locals import *
from pathlib import Path
import sys
from MyWidget import *
import random
from Ball import *


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
myBtn1=MyButton(window,(100,100),'images/btn1.png','images/btn2.png')
myBtn2=MyButton(window,(100,150),'images/btn1.png','images/btn2.png')

myball=Ball(window,WIN_SIZE[0],WIN_SIZE[1])

while True:
    ballRect = pygame.Rect(ballX, ballY, 50, 50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if ballRect.collidepoint(event.pos):
                ballX,ballY=event.pos
        myBtn1.handleEvent(event)
        myBtn2.handleEvent(event)

    keyTuple=pygame.key.get_pressed()
    if keyTuple[pygame.K_LEFT]:ballX-=5
    if keyTuple[pygame.K_RIGHT]: ballX += 5
    if keyTuple[pygame.K_UP]: ballY -= 5
    if keyTuple[pygame.K_DOWN]: ballY += 5
    myball.update()

    window.fill((160,230,140))
    window.blit(ballImg, ballRect)
    myBtn1.draw()
    myBtn2.draw()
    myball.draw()

    pygame.display.update()
    clock.tick(FPS)