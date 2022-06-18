import sys
from pygame import *
from pyrr import Vector3, vector, vector3
from math import sin, cos, radians
import pygame 
import numpy as np

class Camera:
    rotx, roty = (0,0)
    transX, transY, transZ = (0,0,0)
    sx, sy, sz = (1,1,1)
    zpos = 5
    rotate = move = False
    speed = 0.5
    
    def takeAc(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 4: self.zpos = max(1, self.zpos-1)
            elif event.button == 5: self.zpos += 1
            elif event.button == 1: self.rotate = True
            elif event.button == 3: self.move = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1: self.rotate = False
            elif event.button == 3: self.move = False
        elif event.type == MOUSEMOTION:
            i, j = event.rel
            if self.rotate:
                self.rotx += j
                self.roty += i
            if self.move:
                self.transX -= i
                self.transY += j
        else:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP]:
                self.zpos -=1
            if keys_pressed[pygame.K_DOWN]:
                self.zpos +=1
            if keys_pressed[pygame.K_LEFT]:
                self.transX += self.speed
            if keys_pressed[pygame.K_RIGHT]:
                self.transX -= self.speed
            if keys_pressed[pygame.K_a]:
                self.transX -= self.speed
            if keys_pressed[pygame.K_d]:
                self.transX += self.speed
            if keys_pressed[pygame.K_w]:
                self.sx *= 1.05 
                self.sy *= 1.05 
                self.sz *= 1.05 
            if keys_pressed[pygame.K_s]:
                self.sx *= 0.95 
                self.sy *= 0.95 
                self.sz *= 0.95