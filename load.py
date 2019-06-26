#!/usr/bin/python3

import sys
import pywavefront
from OpenGL.GLUT import *
from OpenGL.GLU  import *
from OpenGL.GL   import *
from pywavefront import visualization

mouse = None
axis  = "y"
nwin  = 'Pokemon Center'
name  = 'donut.obj'
mesh  = []

def drawPoints():
	glBegin(GL_POINTS)
	for vertex in verticies:
		glVertex3fv(vertex)
	glEnd()
	return

def drawLines():
	glBegin(GL_LINES)
	for vertex in verticies:
		glVertex3fv(vertex)
	glEnd()
	return

def draw():
	for vertex in verticies:
		glVertex3fv(vertex)
	return

def main():
	global mesh

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(1200,800)
	glutCreateWindow(nwin)

	glutMouseFunc(clickHdl)
	glutDisplayFunc(display)
	glutKeyboardFunc(keyboardHdl)
	glutPassiveMotionFunc(mouseHdl)

	glClearColor(.2,.2,.2,1.)

	glShadeModel(GL_SMOOTH)
	glEnable(GL_CULL_FACE)
	glEnable(GL_DEPTH_TEST)
#	glEnable(GL_LIGHTING)
#
	lightZeroPosition = [-20.,2.,-2.,1.]
	lightZeroColor = [.5,.5,.5,.5]
	lightSpecular = [0.4,0.4,0.4,0.4]
	lightAmbiente = [0.0,0.0,0.0,1.]

	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular)
	glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbiente)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)

#	gluPerspective(GLdouble fovy,  GLdouble aspect,  GLdouble zNear,  GLdouble zFar);

	glMatrixMode(GL_PROJECTION)
	gluPerspective(30.,1.,.1,80.)
	glMatrixMode(GL_MODELVIEW)
	gluLookAt(0,5,10,
		  0,2,0,
		  0,2,-2)

	mesh = pywavefront.Wavefront(name)

	glutMainLoop()

	return

def display():
	global incx1
	global mesh

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	visualization.draw(mesh)

	glutSwapBuffers()

	return

def clickHdl(but,state,x,y):
	global mouse

	if   but is 3:
		glTranslatef(0.0,0.0,0.4)
		glutPostRedisplay()
	elif but is 4 :
		glTranslatef(0.0,0.0,-0.4)
		glutPostRedisplay() 
	elif (mouse is None) and (state is 0) and (but is 0):
		mouse = (x,y)
	elif (state is 0) and (but is 0) :
		mouse = None

def mouseHdl(mx,my):
	global mouse,axis

	if mouse is not None:
		if   axis == 'x':
			if mouse[1] > my :
				glRotatef(-15.0,.5,0.0,0.0)
			elif mouse[1] < my:
				glRotatef(-15.0,-.5,0.0,0.0)
			glutPostRedisplay()
			mouse = (mx,my)
		elif axis == 'y':
			if mouse[0] > mx :
				glRotatef(-15.0,0.0,0.0,.5)
			elif mouse[0] < mx :
				glRotatef(-15.0,0.0,0.0,-.5)
			glutPostRedisplay()
			mouse = (mx,my)
		elif axis == 'z':
			if mouse[0] > mx :
				glRotatef(-15.0,0.0,.5,0.0)
			elif mouse[0] < mx :
				glRotatef(-15.0,0.0,-.5,0.0)
			glutPostRedisplay()
			mouse = (mx,my)

def keyboardHdl( key, x, y):
	global axis

	if ord(key) == ord('h'):  
		glLoadIdentity();
		gluLookAt(0,0,10,
		          0,0,0,
		          0,1,0)
		glutPostRedisplay()

	if ord(key) == ord('x'):
		axis = 'x'
	if ord(key) == ord('y'):
		axis = 'y'
	if ord(key) == ord('z'):
		axis = 'z'

	if ord(key) == ord('a'):  
		glTranslatef(0.2,0.0,0.0)
		glutPostRedisplay()

	if ord(key) == ord('d'): 
		glTranslatef(-0.2,0.0,0.0)
		glutPostRedisplay()

	if ord(key) == ord('w'):  
		glTranslatef(0.0,-0.2,0.0)
		glutPostRedisplay()

	if ord(key) == ord('s'):  
		glTranslatef(0.0,0.2,0.0)
		glutPostRedisplay()

	if ord(key) == ord('q'):  
		glTranslatef(0.0,0.0,0.2)
		glutPostRedisplay()
 
	if ord(key) == ord('e'):  
		glTranslatef(0.0,0.0,-0.2)
		glutPostRedisplay() 

######################################################################################################
main()
