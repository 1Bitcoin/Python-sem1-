import pygame
import time

pi = 3.14
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 400
 
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
PINK = (230, 50, 230)
GGG = (255, 255, 125)
 
pygame.init()
 
clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
# радиус и координаты круга
r = 40
x = 50  # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали

Y1 = y - 15
X1 = x - 10

Y2 = y - 15
X2 = x + 10

X3 = x + 10
Y3 = y + 15

X4 = x - 10
Y4 = y + 15

flag = 0

x_1 = X1
y_1 = Y1

x_2 = X2
y_2 = Y2

temp = 0
a = 10

new_flag = 0

while 1:
    time.sleep(0.15)
    
    if flag < 4 and new_flag == 0:
        flag += 1
    elif new_flag == 0:
        flag = 1

    if new_flag == 1 and flag > 0:
        flag -= 1
    elif new_flag == 1:
        flag = 4
        
    sc.fill(GGG)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
 
    pygame.draw.circle(sc, ORANGE, (x, y), r)
    
    pygame.draw.circle(sc, WHITE, (x_1, y_1), 1)
    pygame.draw.circle(sc, WHITE, (x_2, y_2), 1)
    pygame.draw.circle(sc, PINK, (x, y), 7)
 
    pygame.display.update()

    
    if x >= 455:
        #x = 0 - r
        a = -a
        flag = 3
        new_flag = 1
    elif x < 50:
        new_flag = 0
        a = a * (-1)

    x = x + a
    x_1 = x_1 + a
    x_2 = x_2 + a
    temp = temp + a

    if flag == 1:
        x_1 = X2 + temp
        y_1 = Y2 

        x_2 = X3 + temp
        y_2 = Y3 
        

    if flag == 2:
        x_1 = X3 + temp
        y_1 = Y3  

        x_2 = X4 + temp
        y_2 = Y4
        

    if flag == 3:
        x_1 = X4 + temp
        y_1 = Y4

        x_2 = X1 + temp
        y_2 = Y1


    if flag == 4:
        x_1 = X1 + temp
        y_1 = Y1

        x_2 = X2 + temp
        y_2 = Y2
    print(new_flag)
 
    clock.tick(120)
