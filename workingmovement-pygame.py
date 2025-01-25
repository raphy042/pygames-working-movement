

x=0
y=80
width=1500
height=1000
vel = 1
r=0
g=255
b=0
size =1
import pygame
pygame.init()
win = pygame.display.set_mode((width, height))
run = True

    

while run:
    ##colorchange
    if r==255:
        g=255
        r=0
        b=0
    elif g==255:
        g=0
        r=0
        b=255
    elif b==255:
        r=255
        g=0
        b=0

    ##keypress
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    
    ##bounds
    


    pygame.draw.rect(win, (r,g,b), (x, y, size, size))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('quit')
pygame.quit()
