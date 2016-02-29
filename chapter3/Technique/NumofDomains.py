# coding: utf-8

'''
領域圧縮:
 その前後と変化がない行/列を削除する
 領域の個数は圧縮後も変わらない
'''

from collections import deque

W = 10
H = 10
N = 5
X1 = [1, 1, 4, 9, 10]
X2 = [6, 10, 4, 9, 10]
Y1 = [4, 8, 1, 1, 6]
Y2 = [4, 8, 10, 5, 10]

dx = [1, 0, -1,  0]
dy = [0, 1,  0, -1]

fld = [[False for j in xrange(N*6)] for i in xrange(N*6)]

def compress(x1, x2, w):
	xs = []
	for i in xrange(N):
		for d in xrange(-1, 2):
			tx1 = x1[i] + d
			tx2 = x2[i] + d
			if 1 <= tx1 and tx1 <= W:
				xs.append(tx1)
			if 1 <= tx2 and tx2 <= W:
				xs.append(tx2)
	xs = set(xs)
	xs = list(xs)
	print xs
	for i in xrange(N):
		x1[i] = xs.index(x1[i]) + 1
		x2[i] = xs.index(x2[i]) + 1
	return len(xs)

if __name__ == '__main__':
	W = compress(X1, X2, W)
	H = compress(Y1, Y2, H)

	for i in xrange(N):
		for y in xrange(Y1[i], Y2[i] + 1):
			for x in xrange(X1[i], X2[i] + 1):
				fld[y][x] = True
	ans = 0
	for y in xrange(1, H+1):
		for x in xrange(1, W+1):
			if fld[y][x]: continue
			ans += 1
			que = deque([])
			que.append((x, y))
			fld[y][x] = True
			while len(que) != 0:
				p = que.popleft()
				sx = p[0]
				sy = p[1]
				for i in xrange(4):
					tx = sx + dx[i]
					ty = sy + dy[i]
					if tx <= 0 or W < tx or ty <= 0 or H < ty: continue
					if fld[ty][tx]: continue
					que.append((tx, ty))
					fld[ty][tx] = True
	print ans
