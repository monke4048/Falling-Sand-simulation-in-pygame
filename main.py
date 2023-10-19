import pygame
import pygame.gfxdraw
pygame.init()
width,height = 800,600
win = pygame.display.set_mode((width,height))



blocks = []
gridsize = 8
clock = pygame.time.Clock()
maxHe = (height - gridsize) // gridsize
maxWi = (width - gridsize) // gridsize
x,y = 30,10
dead = True
lx = 10
ly = 10
def Clacultae(maxHe,maxWi,xpos,ypos,static,blocks):
        if ypos < maxHe and [xpos,ypos + 1,1,0] not in blocks and [xpos,ypos + 1,2,0] not in blocks:
                        ypos += 1
                        static = 1
        elif ypos < maxHe and xpos < maxWi and [xpos + 1,ypos + 1,1,0] not in blocks and [xpos + 1,ypos + 1,2,0] not in blocks and [xpos + 1,ypos,2,0] not in blocks:
                        xpos += 1
                        ypos += 1
                        static = 1
        elif ypos < maxHe and xpos > 0 and [xpos - 1,ypos + 1,1,0] not in blocks and [xpos - 1,ypos + 1,2,0] not in blocks and [xpos - 1,ypos,2,0] not in blocks:
                xpos -= 1
                ypos += 1
                static = 1
        else:
                static = 0
        
        return xpos,ypos,static
      
