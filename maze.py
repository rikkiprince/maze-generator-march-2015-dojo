from Tkinter import *
from random import randint

block = 1
free_path = -1
un_expect = 0
ox = 10
oy = 10
size = 25

def displayArray(matrix):

	for m in matrix:
		print m

def drawMaze(matrix, w):
	global block, free_path, un_expect, ox, oy, size
	for y in range(0,len(matrix)):
		row = matrix[y]
		for x in range(0,len(row)):
			colour = 'grey'
			if(row[x] == block):
				colour = 'black'
			elif(row[x] == free_path):
				colour = 'green'
			elif(row[x] == un_expect):
				colour = 'purple'
			w.create_rectangle(ox + x*size, oy + y*size, ox + (x+1)*size, oy + (y+1)*size, fill=colour)

matrix = [[randint(-1,1) for x in xrange(10)] for x in xrange(10)]

#displayArray(matrix)
def gui():
	window = Tk()

	width = (len(matrix) * size) + (2 * ox)
	height = (len(matrix[0]) * size) + (2 * oy)

	w = Canvas(window, width=width, height=height)
	w.pack()

	drawMaze(matrix, w)

	window.mainloop()
