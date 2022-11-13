# Universidad del Valle de Guatemala
# Gráficas por computadora
# Christopher García 20541
# Raycaster

from random import *
import numpy as np
from OpenGL.GL import *

init_pixels = []
ALIVE = (0.0, 1.0, 0.0)
DEAD = (0.0, 0.0, 0.0)


def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 2, 2)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


def generate_init_positions(width, height):

    positions = {
        # Corners
        (9, 10): ALIVE, (10, 10): ALIVE, (11, 10): ALIVE,
        (49, 10): ALIVE, (50, 10): ALIVE, (51, 10): ALIVE,
        (89, 10): ALIVE, (90, 10): ALIVE, (91, 10): ALIVE,

        (8, 8): ALIVE, (12, 8): ALIVE, (8, 12): ALIVE, (12, 12): ALIVE,
        (48, 8): ALIVE, (52, 8): ALIVE, (48, 12): ALIVE, (52, 12): ALIVE,
        (88, 8): ALIVE, (92, 8): ALIVE, (88, 12): ALIVE, (92, 12): ALIVE,
        (8, 48): ALIVE, (12, 48): ALIVE, (8, 52): ALIVE, (12, 52): ALIVE,
        (48, 48): ALIVE, (52, 48): ALIVE, (48, 52): ALIVE, (52, 52): ALIVE,
        (88, 48): ALIVE, (92, 48): ALIVE, (88, 52): ALIVE, (92, 52): ALIVE,
        (8, 88): ALIVE, (12, 88): ALIVE, (8, 92): ALIVE, (12, 92): ALIVE,
        (48, 88): ALIVE, (52, 88): ALIVE, (48, 92): ALIVE, (52, 92): ALIVE,
        (88, 88): ALIVE, (92, 88): ALIVE, (88, 92): ALIVE, (92, 92): ALIVE,

        (9, 50): ALIVE, (10, 50): ALIVE, (11, 50): ALIVE,
        (49, 50): ALIVE, (50, 50): ALIVE, (51, 50): ALIVE,
        (89, 50): ALIVE, (90, 50): ALIVE, (91, 50): ALIVE,

        (9, 90): ALIVE, (10, 90): ALIVE, (11, 90): ALIVE,
        (49, 90): ALIVE, (50, 90): ALIVE, (51, 90): ALIVE,
        (89, 90): ALIVE, (90, 90): ALIVE, (91, 90): ALIVE,

        # Up left
        # Diagonal center
        (13, 87): ALIVE, (14, 86): ALIVE, (15, 85): ALIVE, (16, 84): ALIVE,
        (17, 83): ALIVE, (18, 82): ALIVE, (19, 81): ALIVE, (20, 80): ALIVE,
        (21, 79): ALIVE, (22, 78): ALIVE, (23, 77): ALIVE, (24, 76): ALIVE,
        (25, 75): ALIVE, (26, 74): ALIVE, (27, 73): ALIVE,

        # Diagonal up center

        (9, 87): ALIVE, (10, 86): ALIVE, (11, 85): ALIVE, (12, 84): ALIVE,
        (13, 83): ALIVE, (14, 82): ALIVE, (15, 81): ALIVE, (16, 80): ALIVE,
        (17, 79): ALIVE, (18, 78): ALIVE, (19, 77): ALIVE, (20, 76): ALIVE,
        (21, 75): ALIVE, (22, 74): ALIVE, (23, 73): ALIVE, (24, 72): ALIVE,
        (25, 71): ALIVE,

        # Diagonal down center

        (13, 91): ALIVE, (14, 90): ALIVE, (15, 89): ALIVE, (16, 88): ALIVE,
        (17, 87): ALIVE, (18, 86): ALIVE, (19, 85): ALIVE, (20, 84): ALIVE,
        (21, 83): ALIVE, (22, 82): ALIVE, (23, 81): ALIVE, (24, 80): ALIVE,
        (25, 79): ALIVE, (26, 78): ALIVE, (27, 77): ALIVE, (28, 76): ALIVE,
        (29, 75): ALIVE, (30, 74): ALIVE, (31, 73): ALIVE,

        # Up right
        # Diagonal center
        (87, 87): ALIVE, (86, 86): ALIVE, (85, 85): ALIVE, (84, 84): ALIVE,
        (83, 83): ALIVE, (82, 82): ALIVE, (81, 81): ALIVE, (80, 80): ALIVE,
        (79, 79): ALIVE, (78, 78): ALIVE, (77, 77): ALIVE, (76, 76): ALIVE,
        (75, 75): ALIVE, (74, 74): ALIVE, (73, 73): ALIVE,

        # Diagonal up center

        (91, 87): ALIVE, (90, 86): ALIVE, (89, 85): ALIVE, (88, 84): ALIVE,
        (87, 83): ALIVE, (86, 82): ALIVE, (85, 81): ALIVE, (84, 80): ALIVE,
        (83, 79): ALIVE, (82, 78): ALIVE, (81, 77): ALIVE, (80, 76): ALIVE,
        (79, 75): ALIVE, (78, 74): ALIVE, (77, 73): ALIVE, (76, 72): ALIVE,
        (75, 71): ALIVE,

        # Diagonal down center

        (87, 91): ALIVE, (86, 90): ALIVE, (85, 89): ALIVE, (84, 88): ALIVE,
        (83, 87): ALIVE, (82, 86): ALIVE, (81, 85): ALIVE, (80, 84): ALIVE,
        (79, 83): ALIVE, (78, 82): ALIVE, (77, 81): ALIVE, (76, 80): ALIVE,
        (75, 79): ALIVE, (74, 78): ALIVE, (73, 77): ALIVE, (72, 76): ALIVE,
        (71, 75): ALIVE, (70, 74): ALIVE, (69, 73): ALIVE,

        # Down left
        # Diagonal center
        (13, 13): ALIVE, (14, 14): ALIVE, (15, 15): ALIVE, (16, 16): ALIVE,
        (17, 17): ALIVE, (18, 18): ALIVE, (19, 19): ALIVE, (20, 20): ALIVE,
        (21, 21): ALIVE, (22, 22): ALIVE, (23, 23): ALIVE, (24, 24): ALIVE,
        (25, 25): ALIVE, (26, 26): ALIVE, (27, 27): ALIVE,

        # Diagonal up center

        (9, 13): ALIVE, (10, 14): ALIVE, (11, 15): ALIVE, (12, 16): ALIVE,
        (13, 17): ALIVE, (14, 18): ALIVE, (15, 19): ALIVE, (16, 20): ALIVE,
        (17, 21): ALIVE, (18, 22): ALIVE, (19, 23): ALIVE, (20, 24): ALIVE,
        (21, 25): ALIVE, (22, 26): ALIVE, (23, 27): ALIVE, (24, 28): ALIVE,
        (25, 29): ALIVE,

        # Diagonal down center

        (13, 9): ALIVE, (14, 10): ALIVE, (15, 11): ALIVE, (16, 12): ALIVE,
        (17, 13): ALIVE, (18, 14): ALIVE, (19, 15): ALIVE, (20, 16): ALIVE,
        (21, 17): ALIVE, (22, 18): ALIVE, (23, 19): ALIVE, (24, 20): ALIVE,
        (25, 21): ALIVE, (26, 22): ALIVE, (27, 23): ALIVE, (28, 24): ALIVE,
        (29, 25): ALIVE, (30, 26): ALIVE, (31, 27): ALIVE,

        # Down right
        # Diagonal center
        (87, 13): ALIVE, (86, 14): ALIVE, (85, 15): ALIVE, (84, 16): ALIVE,
        (83, 17): ALIVE, (82, 18): ALIVE, (81, 19): ALIVE, (80, 20): ALIVE,
        (79, 21): ALIVE, (78, 22): ALIVE, (77, 23): ALIVE, (76, 24): ALIVE,
        (75, 25): ALIVE, (74, 26): ALIVE, (73, 27): ALIVE,

        # Diagonal up center

        (91, 13): ALIVE, (90, 14): ALIVE, (89, 15): ALIVE, (88, 16): ALIVE,
        (87, 17): ALIVE, (86, 18): ALIVE, (85, 19): ALIVE, (84, 20): ALIVE,
        (83, 21): ALIVE, (82, 22): ALIVE, (81, 23): ALIVE, (80, 24): ALIVE,
        (79, 25): ALIVE, (78, 26): ALIVE, (77, 27): ALIVE, (76, 28): ALIVE,
        (75, 29): ALIVE,

        # Diagonal down center

        (87, 9): ALIVE, (86, 10): ALIVE, (85, 11): ALIVE, (84, 12): ALIVE,
        (83, 13): ALIVE, (82, 14): ALIVE, (81, 15): ALIVE, (80, 16): ALIVE,
        (79, 17): ALIVE, (78, 18): ALIVE, (77, 19): ALIVE, (76, 20): ALIVE,
        (75, 21): ALIVE, (74, 22): ALIVE, (73, 23): ALIVE, (72, 24): ALIVE,
        (71, 25): ALIVE, (70, 26): ALIVE, (69, 27): ALIVE,

        # Centers
        # Down left
        (29, 30): ALIVE, (30, 30): ALIVE, (31, 30): ALIVE,

        # Down Right
        (69, 30): ALIVE, (70, 30): ALIVE, (71, 30): ALIVE,

        # Up left
        (29, 70): ALIVE, (30, 70): ALIVE, (31, 70): ALIVE,

        # Up Right
        (69, 70): ALIVE, (70, 70): ALIVE, (71, 70): ALIVE,

        # Around Centers
        # Down left
        (28, 27): ALIVE, (32, 27): ALIVE,
        (28, 29): ALIVE, (32, 29): ALIVE,
        (28, 31): ALIVE, (32, 31): ALIVE,
        (28, 33): ALIVE, (32, 33): ALIVE,
        (30, 28): ALIVE, (32, 32): ALIVE,
        (26, 30): ALIVE, (34, 30): ALIVE,

        # Down Right
        (68, 27): ALIVE, (72, 27): ALIVE,
        (68, 29): ALIVE, (72, 29): ALIVE,
        (68, 31): ALIVE, (72, 31): ALIVE,
        (68, 33): ALIVE, (72, 33): ALIVE,
        (70, 28): ALIVE, (72, 32): ALIVE,
        (66, 30): ALIVE, (74, 30): ALIVE,

        # Up left
        (28, 67): ALIVE, (32, 67): ALIVE,
        (28, 69): ALIVE, (32, 69): ALIVE,
        (28, 71): ALIVE, (32, 71): ALIVE,
        (28, 73): ALIVE, (32, 73): ALIVE,
        (30, 68): ALIVE, (32, 72): ALIVE,
        (26, 70): ALIVE, (34, 70): ALIVE,

        # Up Right
        (68, 67): ALIVE, (72, 67): ALIVE,
        (68, 69): ALIVE, (72, 69): ALIVE,
        (68, 71): ALIVE, (72, 71): ALIVE,
        (68, 73): ALIVE, (72, 73): ALIVE,
        (70, 68): ALIVE, (72, 72): ALIVE,
        (66, 70): ALIVE, (74, 70): ALIVE,
    }

    for x in range(width):
        for y in range(height):
            if (x, y) not in positions.keys():
                positions[(x, y)] = DEAD

    # Si se descomenta esta parte y se comenta lo anterior es posible
    # ver posiciones random en vez de un patrón inicial

    # positions = {}

    # for x in range(width):
    #     for y in range(height):
    #         if randint(0,10) > 8:
    #             positions[(x, y)] = ALIVE
    #         else:
    #             positions[(x, y)] = DEAD

    return positions


def get_neighbors_coords(x, y, width, height):
    l = (x - 1) % width
    r = (x + 1) % width
    a = (y - 1) % height
    b = (y + 1) % height

    return l, r, a, b
