# Universidad del Valle de Guatemala
# Gráficas por computadora
# Christopher García 20541
# Raycaster - Proyecto#3

import pygame
from pygame.locals import *
from OpenGL.GL import *
from utilities import *
from texts import *
from math import atan2, cos, pi, sin

width = 1000
height = 500
            
pygame.init()
screen = pygame.display.set_mode((width, height))
r = Raycaster(screen)

pygame.mixer.init()
pygame.mixer.music.load('./Music.mp3')
pygame.mixer.music.play(-1)

imageStart = pygame.image.load('./DoomStart.png').convert()

fps = FPS()
PAUSE = Pause()

running = True
runningM = True
runningM2 = True
runningM3 = True

Mdisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Doom chafa')

center = 0, height//2

buttonA = Button("Mapa 1", (330, 250))
buttonB = Button("Mapa 2", (630, 250))

while running:
    
    # Pantalla de inicio
    while runningM:
        Mdisplay.blit(imageStart, (-50, 0)) # DoomStart
        # Mdisplay.blit(imageStart, (425, 150)) # Win
        pygame.display.flip()
    
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                runningM = False
                running = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    runningM = False
                    running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    runningM = False
                    running = False
        
    # Sección de controles
    while runningM2:
        
        Mdisplay.fill(BLACK)
        
        Mdisplay.blit(title1, titleRc1)
        Mdisplay.blit(title2, titleRc2)
        Mdisplay.blit(title3, titleRc3)
        Mdisplay.blit(title4, titleRc4)
        Mdisplay.blit(title5, titleRc5)
        Mdisplay.blit(title6, titleRc6)
        Mdisplay.blit(title7, titleRc7)
        
        pygame.display.flip()
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                runningM2 = False
                running = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    runningM2 = False
                    running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    runningM2 = False

    # Pantalla de selección niveles
    while runningM3:
        Mdisplay.fill(BLACK)
        buttonA.show(screen)
        buttonB.show(screen)
        Mdisplay.blit(title7, titleRc7)
        pygame.display.flip()

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                runningM3 = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    runningM3 = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    runningM3 = False
            
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if buttonA.rect.collidepoint(x, y):
                        r.load_map('./map.txt')
                    elif buttonB.rect.collidepoint(x, y):
                        r.load_map('./map2.txt')

    if r.map == []:
        r.load_map('./map.txt')

    running = True

    # Renderizado juego
    screen.fill(BLACK, (0, 0, r.width/2, r.height))
    screen.fill(SKY, (r.width/2, 0, r.width, r.height/2))
    screen.fill(GROUND, (r.width/2, r.height/2, r.width, r.height/2))
    
    r.clearZ()
    r.render()
    
    fps.render(screen)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        
        #--> Descomentar esto para usar mouse como cámara horizontal 
        
        # mouse_pos = pygame.mouse.get_pos()
        # xM = (mouse_pos[0] - center[0])**2
        # r.player["a"] = xM/100000

        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                running = False
                
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                r.player["a"] -= pi/15
            if event.key == pygame.K_d:
                r.player["a"] += pi/15
                
            if event.key == pygame.K_p:
                PAUSE.toggle()
                
            if event.key == pygame.K_RIGHT:
                r.player["x"] -= int(10 * sin(r.player["a"]))
                r.player["y"] += int(10 * cos(r.player["a"]))
            if event.key == pygame.K_LEFT:
                r.player["x"] += int(10 * sin(r.player["a"]))
                r.player["y"] -= int(10 * cos(r.player["a"]))
            if event.key == pygame.K_UP:
                r.player["x"] += int(10 * cos(r.player["a"]))
                r.player["y"] += int(10 * sin(r.player["a"]))
            if event.key == pygame.K_DOWN:
                r.player["x"] -= int(10 * cos(r.player["a"]))
                r.player["y"] -= int(10 * sin(r.player["a"]))
                
    pygame.display.update()
    fps.clock.tick(60)
    
    