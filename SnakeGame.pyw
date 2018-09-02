import pygame
import time
import random

pygame.init()

display_width = 608#19
display_height = 512#16
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255 ,0,0)
blocksize = 32
master = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()
def apple(ax , ay):
    pygame.draw.rect(master ,red, [ax*blocksize, ay *blocksize, blocksize,blocksize])
def crash():
    print("SNAKE OVER!")
    time.sleep(2)
    gameloop()
def snake(array):
    for e in range(len(array)):
        pygame.draw.rect(master ,green, [array[e][0]*blocksize,array[e][1]*blocksize, blocksize,blocksize])
def gameloop():
    dirx = -1
    diry = 0
    array = [[11,4]]
    game_exit = False
    snakelen = 4
    ax =random.randrange(display_width/blocksize-1)
    ay =random.randrange(1,display_height/blocksize-1)
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    dirx = -1
                    diry = 0
                if event.key == pygame.K_RIGHT:
                    dirx = 1
                    diry = 0
                if event.key == pygame.K_UP:
                    diry = -1
                    dirx = 0
                if event.key == pygame.K_DOWN:
                    diry = 1
                    dirx = 0
        ##########################
        master.fill(black)
        pygame.draw.rect(master , white , [0,0,display_width,blocksize])
        '''#drawing grid
        for e in range(int(display_width/blocksize)+blocksize):
            pygame.draw.line(master , black , (e * blocksize,0),(e*blocksize,display_height))
        for e in range(int(display_height/blocksize)+blocksize):
            pygame.draw.line(master , black , (0,e * blocksize),(display_width,e*blocksize))
        '''
        apple(ax ,ay)
        array[0][0] += dirx
        array[0][1] += diry
        array.insert(1,[array[0][0],array[0][1]])
        for e in range(len(array)-snakelen):
            array.pop()
        if array[0][0] == ax and array[0][1] == ay:
            snakelen+=1
            ax = random.randrange(display_width/blocksize)
            ay = random.randrange(1,display_height/blocksize)
        for e in range(len(array)):
            if array[e][0] == ax and array[e][1] == ay:
                ax = random.randrange(display_width/blocksize)
                ay = random.randrange(1,display_height/blocksize)
        for e in range(snakelen+1):
            if len(array) == snakelen:
                if e > 2:
                    if array[0][0] == array[e-1][0] and array[0][1] == array[e-1][1]:
                        crash()
        if array[0][0] < 0 or array[0][0] > display_width/blocksize or array[0][1] < 1 or array[0][1] > display_height/blocksize:
            crash()
        print("x: "+ str(ax) + "     y: "+str(ay) + "            snake x: "+ str(array[0][0]) + "   snake y: "+str(array[0][1]))
        snake(array)
        font = pygame.font.SysFont(None , 25)
        text = font.render("POINTS : " + str(snakelen-4),True,black)
        master.blit(text,(50,blocksize/2))
        pygame.display.update()
        clock.tick(5)
gameloop()
pygame.quit()
quit()
