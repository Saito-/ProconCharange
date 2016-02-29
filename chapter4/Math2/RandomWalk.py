# coding: utf-8

EPS = 1e-8

N = 10
M = 10
grid = [
 '..######.#',
 '......#..#',
 '.#.##.##.#',
 '.#........',
 '##.##.####',
 '....#....#',
 '.#######.#',
 '....#.....',
 '.####.####',
 '....#.....',
]

N = 3
M = 10
grid = [
 '.#...#...#',
 '.#.#.#.#.#',
 '...#...#..',
]

can_goal = [[False for j in xrange(M)] for i in xrange(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''
Ax = b を解く
'''
def gauss_jordan(A, b):
	n = len(A)
	B = [[0 for j in xrange(n+1)] for i in xrange(n)] 
	
	for i in xrange(n):
		for j in xrange(n):
			B[i][j] = A[i][j]
	for i in xrange(n):
		B[i][n] = b[i]
	
	for i in xrange(n):
		pivot = i
		for j in xrange(i, n):
			if abs(B[j][i]) > abs(B[pivot][i]): pivot = j
		tmp = B[i]
		B[i] = B[pivot]
		B[pivot] = tmp

		if abs(B[i][i]) < EPS: return []

		div = B[i][i]
		for j in xrange(i, n+1): 
			B[i][j] /= div
		for j in xrange(n):
			if i != j:
				mul = B[j][i]
				for k in xrange(i, n+1):
					B[j][k] -= mul * B[i][k]	

	x = [0] * n
	for i in xrange(n): x[i] = B[i][n]
	return x

def dfs(x, y):
	can_goal[x][y] = True
	for i in xrange(4):
		nx = x + dx[i]
		ny = y + dy[i]
		in_x = 0 <= nx and nx < N
		in_y = 0 <= ny and ny < M
		if in_x and in_y and not can_goal[nx][ny] and grid[nx][ny] != '#':
			dfs(nx, ny)

if __name__ == '__main__':
	A = [[0 for j in xrange(N*M)] for i in xrange(N*M)]
	b = [0] * (N*M)
	dfs(N-1, M-1)

	for x in xrange(N):
		for y in xrange(M):
			if x == N-1 and y == M-1 or not can_goal[x][y]:
				A[x*M+y][x*M+y] = 1
				continue
			move = 0
			for k in xrange(4):
				nx = x + dx[k]
				ny = y + dy[k]
				in_x = 0 <= nx and nx < N
				in_y = 0 <= ny and ny < M
				if in_x and in_y and grid[nx][ny] == '.':
					A[x*M+y][nx*M+ny] = -1
					move += 1
			b[x*M+y] = move
			A[x*M+y][x*M+y] = move
	res = gauss_jordan(A, b)
	print format(res[0], '.8f')