while True:
    mKEY = pygame.mouse.get_pressed()
    win.fill((146,144,255))
    pygame.display.set_caption(str(clock.get_fps()))
    for g in pygame.event.get():
        if g.type == pygame.KEYDOWN:
              if g.key == pygame.K_SPACE:
                    dead = False        
        if g.type == pygame.QUIT:
            print(len(blocks))
            pygame.quit()
    if mKEY[0]:
        m = pygame.mouse.get_pos()
        if [m[0] //gridsize,m[1]//gridsize,2,0]:
               if [m[0] //gridsize,m[1]//gridsize,1,1] not in blocks:
                        blocks.append([m[0] //gridsize,m[1]//gridsize,1,1])
    if mKEY[2]:
        m = pygame.mouse.get_pos()
        
        if [m[0] //gridsize,m[1]//gridsize,2,0] not in blocks:
               if [m[0] //gridsize,m[1]//gridsize,1,1] not in blocks :
                        blocks.append([m[0] //gridsize,m[1]//gridsize,2,0])
    
    for i in blocks:
        if i[2] == 1:
                if i[3] == 1:
                        i[0],i[1],i[3] = Clacultae(maxHe,maxWi,i[0],i[1],i[3],blocks)
                pygame.draw.rect(win,(255,255,0),(i[0]* gridsize,i[1] * gridsize,gridsize,gridsize))
        if i[2] == 2:
             pygame.draw.rect(win,(107,109,0),(i[0] * gridsize,i[1]*gridsize,gridsize,gridsize))
    pygame.display.flip()
    clock.tick(1000000000000000000)

#1 - sand
#2 - stone
b = [                                                                                                             [16, 10, 1 ,1,1], [17, 10, 1 ,1,1], [18, 10, 1 ,1,1], [19, 10, 1 ,1,1],
                                                            [13, 11, 1 ,1,2]                  , [15, 11, 1 ,1,1], [16, 11, 1 ,1,1], [17, 11, 1 ,1,1], [18, 11, 1 ,1,1], [19, 11, 1 ,1,1], [20, 11, 1 ,1,1],                   [22, 11, 1 ,1,2], 
                        [11, 12, 1 ,1,2], [12, 12, 1 ,1,2], [13, 12, 1 ,1,2], [14, 12, 1 ,1,3], [15, 12, 1 ,1,2], [16, 12, 1 ,1,3], [17, 12, 1 ,1,2], [18, 12, 1 ,1,2], [19, 12, 1 ,1,3], [20, 12, 1 ,1,2], [21, 12, 1 ,1,3], [22, 12, 1 ,1,2], [23, 12, 1 ,1,2], [24, 12, 1 ,1,2],
                        [11, 13, 1 ,1,2], [12, 13, 1 ,1,2], [13, 13, 1 ,1,3], [14, 13, 1 ,1,3], [15, 13, 1 ,1,2], [16, 13, 1 ,1,3], [17, 13, 1 ,1,2], [18, 13, 1 ,1,2], [19, 13, 1 ,1,3], [20, 13, 1 ,1,2], [21, 13, 1 ,1,3], [22, 13, 1 ,1,3], [23, 13, 1 ,1,2], [24, 13, 1 ,1,2],
                        [11, 14, 1 ,1,2], [12, 14, 1 ,1,2], [13, 14, 1 ,1,3], [14, 14, 1 ,1,3], [15, 14, 1 ,1,3], [16, 14, 1 ,1,2], [17, 14, 1 ,1,2], [18, 14, 1 ,1,2], [19, 14, 1 ,1,2], [20, 14, 1 ,1,3], [21, 14, 1 ,1,3], [22, 14, 1 ,1,3], [23, 14, 1 ,1,2], [24, 14, 1 ,1,2],
                                                            [13, 15, 1 ,1,3], [14, 15, 1 ,1,3], [15, 15, 1 ,1,3], [16, 15, 1 ,1,3], [17, 15, 1 ,1,2], [18, 15, 1 ,1,2], [19, 15, 1 ,1,3], [20, 15, 1 ,1,3], [21, 15, 1 ,1,3], [22, 15, 1 ,1,3],
                                                                              [14, 16, 1 ,1,3], [15, 16, 1 ,1,2], [16, 16, 1 ,1,3], [17, 16, 1 ,1,3], [18, 16, 1 ,1,3], [19, 16, 1 ,1,3], [20, 16, 1 ,1,2], [21, 16, 1 ,1,3],
                                                                              [14, 17, 1 ,1,3], [15, 17, 1 ,1,2], [16, 17, 1 ,1,2], [17, 17, 1 ,1,2], [18, 17, 1 ,1,2], [19, 17, 1 ,1,2], [20, 17, 1 ,1,2], [21, 17, 1 ,1,3],
                                                            [13, 18, 1 ,1,1], [14, 18, 1 ,1,1], [15, 18, 1 ,1,1], [16, 18, 1 ,1,2], [17, 18, 1 ,1,2], [18, 18, 1 ,1,2], [19, 18, 1 ,1,2], [20, 18, 1 ,1,1], [21, 18, 1 ,1,1], [22, 18, 1 ,1,1],
                                          [12, 19, 1 ,1,3], [13, 19, 1 ,1,3], [14, 19, 1 ,1,1], [15, 19, 1 ,1,1], [16, 19, 1 ,1,3], [17, 19, 1 ,1,3], [18, 19, 1 ,1,3], [19, 19, 1 ,1,3], [20, 19, 1 ,1,1], [21, 19, 1 ,1,1], [22, 19, 1 ,1,3], [23, 19, 1 ,1,3],
                                          [12, 20, 1 ,1,3], [13, 20, 1 ,1,3], [14, 20, 1 ,1,3], [15, 20, 1 ,1,1], [16, 20, 1 ,1,1], [17, 20, 1 ,1,3], [18, 20, 1 ,1,3], [19, 20, 1 ,1,1], [20, 20, 1 ,1,1], [21, 20, 1 ,1,3], [22, 20, 1 ,1,3], [23, 20, 1 ,1,3],
                                          [12, 21, 1 ,1,3], [13, 21, 1 ,1,3], [14, 21, 1 ,1,3], [15, 21, 1 ,1,1], [16, 21, 1 ,1,2], [17, 21, 1 ,1,1], [18, 21, 1 ,1,1], [19, 21, 1 ,1,2], [20, 21, 1 ,1,1], [21, 21, 1 ,1,3], [22, 21, 1 ,1,3], [23, 21, 1 ,1,3],
                                          [12, 22, 1 ,1,3], [13, 22, 1 ,1,3], [14, 22, 1 ,1,3], [15, 22, 1 ,1,1], [16, 22, 1 ,1,1], [17, 22, 1 ,1,1], [18, 22, 1 ,1,1], [19, 22, 1 ,1,1], [20, 22, 1 ,1,1], [21, 22, 1 ,1,3], [22, 22, 1 ,1,3], [23, 22, 1 ,1,3],
                                                            [13, 23, 1 ,1,3], [14, 23, 1 ,1,3], [15, 23, 1 ,1,1], [16, 23, 1 ,1,1], [17, 23, 1 ,1,1], [18, 23, 1 ,1,1], [19, 23, 1 ,1,1], [20, 23, 1 ,1,1], [21, 23, 1 ,1,3], [22, 23, 1 ,1,3] ]