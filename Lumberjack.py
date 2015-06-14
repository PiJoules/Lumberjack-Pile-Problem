
class Lumberjack():
	def __init__(self, logs, grid):
		self.logs = logs
		self.grid = grid
		self.w = len(grid)

		self.distribute_logs()

	def distribute_logs(self):
		logs = self.logs
		grid = self.grid
		w = self.w

		grid_row = []
		for y in range(w):
			for x in range(w):
				grid_row.append( int(grid[y][x]) )

		index = 0
		val = grid_row[0]
		while logs > 0:
			for i in range(1, w*w):
				if grid_row[i] < val:
					val = grid_row[i]
					index = i
			grid_row[index] += 1
			logs -= 1
			val = grid_row[0]
			index = 0

		for y in range(w):
			for x in range(w):
				self.grid[y][x] = grid_row[y*w+x]

	def print_grid(self):
		for row in self.grid:
			print row