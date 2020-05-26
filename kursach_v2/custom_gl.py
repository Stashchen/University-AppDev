from PyQt5.QtWidgets import QOpenGLWidget

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutSolidCube


def custom_map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


class CustomGL(QOpenGLWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)

    def initializeGL(self):
        self.widget_width = self.frameGeometry().width()
        self.widget_height = self.frameGeometry().height()

        self.x_axis_rotation = 0
        self.y_axis_rotation = 0

        self.sectors = 20

        self.visual_mode = GL_TRIANGLE_STRIP
        self.current_figure = self.draw_dome

        glClearColor(0, 0, 0, 1)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(self.y_axis_rotation, 0, 1, 0)
        glRotatef(self.x_axis_rotation, 1, 0, 0)

        if self.current_figure == CustomGL.draw_dome:
            self.current_figure(self.sectors, self.visual_mode)
        else:
            self.current_figure(self.visual_mode)

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-2.0, 2.0, -2.0, 2.0, -3.0, 3.0)
        glViewport(0, 0, w, h)

    def mousePressEvent(self, event):
        self.pressed_event = event.pos()

    def mouseMoveEvent(self, event):
        self.x_axis_rotation += (360 * (float(event.y()) - float(self.pressed_event.y())) / self.widget_height)
        self.y_axis_rotation += (360 * (float(event.x()) - float(self.pressed_event.x())) / self.widget_width)

        self.pressed_event = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.pressed_event = event.pos()

    @staticmethod
    def draw_dome(a, mode):
        globe = []

        for i in range(a + 1):
            lat = custom_map(i, 0, a, 0, np.pi)  # -np.pi / 2
            globe.append([])
            for j in range(a + 1):
                lon = custom_map(j, 0, a, 0, np.pi)  # np.pi
                x = np.sin(lon) * np.cos(lat)
                y = np.sin(lon) * np.sin(lat)
                z = np.cos(lon)

                globe[i].append((x, y, z))

        for i in range(a):
            glBegin(mode)
            glColor3f(0, 1, 1)
            for j in range(a + 1):
                x, y, z = globe[i][j]
                if j % 2 == 0:
                    glColor3f(1, 0, 1)
                else:
                    glColor3f(0, 1, 1)

                glVertex3f(x, y, z)
                x, y, z = globe[i + 1][j]

                glVertex3f(x, y, z)

            glEnd()

    @staticmethod
    def draw_piramid(mode):
        glBegin(mode)
        glColor3f(1, 0, 0)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(-.5, -.5, .5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, .5)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, .5)
        glVertex3f(-.5, -.5, .5)

        glVertex3f(-.5, -.5, .5)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(.5, -.5, .5)

        glEnd()



