# coding: utf-8

from collections import deque

inf = float('inf')

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
X = 5
Y = 5
field = [
['X', 'X', 'D', 'X', 'X'],
['X', '.', '.', '.', 'X'],
['D', '.', '.', '.', 'X'],
['X', '.', '.', '.', 'D'],
['X', 'X', 'X', 'X', 'X'],
]

V = X * Y * 3 + 10
G = [[] for i in xrange(V)]
match = [-1] * V
used = [False] * V

dX = []
dY = []
pX = []
pY = []

dist =  [[[[-1 for i in xrange(Y)] for i in xrange(X)] for i in xrange(Y)] for i in xrange(X)]

def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

def dfs(v):
	used[v] = True
	for i in xrange(len(G[v])):
		u = G[v][i]
		w = match[u]
		if w < 0 or not used[w] and dfs(w):
			match[v] = u
			match[u] = v
			return True
	return False

def bfs(x, y, d):
	d[x][y] = 0
	qx = deque()
	qy = deque()
	qx.append(x)
	qy.append(y)
	while len(qx) != 0:
		x = qx.popleft()
		y = qy.popleft()
		for k in xrange(4):
			x2 = x + dx[k]
			y2 = y + dy[k]
			in_x = 0 <= x2 and x2 < X 
			in_y = 0 <= y2 and y2 < Y
			if in_x and in_y:
				is_Person = field[x2][y2] == '.'
				if is_Person and d[x2][y2] < 0:
					d[x2][y2] = d[x][y] + 1
					qx.append(x2)
					qy.append(y2)

def solve():
	n = X * Y
	for x in xrange(X):
		for y in xrange(Y):
			if field[x][y] == 'D':
				dX.append(x)
				dY.append(y)
				bfs(x, y, dist[x][y])
			elif field[x][y] == '.':
				pX.append(x)
				pY.append(y)
	d = len(dX)
	p = len(pX)
	for i in xrange(d):
		for j in xrange(p):
			tmp = dist[dX[i]][dY[i]][pX[j]][pY[j]]
			if tmp >= 0:
				for k in xrange(tmp, n+1):
					add_edge((k-1)*d+i, n*d+j)
	
	if p == 0:
		print 0
		return
	num = 0
	for i in xrange(len(match)):
		match[i] = -1
	for v in xrange(n*d):
		for i in xrange(len(used)):
			used[i] = False
			if dfs(v):
				if num+1 == p:
					print v / d + 1
					return
				num += 1
	print 'impossible'

if __name__ == '__main__':
	solve()
