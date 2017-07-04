# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:59:01 2017

@author: kanghyun
"""

import pygame
import json

from cube_configure import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#표먼, 정육면체의 각 꼭지점의 번호를 0~7 이라고 정의한 후, 면 6개를 만든
surfaces = ((0,1,2,3),(3,2,6,7),(7,6,5,4),(4,5,1,0),(1,5,6,2),(0,4,7,3))

edges = (
        (0,1),(0,3),(0,4),
        (2,1),(2,3),(2,6),
        (5,1),(5,6),(5,4),
        (7,6),(7,3),(7,4)
         )

vertices_list = setVertices_list() # 임시 json 데이터를 받아 꼭지점 자동 setting


def drawCube():
    
    glBegin(GL_QUADS)
    glColor3f(50,0,0)
    
    for i in range(0,1024): # 1024 기준, 나중에 직접 데이터 받을때에는 count 등으로 설
        vertices=vertices_list[i]
        for surface in surfaces:
            for vertex in surface:
                glVertex3fv(vertices[vertex]) #면을 만들 꼭지점 4개를 넘겨준
    glEnd()
    
    
    glBegin(GL_LINES)
    glColor3f(10, 10, 10)
    
    for i in range(0,1024):
        vertices=vertices_list[i]
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
    glEnd()
    
def cube_write_main():
    pygame.init()
    display = (1000, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-3, -1, -30) # 윈도우 시점
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(5,0,1,0) #회전 (속도, x축,y축,z)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawCube()
        pygame.display.flip()
        pygame.time.wait(10)
    
if __name__=="__main__":
    cube_write_main()