
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
x = 0
y = 0

def gencrd(x):
    return (random.randint(0,x))
while True:
    count = count + 1
    ##if(count%1000 == 0):
        ##fpsClock.tick(2000) 
        ##DISPLAYSURF.fill((gencrd(255),gencrd(255),gencrd(255)))
    if(count%10000 == 0):
        pygame.image.save(DISPLAYSURF, "screenshot.jpeg")
    a = gencrd(1366)
    b = gencrd(768)
   
    c = (255-gencrd(255),255-gencrd(255),255-gencrd(255))
    
    pygame.draw.line(DISPLAYSURF , c , (x,y) , (a,b))
    x = a
    y = b
    
    for event in pygame.event.get():
        
        
                
        if event.type == QUIT:
        
            pygame.quit()
            sys.exit()
    
    ##fpsClock.tick(FPS)
    fpsClock.tick(2000)
    pygame.display.update()

