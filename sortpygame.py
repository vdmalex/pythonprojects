import pygame
import random
import sys

colors = [
(255,0,0),
(0,255,0),
(0,0,255)]
color=colors[0]
colorsLen = len(colors)


def randomRec():
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    width = random.randint(0, 50)
    height = random.randint(0, 100)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return pygame.Rect(x, y, width, height)
    #pygame.draw.rect(surface, (r, g, b), rr)

def handle_keys(r):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:       
                return pygame.Rect.move(r,0,-1)
            elif event.key == pygame.K_DOWN:
                return pygame.Rect.move(r,0,1)
            elif event.key == pygame.K_LEFT:
                return pygame.Rect.move(r,-1,0)
            elif event.key == pygame.K_RIGHT:
                return pygame.Rect.move(r,1,0)
        else:
            return r
    return r
# todo fading rectange multithreading


     
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)


screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    #r=randomRec()
    rr=pygame.Rect(50, 50, 50, 50)
    #p=pygame.Rect(50, 50, 50, 50)
    color=(0,0,0)
    r=255
    g=0
    b=0
    #print(((r==255) & (g == 0) & (b==0)))
    #pygame.draw.rect(surface, (0, 0, 0), p)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(10000)
        #randomRec(surface)
        #r=pygame.Rect.move(r,40,10)
        #print(pygame.mouse.get_pressed())
        test=pygame.mouse.get_pressed()
        #drawGrid(surface)
        coord=pygame.mouse.get_pos()
       
        if test[0]:
            
            #print(color)
            
            #if (((coord[0]<40) & (coord[0]>1)) &((coord[1]<40) & (coord[1]>1))):
            if pygame.Rect.collidepoint(rr, pygame.mouse.get_pos()):
                #print(coord)
                x=random.randint(0,colorsLen-1)
                color=colors[x]
                #print(color)
        
            #print(color)
            pygame.draw.circle(surface,(color),coord,3)
        if test[1]:
            if ((r==255) & (g < 255) & (b==0)):
                g+=1
            elif((r>0) & (g == 255) & (b==0)):
                r-=1
            elif((r==0) & (g == 255) & (b<255)):
                b+=1
            elif((r==0) & (g > 0) & (b==255)):
                g-=1
            elif((r<255) & (g == 0) & (b==255)):
                r+=1
            elif((r==255) & (g == 0) & (b>0)):
                b-=1

            

            #(r<255)
            #(g<255)
            #(b<255)
            print(r)
            print(g)
            print(b)
            pygame.draw.circle(surface,(r,g,b),coord,3)
        #p=handle_keys(p)
        #pygame.Rect.update(p,coord[0],coord[1])
        #print(pygame.Rect.update(p,0,0))
        #print(coord)
        #r=randomRec()
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        #pygame.draw.rect(surface, (red, green, blue), r)

        #pygame.draw.rect(surface, (0, 0, 0), p)

        screen.blit(surface, (0, 0))
        pygame.display.update()
        


main()
