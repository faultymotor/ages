import sys
 
import pygame
from pygame.locals import *

from ages import calc
 
SCREEN_SHAPE = 500
FPS = 16.0

vor = None

def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    global vor
    if vor:
        vor = calc.lloyd_relaxation(vor, reps=1, size=SCREEN_SHAPE)
    else:
        vor = calc.get_random_voronoi(size=(SCREEN_SHAPE))

BLACK = (0,0,0)
BLUE = (0,204,204)
def draw(screen):
    screen.fill(BLACK)
    for point in vor.points:
        pygame.draw.circle(screen, BLUE, point, 2)
    pygame.display.update()
 
def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_SHAPE,) * 2)

    dt = 1 / FPS 
    while True: 
        update(dt) 
        draw(screen)
        
        dt = fpsClock.tick(FPS)

main()