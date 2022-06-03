import pygame, sys

screen = pygame.display.set_mode((1024,576), pygame.RESIZABLE + pygame.SCALED)
WINDOW_SIZE = (pygame.display.get_surface().get_size())
size = round(WINDOW_SIZE[0]/20),round(WINDOW_SIZE[1]/14)

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption("Dnd Maps")

# Variables
objecttiles = [] # x, y, num
mouseholding = -1
click = False
editing = False
playertoken = (100,100)
players = [] # x, y, color
makingplayer = -1
color = (0,0,0)
currentkey = ""

# Images

bgl = pygame.image.load('Assets\Background.png').convert()
bg = pygame.transform.scale(bgl, (WINDOW_SIZE))

for x in range(20):
    for y in range(14):
        objecttiles.append([x,y,0])

while True:
    screen.fill((0,125,255))
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                click = False
        if event.type == KEYDOWN:
            if event.key == K_e:
                editing = not editing
            if event.key == K_p:
                makingplayer = 0
            if makingplayer > -1:
                if event.key == pygame.K_BACKSPACE:
                   currentkey = currentkey[:-1]
                   color[makingplayer] = int(currentkey)
                elif event.key == K_0 or event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9 or event.key == K_COMMA:
                    currentkey += event.unicode
                    color[makingplayer] = int(currentkey)
                elif event.key == K_RETURN:
                    players.append(int(color))
                    makingplayer = -1


    if editing:
        WINDOW_SIZE = (pygame.display.get_surface().get_size())
    else:
        WINDOW_SIZE = (pygame.display.get_surface().get_size()[0]/1.25,(pygame.display.get_surface().get_size())[1])
    size = round(WINDOW_SIZE[0]/20),round(WINDOW_SIZE[1]/14)
    bg = pygame.transform.scale(bgl, (WINDOW_SIZE))

    screen.blit(bg,(0,0))

    for tile in objecttiles:
        # Click Handler
        rect = pygame.Rect((tile[0]*size[0],tile[1]*size[1]),(size[0],size[1]))
        # DRAW TILE HANDLER
        if tile[2] == 0:
            pygame.draw.rect(screen, (255,255,255), rect, 1)

        if rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0,0,255), rect) # Mouse hover
    
    for player in players:
        pygame.draw.circle(screen, player, (0,0),size[0]/40)

    if click and mouseholding == -1:
        playertoken = mx,my
    pygame.draw.circle(screen, (255,255,255), playertoken, size[0],1)
    
    pygame.display.flip()