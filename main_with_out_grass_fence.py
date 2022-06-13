import sys, pygame 
from pygame.locals import * 
from pygame.constants import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
from camera import Camera 
from Loader.objloader import * 
import numpy as np 
from OpenGL.GL.shaders import * 
import os 
from PIL import * 
 

 
 
while 1: 
    clock.tick(30) 
    for e in pygame.event.get(): 
        if e.type == QUIT: 
            sys.exit() 
        cam.takeAc(e) 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
 
    glTranslate(cam.transX/20., cam.transY/20., - cam.zpos) 
    glRotate(cam.rotx, 1, 0, 0) 
    glRotate(cam.rotx, 0, 1, 0) 
    glScale(cam.sx, cam.sy, cam.sz) 
    obj.render() 
 
    pygame.display.flip()