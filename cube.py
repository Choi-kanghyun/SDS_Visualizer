import sys

from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QOpenGLWidget, QSlider,
        QWidget)

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import cube_configure

#vertices_list = [((0.00, 0.00, 0.00),( 0.00, 0.01, 0.00),( 0.01, 0.01, 0.00),(0.01,0.00,0.00),(0.00,0.00,0.01),
#                  (0.00,0.01,0.01),(0.01,0.01,0.01),(0.01,0.00,0.01)),
#                 ((0.00,0.01,0.00),(0.00,0.02,0.00),(0.01,0.02,0.00),(0.01,0.01,0.00),(0.00,0.01,0.01),
#                  (0.00,0.02,0.01),(0.01,0.02,0.01),(0.01,0.01,0.01))]
        
#edges = (
#        (0,1),(0,3),(0,4),
#        (2,1),(2,3),(2,6),
#        (5,1),(5,4),(5,6),
#        (7,3),(7,4),(7,6)
#        )


surfaces = ((0,1,2,3),(3,2,6,7),(7,6,5,4),(4,5,1,0),(1,5,6,2),(0,4,7,3))

edges = (
        (0,1),(0,3),(0,4),
        (2,1),(2,3),(2,6),
        (5,1),(5,6),(5,4),
        (7,6),(7,3),(7,4)
        )

vertices_list = cube_configure.setVertices_list() # 1024 개의 임시 데이터 json 을 받아온다


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        
        self.cube = Cube()
        
        self.xSlider = self.createSlider()
        self.ySlider = self.createSlider()
        self.zSlider = self.createSlider()
        
        # 회전 부분, 이벤트 연결
        self.xSlider.valueChanged.connect(self.cube.setXRotation)
        self.cube.xRotationChanged.connect(self.xSlider.setValue)
        self.ySlider.valueChanged.connect(self.cube.setYRotation)
        self.cube.yRotationChanged.connect(self.ySlider.setValue)
        self.zSlider.valueChanged.connect(self.cube.setZRotation)
        self.cube.zRotationChanged.connect(self.zSlider.setValue)
        
        mainLayout = QHBoxLayout() # 수평 정렬
        mainLayout.addWidget(self.cube)
        mainLayout.addWidget(self.xSlider)
        mainLayout.addWidget(self.ySlider)
        mainLayout.addWidget(self.zSlider)
        self.setLayout(mainLayout) # 레이아웃 
        
        self.xSlider.setValue(15 * 16)
        self.ySlider.setValue(345 * 16)
        self.zSlider.setValue(0 * 16)
        
        self.setWindowTitle("3D Visualizer")
        
        
    def createSlider(self): 
        slider = QSlider(Qt.Vertical) # Vertical 모드로 슬라이드 생성
        slider.setRange(0, 360*16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15*16)
        slider.setTickPosition(QSlider.TicksRight)
        
        return slider
        
class Cube(QOpenGLWidget):
    #signal 연결
    xRotationChanged = pyqtSignal(int) 
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Cube, self).__init__(parent)
        
        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        
        self.lastPos = QPoint()
        
        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0) # 색상
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        
    def minimumSizeHint(self):
        return QSize(300, 400)
    
    def sizeHint(self):
        return QSize(600, 800)
    
    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()
            
    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()
    
    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()
            
    # initali , paint, resize GL 
    
    def initializeGL(self):
        print("initalizerGL")
        self.setClearColor(self.trolltechPurple.darker()) # color 초기화
        self.object = self.makeObject() # genList -> 그려줄 코드를 object 에 넣어준다 
        
        gl.glShadeModel(gl.GL_FLAT)
        gl.glEnable(gl.GL_DEPTH_TEST) #깊이 버퍼를 활성화
        gl.glEnable(gl.GL_CULL_FACE) #후면 제거모드 활성화
        
    def paintGL(self):
        print("paintGL")
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity() # 단위행렬로 초기화 
        
        gl.glTranslatef(-1.2, -1.2, -1.8)
        gl.glScalef(0.15, 0.15, 0.15)
        
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        gl.glCallList(self.object) # object 코드 실행
    
    def resizeGL(self, width, height):
        print("resizeGL")
        side = min(width, height)
        if side < 0: 
            return
        #gl.glViewport((width-side)//2, (height-side)//2, side, side)
        gl.glViewport(0,0,width,height)
        
        #행렬 모드를 프로젝션, 모델뷰, 텍스쳐 등으로 적용시킬때 쓰는 함수
        gl.glMatrixMode(gl.GL_PROJECTION) # 출력시 좌표 (화면에 뿌릴지 좌표)
        gl.glLoadIdentity() #GL_PROJECTION 단위행렬 초기화
        gl.glOrtho(-2.4, 2.4, -2.4, 2.4, -2, 4)  #viewport 변경 시, 왜곡현상 중재   
        
        
        gl.glMatrixMode(gl.GL_MODELVIEW) # Modelview, 실제 좌표
        
    def mousePressEvent(self, event):
        self.lastPos = event.pos() 
        
    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x() # event 움직인 x - press 시 x
        dy = event.y() - self.lastPos.y()
        
        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 4*dy)
            self.setYRotation(self.yRot + 4*dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 4*dy)
            self.setZRotation(self.zRot + 4*dx)
            
        self.lastPos = event.pos()
        
    def makeObject(self): #그려줄 코드는 여기에다가 작성 
        print("makeObj TEst")
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE) # 여기서부터 작성
        
        gl.glBegin(gl.GL_LINES)
        gl.glColor3f(0, 0, 0)
        for i in range(0,1024): #1024 번, 나중에 미들웨어에서 받아올때는 변수를 사용해서 탄력적으로 .. 6.30
            vertices=vertices_list[i]
            for edge in edges:
                for vertex in edge:
                    gl.glVertex3fv(vertices[vertex]) #면을 만들 꼭지점 4개를 넘겨준다     
                    # 텍스트 표시 ! , 하드코딩 #
                    
                        
        gl.glEnd()
        
        gl.glBegin(gl.GL_QUADS)
        
        self.setColors("yellowgreen") # 기본 색상 - Plane 1
   
        for i in range(0,1024): # 1024 기준, 나중에 직접 데이터 받을때에는 count 등으로 설
            if i == 256: # 1024 기준, Tier 별 색상 구
                self.setColors("skyblue")
            elif i == 512:
                self.setColors("red")
            elif i == 768:
                self.setColors("gray")
                
            vertices=vertices_list[i]
            for surface in surfaces:
                for vertex in surface:
                    gl.glVertex3fv(vertices[vertex]) #면을 만들 꼭지점 4개를 넘겨준
        gl.glEnd()
        
        gl.glEndList()
        
        return genList
    
    
    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def setClearColor(self, c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())
        
        
    def setColors(self, color):
        if color=="red":
            gl.glColor3f(125, 0, 0)
        elif color=="green":
            gl.glColor3f(0,125,0)
        elif color=="blue":
            gl.glColor3f(0,0,125)
        elif color=="white":
            gl.glColor3f(0,0,0)
        elif color=="black":
            gl.glColor3f(255,255,255)
        elif color=="gray":
            gl.glColor3f(213,213,213)
        elif color=="yellow":
            gl.glColor3f(250,237,125)
        elif color=="skyblue":
            gl.glColor3f(178,235,244)
        elif color=="yellowgreen":
            gl.glColor3f(183,240,177)
            
    
    
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

        