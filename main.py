import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    print(p)
    return open(p, 'r').read()

def rotationMatrix(degree):
    radian = degree * np.pi / 180.0

    mat = np.array([
    ], dtype=np.float32)

    return mat

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

    ], dtype=np.float32)

    # Creating Indices

    indices = np.array(
        [

        ], dtype=np.uint32)

    vertexShader = compileShader(getFileContents(
        "triangle.vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents(
        "triangle.fragment.shader"), GL_FRAGMENT_SHADER)
    shader = glCreateProgram()


    shader = glCreateProgram()
    glAttachShader(shader, vertexShader)
    glAttachShader(shader, fragmentShader)
    glLinkProgram(shader)

    VBO = glGenBuffers(1)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, 'position')
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 6, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)
    color = glGetAttribLocation(shader, 'color')
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 6, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    glUseProgram(shader)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    


def draw(count):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # enable depth test
    glEnable(GL_DEPTH_TEST)
    # apply the depth checking function
    glDepthFunc(GL_LESS)
    # Draw Triangle

    transk = glGetUniformLocation(shader, 'transform')

    glUniformMatrix4fv(transk, 1, GL_FALSE, rotationMatrix(count))

    glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)

def main():
    init()
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if count == 360: count = 0
        draw(count)
        count += 1
        glRotate(1, 3, 1, 3)
        pygame.display.flip()
        pygame.time.wait(10)


main()
