#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import time
#==============================================================================

#==============================================================================
#===========================Generates The Main Canvas==========================
#==============================================================================
class GLWidget(QGLWidget):

    def __init__(self,parent=None,matrixSize=None,matrix=None):
        super(GLWidget,self).__init__()
        self.matrixSize=matrixSize
        self.matrix=matrix
        self.yellow=[1.0,1.0,0.0]
        self.blue=[0.0,0.0,1.0]
        self.red=[1.0,0.0,0.0]
        self.green=[0.0,1.0,0.0]
        self.cyan=[0.0,1.0,1.0]
        self.black=[0.0,0.0,0.0]
        self.positionEyeX=0
        self.positionEyeY=0
        self.zoom=2.0

    def initializeGL(self):
        self.qglClearColor(QColor(0,0,0))
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self,width,height):
        if(height==0):
            height=1
        glViewport(0,0,width,height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect=width/float(height)
        gluPerspective(45.0,aspect,1.0,100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslate(0.0,0.0,-50.0)
        glScale(self.zoom,self.zoom,self.zoom)
        self.drawPlayer()
        self.drawMaze()
        self.drawMeta()
        self.plane()

    def setSliderValue(self,value):
        self.zoom=value/5
        self.updateGL()

    def startSimulation(self,path):
        for index in range(len(path)):
            self.positionEyeX=(path[index][0])-1
            self.positionEyeY=(path[index][1])-1
            self.updateGL()
            time.sleep(0.20)
            print("Position: (",self.positionEyeX,",",self.positionEyeY,")")

#==============================================================================
#============================Painting Graphic Design===========================
#==============================================================================
    def plane(self):
        glDisable(GL_TEXTURE_2D)
        #======================================================================
        #=========================Drawing The Plane 2D=========================
        #======================================================================
        #Axis of the plane X===================================================
        glColor3f(self.green[0],self.green[1],self.green[2])
        glLineWidth(2)
        glBegin(GL_LINES)
        glVertex2f(self.matrixSize,0.0)
        glVertex2f(-self.matrixSize,0.0)
        glEnd()
        for i in range(-self.matrixSize,self.matrixSize+1):
            glColor3f(self.green[0],self.green[1],self.green[2])
            glBegin(GL_LINES)
            glVertex2f(-0.5,i)
            glVertex2f(0.5,i)
            glEnd()
        #Axis of the plane Y===================================================
        glColor3f(self.green[0],self.green[1],self.green[2])
        glLineWidth(2)
        glBegin(GL_LINES)
        glVertex2f(0.0,self.matrixSize)
        glVertex2f(0.0,-self.matrixSize)
        glEnd()
        for i in range(-self.matrixSize,self.matrixSize+1):
            glColor3f(self.green[0],self.green[1],self.green[2])
            glBegin(GL_LINES)
            glVertex2f(i,0.5)
            glVertex2f(i,-0.5)
            glEnd()

    def drawMaze(self):
        glDisable(GL_TEXTURE_2D)
        for row in range(self.matrixSize):
            for column in range(self.matrixSize):
                if (self.matrix[row][column]=="0"):
                    glPushMatrix()
                    glTranslatef(row*1.0,column*1.0,0.0)
                    self.drawSquareTwo()
                    glPopMatrix()
                if (self.matrix[row][column]=="1"):
                    glPushMatrix()
                    glTranslatef(row*1.0,column*1.0,0.0)
                    self.drawSquareThree()
                    glPopMatrix()
                if (self.matrix[row][column]=="C"):
                    glPushMatrix()
                    glTranslatef(row*1.0,column*1.0,0.0)
                    self.drawSquareFive()
                    glPopMatrix()

    def drawPlayer(self):
        self.loadTextures()
        glEnable(GL_TEXTURE_2D)
        for row in range(self.matrixSize):
            for column in range(self.matrixSize):
                if (self.matrix[row][column]=="S"):
                    glPushMatrix()
                    glTranslatef((row*1.5)+self.positionEyeX,(column*1.5)+self.positionEyeY,0.0)
                    self.drawSquareOne()
                    glPopMatrix()

    def drawMeta(self):
        glDisable(GL_TEXTURE_2D)
        for row in range(self.matrixSize):
            for column in range(self.matrixSize):
                if (self.matrix[row][column]=="M"):
                    glPushMatrix()
                    glTranslatef(row*1.0,column*1.0,0.0)
                    self.drawSquareFour()
                    glPopMatrix()

    def drawSquareOne(self):
        glColor3f(self.yellow[0],self.yellow[1],self.yellow[2])
        glLineWidth(1)
        glBegin(GL_QUADS)
        glTexCoord2f(1.0,1.0);glVertex2f(0.5,0.5)
        glTexCoord2f(0.0,1.0);glVertex2f(-0.5,0.5)
        glTexCoord2f(0.0,0.0);glVertex2f(-0.5,-0.5)
        glTexCoord2f(1.0,0.0);glVertex2f(0.5,-0.5)
        glEnd()

    def drawSquareTwo(self):
        glColor3f(self.blue[0],self.blue[1],self.blue[2])
        glLineWidth(1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()

    def drawSquareThree(self):
        glColor3f(self.black[0],self.black[1],self.black[2])
        glLineWidth(1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()
        glColor3f(self.blue[0],self.blue[1],self.blue[2])
        glLineWidth(1)
        glBegin(GL_QUADS)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()

    def drawSquareFour(self):
        glColor3f(self.red[0],self.red[1],self.red[2])
        glLineWidth(1)
        glBegin(GL_QUADS)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()

    def drawSquareFive(self):
        glColor3f(self.blue[0],self.blue[1],self.blue[2])
        glLineWidth(1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()
        glColor3f(self.cyan[0],self.cyan[1],self.cyan[2])
        glLineWidth(1)
        glBegin(GL_QUADS)
        glVertex2f(1.0,0.0)
        glVertex2f(1.0,1.0)
        glVertex2f(0.0,1.0)
        glVertex2f(0.0,0.0)
        glEnd()

    def loadTextures(self):
        image=Image.open("Image/PlayerOne.png")
        sizeX=image.size[0]
        sizeY=image.size[1]
        image=image.tostring("raw","RGBX",0,-1)
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, sizeX, sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
#==============================================================================