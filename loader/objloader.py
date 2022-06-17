import os
import pygame
from OpenGL.GL import *
class OBJ:

    def loadMaterial(self, filename):
        contents = {}
        mtl = None

        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'newmtl':
                mtl = contents[values[1]] = {}
            elif mtl is None:
                raise ValueError("mtl file doesn't start with newmtl stmt")
            else:
                mtl[values[0]] = list(map(float, values[1:]))
        return contents

    def init(self, filename):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.gl_list = 0
        dirname = os.path.dirname(filename)

        material = None

        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append(list(map(float, values[1:3])))
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                self.mtl = self.loadMaterial(os.path.join(dirname, values[1]))
            

    

    def generate(self):
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        # glFrontFace(GL_CW)
        for face in self.faces:
            vertices, normals, texture_coords, material = face

            mtl = self.mtl[material]
            glColor(*mtl['Kd'])

            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glEndList()

    def render(self):
        glCallList(self.gl_list)

    def free(self):
        glDeleteLists([self.gl_list])
        