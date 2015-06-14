import sys
from Lumberjack import Lumberjack

n = int(raw_input())
logs = int(raw_input())
grid = []

for i in range(n):
	grid.append(raw_input().split())

l = Lumberjack(logs, grid)

l.print_grid()
