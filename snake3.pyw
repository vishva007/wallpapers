
import random
import pygame, sys
import os
from pygame.locals import *

 
pygame.init()
xres = 1366
yres = 768
DISPLAYSURF = pygame.display.set_mode((xres,yres))
anotherSurface = DISPLAYSURF.convert_alpha()
FPS = 200
fpsClock = pygame.time.Clock()
count = 0
pygame.display.set_caption('Welcome Vishva')


def gencrd(x):
    return (random.randint(0,x))
while True:
    count = count + 1
    ##if(count%1000 == 0):
        ##fpsClock.tick(2000) 
        ##DISPLAYSURF.fill((gencrd(255),gencrd(255),gencrd(255)))
    if(count%10000 == 0):
        pygame.image.save(DISPLAYSURF, "screenshot.jpeg")
    a = gencrd(100)
    b = gencrd(100)
    x = gencrd(1366)
    y = gencrd(768)
    c = (255-gencrd(255),255-gencrd(255),255-gencrd(255))
    
    pygame.draw.rect(DISPLAYSURF , c , (x , y , a , b) , 0)
    for event in pygame.event.get():
        ##fpsClock.tick(FPS)
        
                
        if event.type == QUIT:
        
            pygame.quit()
            sys.exit()
    
    ##fpsClock.tick(FPS)
    
    pygame.display.update()

