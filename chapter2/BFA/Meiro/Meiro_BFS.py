import sys
from collections import deque

f = open(sys.argv[1]);
line = f.readline()[:-1]
N, M = line.split(',')
N = int(N[2:])
M = int(M[2:])

maze = []
for i in range(N):
	maze.append(f.readline()[:-1])

f.close()

for i in range(N):
	s = maze[i].find("S")
	g = maze[i].find("G")
	if s != -1:
		start = (i, s)
	if g != -1:
		goal = (i, g)

queue = deque([start])

dist = []
for i in range(N):
	row = []
	for j in range(M):
		row.append(float("inf"))
	dist.append(row)

dist[start[0]][start[1]] = 0

towards = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while len(queue) > 0:
	pos = queue.popleft()
	if pos == goal:
		break
	for move in towards:
		nx = pos[0] + move[0]
		ny = pos[1] + move[1]
		in_x = nx >= 0 and nx < N
		in_y = ny >= 0 and ny < M
		if in_x and in_y and maze[nx][ny] != '#' and dist[nx][ny] == float("inf"):
			queue.append((nx, ny))
			dist[nx][ny] = dist[pos[0]][pos[1]] + 1

print dist[goal[0]][goal[1]]
