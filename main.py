# Universidad del Valle de Guatemala
# Gráficas por computadora
# Christopher García 20541
# Raycaster

# Conway’s Game Of Life
# Referencia: https://inventwithpython.com/bigbookpython/project13.html

import sys
import time
import pygame
from OpenGL.GL import *
from pixels import *

pygame.init()

width = 375
height = 375

screen = pygame.display.set_mode(
    (width, height),
    pygame.OPENGL | pygame.DOUBLEBUF
)

delayT = 0

pixels = generate_init_positions(width, height)

running = True
while running:
    # Clear
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Paint
    pixelsT = pixels
    
    for key in pixelsT.keys():
        pixel(key[0], key[1], pixelsT[key])
        
    for x in range(width):
        for y in range(height):

            NumN = 0
            left, right, above, below = get_neighbors_coords(x, y, width, height)

            # Se busca la cantidad de vecinos vivos
            # Esquina superior izquierda
            if pixelsT[(left, above)] == ALIVE:
                NumN += 1  
            # Centro superior
            if pixelsT[(x, above)] == ALIVE:
                NumN += 1 
            # Esquina superior derecha   
            if pixelsT[(right, above)] == ALIVE:
                NumN += 1 
            # Centro izquierdo
            if pixelsT[(left, y)] == ALIVE:
                NumN += 1
            # Centro derecho
            if pixelsT[(right, y)] == ALIVE:
                NumN += 1
            # Esquina inferior izquierda
            if pixelsT[(left, below)] == ALIVE:
                NumN += 1
            # Centro inferior
            if pixelsT[(x, below)] == ALIVE:
                NumN += 1
            # Esquina superior derecha
            if pixelsT[(right, below)] == ALIVE:
                NumN += 1

            # Reglas
            if pixelsT[(x, y)] == ALIVE and (NumN == 2 or NumN == 3):
                pixels[(x, y)] = ALIVE
                
            elif pixelsT[(x, y)] == DEAD and NumN == 3:
                pixels[(x, y)] = ALIVE
                
            else:
                pixels[(x, y)] = DEAD
                
    # Flip
    pygame.display.flip()

    try:
        time.sleep(delayT)
    except KeyboardInterrupt:
        sys.exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    