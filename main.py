import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
# import os

def init():
    global vao, vbo, ebo, shader
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glViewport(0, 0, 500, 500)


    vertices = np.array([
        [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0],  # 0
        [0.5, -0.5, 0.5, 0.0, 1.0, 0.0],  # 1
        [0.5, 0.5, 0.5, 0.0, 0.0, 1.0],  # 2
        [-0.5, 0.5, 0.5, 1.0, 1.0, 1.0],  # 3

        [-0.5, -0.5, -0.5, 1.0, 0.0, 0.0],  # 4
        [0.5, -0.5, -0.5, 0.0, 1.0, 0.0],  # 5
        [0.5, 0.5, -0.5, 0.0, 0.0, 1.0],  # 6
        [-0.5, 0.5, -0.5, 1.0, 1.0, 1.0]  # 7

    ], dtype=np.float32)

    # Creating Indices

    indices = np.array(
        [
            0, 1, 2,
            2, 3, 0,
            #
            4, 5, 6,
            6, 7, 4,

            6, 2, 5,
            2, 1, 5,

            3, 2, 6,
            6, 7, 3,

            7, 3, 4,
            4, 0, 3,

        ], dtype=np.uint32)
        
def main():
    init()
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if count == 360: count = 0
        # draw(count)
        count += 1
        glRotate(1, 3, 1, 3)
        pygame.display.flip()
        pygame.time.wait(10)


main()
