# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:51:13 2017

@author: kanghyun
"""

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


#colors = ((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(1,1,1))




def drawCube():
    
    #vertices_list = [((0,0,0),(0,1,0),(1,1,0),(1,0,0),(0,0,1),(0,1,1),(1,1,1),(1,0,1)),
    #                 ((0,1,0),(0,2,0),(1,2,0),(1,1,0),(0,1,1),(0,2,1),(1,2,1),(1,1,1))]
    surfaces = ((0,1,2,3),(3,2,6,7),(7,6,5,4),(4,5,1,0),(1,5,6,2),(0,4,7,3))
    edges = ((0,1),(0,3),(0,4),
             (2,1),(2,3),(2,6),
             (5,1),(5,6),(5,4),
             (7,6),(7,3),(7,4))
    
    
    
    vertices_list = [((0,0,0),(1,0,0),(1,1,0),(0,1,0),
                      (0,0,1),(1,0,1),(1,1,1),(0,1,1)),
    ((0,1,0),(1,1,0),(1,2,0),(0,2,0),
     (0,1,1),(1,1,1),(1,2,1),(0,2,1)),
     ((0,0,1),(1,0,1),(1,1,1),(0,1,1),
      (0,0,2),(1,0,2),(1,1,2),(0,1,2))]
     
     
                     
    
    
    
    
    #glBegin(GL_QUADS)
    
    #glColor3f(250, 12, 1)
    #for i in range(0,2):
    #    vertices=vertices_list[i]
    #    for surface in surfaces:
    #        for vertex in surface:
    #            glVertex3fv(vertices[vertex])
    #glEnd()
    
    #glBegin(GL_LINES)
    glBegin(GL_LINES)
    
    glColor3f(100, 0, 0)
    #for i in range(0,3):
    #    vertices=vertices_list[i]
    #    for edge in edges:
    #        for vertex in edge:
    #            glVertex3fv(vertices[vertex])
    
    for i in range(0,3):
        vertices=vertices_list[i]
        print(vertices[0][1])
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[4])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[6])
        glVertex3fv(vertices[5])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[5])
        glVertex3fv(vertices[6])
        glVertex3fv(vertices[5])
        glVertex3fv(vertices[4])
        glVertex3fv(vertices[7])
        glVertex3fv(vertices[6])
        glVertex3fv(vertices[7])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[7])
        glVertex3fv(vertices[4])
        
        
        
        
                
    glEnd()
        
        
        
    
    
def myOpenGL():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawCube()
        pygame.display.flip()
        pygame.time.wait(10)
        
if __name__=='__main__':
    myOpenGL()
