from maze import displayArray, drawMaze
import random
from Tkinter import *

block_size = 3
block_count = 2

class Block:
	width = block_size
	height = block_size
	grid = [[1 for x in xrange(width)] for x in xrange(height)]

	def __init__(self, starting_grid):
		self.grid = starting_grid

	def get_grid(self):
		return self.grid
	#def get_rotated(self):
	def copy(self, to, x, y):
		for gy in range(self.height):
			for gx in range(self.width):
				to[x+gx][y+gy] = self.grid[gx][gy]


pipe = Block([[1,0,1],[1,0,1],[1,0,1],])
corner = Block([[1,0,1],[1,0,0],[1,1,1],])
tiles = [pipe, corner]

def mazeGenerator():
	global block_count, block_size, tiles
	grid = [[-1 for x in xrange(block_count*block_size)] for x in xrange(block_count*block_size)]
	yield grid
	for y in range(block_count):
		for x in range(block_count):
			random.choice(tiles).copy(grid, x*block_size, y*block_size)
			yield grid

def initWindow():
	ox = 10
	oy = 10
	size = 25
	window = Tk()
	generator = mazeGenerator()
	print dir(generator)
	maze = generator.next()

	width = (len(maze) * size) + (2 * ox)
	height = (len(maze[0]) * size) + (2 * oy)

	canvas = Canvas(window, width=width, height=height)
	canvas.pack()

	drawMaze(maze, canvas)

	def update():
		drawMaze(generator.next(), canvas)
		window.after(1000, update)

	window.after(1000, update)

	window.mainloop()

initWindow()