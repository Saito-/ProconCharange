# coding: utf-8

M = 4
N = 4
tile = [
	[1, 0, 0, 1],
	[0, 1, 1, 0],
	[0, 1, 1, 0],
	[1, 0, 0, 1],
]

dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]

opt = [[0 for j in xrange(N)] for i in xrange(M)]
flip = [[0 for j in xrange(N)] for i in xrange(M)]

from copy import deepcopy

def get(x, y):
	c = tile[x][y]
	for d in xrange(5):
		x2 = x + dx[d]
		y2 = y + dy[d]
		if 0 <= x2 and x2 < M and 0 <= y2 and y2 < N:
			c += flip[x2][y2]
	return c % 2

def calc():
	for i in xrange(1, M):
		for j in xrange(N):
			if get(i-1, j) != 0:
				flip[i][j] = 1
	for j in xrange(N):
		if get(M-1, j) != 0: return -1
	res = 0
	for i in xrange(M):
		for j in xrange(N):
			res += flip[i][j]
	return res

if __name__ == '__main__':
	res = -1
	for i in xrange(1 << N):
		for x in xrange(M):
			for y in xrange(N):
				flip[x][y] = 0
		for j in xrange(N):
			flip[0][N-j-1] = i >> j & 1
		num = calc()
		if num >= 0 and (res < 0 or res > num):
			res = num
			opt = deepcopy(flip)
	if res < 0:
		print 'IMPOSSIBLE'
	else:
		for i in xrange(M):
			for j in xrange(N):
				print opt[i][j],
			print

