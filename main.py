import pygame
pygame.init()
width,height = 800,600
win = pygame.display.set_mode((width,height))
blocks = [[2,3,1,1]]
gridsize = 4
clock = pygame.time.Clock()
maxHe = (height - gridsize) // gridsize
maxWi = (width - gridsize) // gridsize
while True:
    mKEY = pygame.mouse.get_pressed()
    win.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))
    for g in pygame.event.get():
        if g.type == pygame.QUIT:
            print(len(blocks))
            pygame.quit()
    
    if mKEY[0]:
        m = pygame.mouse.get_pos()
        if [m[0] //gridsize,m[1]//gridsize,1] not in blocks and [m[0] //gridsize,m[1]//gridsize,2] not in blocks:
            blocks.append([m[0] //gridsize,m[1]//gridsize,1,1])
    if mKEY[2]:
        m = pygame.mouse.get_pos()
        if [m[0] //gridsize,m[1]//gridsize,2] not in blocks and [m[0] //gridsize,m[1]//gridsize,1] not in blocks:
            blocks.append([m[0] //gridsize,m[1]//gridsize,2,0])
    
    for i in blocks:
        if i[2] == 1:
                if i[3] == 1:
                        if i[1] < maxHe and [i[0],i[1] + 1,1,0] not in blocks and [i[0],i[1] + 1,2,0] not in blocks:
                                i[1] += 1
                        elif i[1] < maxHe and i[0] < maxWi and [i[0] + 1,i[1] + 1,1,0] not in blocks and [i[0] + 1,i[1] + 1,2,0] not in blocks and [i[0] + 1,i[1] ,2,0] not in blocks:
                                i[0] += 1
                                i[1] += 1
                        elif i[1] < maxHe and i[0] > 0 and [i[0] - 1,i[1] + 1,1,0] not in blocks and [i[0] - 1,i[1] + 1,2,0] not in blocks and [i[0] - 1,i[1],2,0] not in blocks:
                                i[0] -= 1
                                i[1] += 1
                        else:
                                i[3] = 0
                pygame.draw.rect(win,(109,68,46),(i[0] * gridsize,i[1]*gridsize,gridsize,gridsize))
        if i[2] == 2:
            pygame.draw.rect(win,(127,127,127),(i[0] * gridsize,i[1]*gridsize,gridsize,gridsize))
    pygame.display.flip()
    clock.tick(1200000000000)
