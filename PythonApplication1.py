from random import randint
class MazeGen:
    #finished = false
    def __init__(self, arr):
        self.arr = arr
        starting_point = (0, 0, 'S')
        self.points = [starting_point]
        self.arr[starting_point[0]][starting_point[1]] = -1
    def update_maze(self):
        starting_point = self.points.pop()
        direction = self.random_dir(starting_point)
        self.walk(starting_point, direction)
    def random_dir(self, starting_point):
        for direction in ('N', 'E', 'S', 'W'):
            if direction == starting_point[2]:
                continue
            if self.valid_direction(starting_point, direction):
                return direction
    def valid_direction(self, point, direction):
        return self.valid_point(point, direction, 1)
    def valid_point(self, point, direction, num_steps):
        coords = [point[0], point[1]]
        if direction == 'E':
            coords[1] += 1
        elif direction == 'W':
            coords[1] -= 1
        elif direction == 'N':
            coords[0] -= 1
        elif direction == 'S':
            coords[0] += 1
        return coords[0] >= 0 and coords[1] >= 0
    def walk(self, starting_point, direction):
        steps = randint(1, 4)
        if direction == 'E':
            for i in range(steps):
                self.arr[starting_point[0]][starting_point[1] + i + 1] = -1
        elif direction == 'S':
            for i in range(steps):
                self.arr[starting_point[0] + i + 1][starting_point[1]] = -1
        elif direction == 'W':
            for i in range(steps):
                self.arr[starting_point[0]][starting_point[1] - i - 1] = -1
        elif direction == 'N':
            for i in range(steps):
                self.arr[starting_point[0] - i - 1][starting_point[1]] = -1
        self.points.append((starting_point[0], starting_point[1] + 2, direction))
n = 10
m = 10
maze = [[0 for x in range(n)] for x in range(m)]
generator = MazeGen(maze)
#while not generator.finished:
generator.update_maze()
print(generator.arr)
#maze = [0] * n
#maze = maze * m
#for i in range(m):
#    maze.append([])
#for i in range(n):
#    for j in range(m):
#        maze[n][m] = 0