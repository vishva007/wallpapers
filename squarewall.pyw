
import random
import pygame, sys
import os
from pygame.locals import *

 
pygame.init()
xres = 1400
yres = 800
DISPLAYSURF = pygame.display.set_mode((xres,yres))
anotherSurface = DISPLAYSURF.convert_alpha()
FPS = 200
fpsClock = pygame.time.Clock()
count = 0
pygame.display.set_caption('Welcome Vishva')
x = 0
y = 0
def nextx(x,y):
    if(x==1400):
        return (0,y+100)
    else:
        return (x+100,y)


def gencrd(x):
    return (random.randint(0,x))

while True:
    count = count + 1
    
    if(count%100 == 0):
        pygame.image.save(DISPLAYSURF, "screenshot.jpeg")
    a = 100
    b = 100
    p = []
    if(x==1400):
        x = 0
        y = y+100
    else:
        x = x+100
    
    if(y==800):
        y = 0
        
    
    c = (255-gencrd(255),255-gencrd(255),255-gencrd(255))
    w = 0
    pygame.draw.rect(DISPLAYSURF , c , (x , y , a , b) , w)
    for event in pygame.event.get():
        
        
                
        if event.type == QUIT:
        
            pygame.quit()
            sys.exit()
    
    ##fpsClock.tick(FPS)
    
    pygame.display.update()

