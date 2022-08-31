# importing all needed modules
import pygame
from box import Box
import numpy

# initializing pygame
pygame.init()

# Permanent variables: Scale, each block size, width, height, dimensions
SIDE = 700
DIMENSIONS = (SIDE, SIDE)

BLACK = (40, 40, 40)
WHITE = (200, 200, 200)
GREEN = (40, 150, 40)
RED = (150, 40, 40)
BLUE = (40, 40, 150)


# Setting up pygame
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('2D Projections')

FRAMES = int(1000/60)

# -----------------------------------------------------------------------

UNIT = 10
PARTITIONS = 2 * UNIT
UNIT_SIZE = SIDE / PARTITIONS

AXIS_WIDTH = 4


def build_graph():
    screen.fill(BLACK)
    
    # horizontal axis and verticle axis
    pygame.draw.line(screen, WHITE, (0, SIDE/2), (SIDE, SIDE/2), width=AXIS_WIDTH)
    pygame.draw.line(screen, WHITE, (SIDE/2, 0), (SIDE/2, SIDE), width=AXIS_WIDTH)

    # unites
    for i in range(PARTITIONS):
        pygame.draw.line(screen, GREEN, (i * UNIT_SIZE, SIDE/2 - 10), (i * UNIT_SIZE, SIDE/2 + 10), width=AXIS_WIDTH)
        pygame.draw.line(screen, GREEN, (SIDE/2 - 10, i * UNIT_SIZE), (SIDE/2 + 10, i * UNIT_SIZE), width=AXIS_WIDTH)

def graph(points):
    true_points = [[UNIT_SIZE * p[0] + SIDE/2, UNIT_SIZE * p[1] + SIDE/2] for p in points]

    # connect shape using verticies
    for i in range(4):
        pygame.draw.line(screen, BLUE, true_points[i], true_points[(i+1)%4], AXIS_WIDTH)
        pygame.draw.line(screen, BLUE, true_points[i+4], true_points[(i+5)%4 + 4], AXIS_WIDTH)
        pygame.draw.line(screen, BLUE, true_points[i], true_points[i+4], AXIS_WIDTH)

    # graph verticies as points
    for point in true_points:
        pygame.draw.circle(screen, RED, point, AXIS_WIDTH)

box_verticies = 4 * numpy.array([[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1], [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]])
box = Box(20, box_verticies)

SHOW_GRID = True

# Game loop
while True:
    pygame.time.delay(FRAMES)

    if SHOW_GRID:
        build_graph()
    else:
        screen.fill(BLACK)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # key detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        box.rotate_over_y(0.05)
    if keys[pygame.K_LEFT]:
        box.rotate_over_y(-0.05)
    if keys[pygame.K_UP]:
        box.rotate_over_x(-0.05)
    if keys[pygame.K_DOWN]:
        box.rotate_over_x(0.05)
    if keys[pygame.K_SPACE]:
        box.rotate_over_z(0.05)

    graph(box.projected_verticies())
    pygame.display.update()

