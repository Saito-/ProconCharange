# coding: utf-8

N = 3
x = [1, 2, 3]
y = [1, 2, 1]

G = [[False for j in xrange(N)] for i in xrange(N)]
color = [-1] * N
used = [[False for j in xrange(N)] for i in xrange(N)]

def rec(v, u):
	used[v][u] = True
	used[u][v] = True
	c = 3 - color[v] - color[u]
	for w in xrange(N):
		if G[v][w] and G[u][w]:
			if color[w] < 0:
				color[w] = c
				if not rec(v, w) or not rec(u, w):
					return False
			elif color[w] != c:
				return False
	return True

def solve():
	for i in xrange(N):
		v = [-1, -1, -1]
		for j in xrange(N):
			if x[i] < x[j]:
				k = y[j] - y[i] + 1
				if 0 <= k and k < 3 and (v[k] < 0 or x[j] < x[v[k]]):
					v[k] = j
		for k in xrange(3):
			if v[k] >= 0:
				G[i][v[k]] = True
				G[v[k]][i] = True
	res = 1

	for v in xrange(N):
		for u in xrange(N):
			if G[v][u] and not used[v][u]:
				res = max(res, 2)
				for w in xrange(N):
					if G[v][w] and G[u][w]:
						res = max(res, 3)
						for i in xrange(N): color[i] = -1
						color[v] = 0
						color[u] = 1
						if not rec(v, u):
							print 4
							return
						break

	print res

if __name__ == '__main__':
	solve()

