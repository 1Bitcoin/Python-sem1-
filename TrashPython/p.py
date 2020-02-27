import pygame as pg
import pygame 
from pygame.locals import * 
pg.init()

windowColor = Color("lightyellow") 

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game")
clock = pg.time.Clock()


def nlo(sr, x, y, k=1):
    h, w = 30*k, 60*k
    nlo = pg.Surface((3*60, 3*30), pg.SRCALPHA, 32)
    nlo = nlo.convert_alpha()

    pg.draw.ellipse(nlo, (255, 200, 24), pg.Rect(3*w/2, 0, w, h))
    pg.draw.ellipse(nlo, (120, 10, 255), pg.Rect(w, h/3, 2.1*w, 1.5*h))

    sr.blit(nlo, (x, y))


def bg(sc):
    k = 4/5
    pg.draw.rect(sc, 0, (0, 0, WIDTH, HEIGHT*k))
    pg.draw.rect(sc, (0, 128, 0), (0, HEIGHT*k, WIDTH, HEIGHT*(1-k)))

    h, w = 220, 50
    pg.draw.rect(sc, (0, 225, 128), (WIDTH/5,  HEIGHT*k-150, w, h))
   

x, y = WIDTH/2, HEIGHT/1.5
a = 0
k = 1

while True:
    bg(screen)
    #screen.fill(Color("lightblue"))
    
    pygame.draw.polygon(screen, (0, 128, 0),
                        [[0, 600],[0, 500], [300, 500],
                         [400, 550], [800, 550], [800, 600]])
    
    pygame.draw.rect(screen, Color("red"), (20, 400, 260, 100)) 
    pygame.draw.polygon(screen, Color("brown"),
                        [[0, 400], [300, 400],[100, 300]])
    
    pygame.draw.polygon(screen, windowColor,
                        [[100, 380], [210, 380],[130, 360]])
    
    pygame.draw.rect(screen, windowColor, (90, 420, 30, 30)) 
    pygame.draw.rect(screen, windowColor, (170, 420, 30, 30)) 
    pygame.draw.rect(screen, Color("white"), (230, 420, 40, 80))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break
    x += 2
    y -= 0.9
    k -= 0.004
    
    if (x > WIDTH + 60):
        k = 100



    nlo(screen, x, y, k)
    pg.display.flip()
    clock.tick(30)
