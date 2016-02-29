# coding: utf-8

inf = float('inf')

MAX_N = 100
MAX_M = 100
MAX_V = MAX_N + MAX_M + 1

N = 3
M = 4

V = N + M + 1

X = [-3, -2, 2]
Y = [3, -2, 2]
B = [5, 6, 5]

P = [-1, 1, -2, 0]
Q = [1, 1, -2, -1]
C = [3, 4, 7, 3]

E = [
[3, 1, 1, 0],
[0, 0, 6, 0],
[0, 3, 0, 2],
]

g = [[inf for j in xrange(V)] for i in xrange(V)] 

prev = [[0 for j in xrange(V)] for i in xrange(V)]
for i in xrange(V):
	for j in xrange(V):
		prev[i][j] = i
used = [False] * V

def solve():
	for j in xrange(M):
		s = 0
		for i in xrange(N):
			c = abs(X[i] - P[j]) + abs(Y[i] - Q[j]) + 1
			g[i][N+j] = c
			if E[i][j] > 0: g[N+j][i] = -c
			s += E[i][j]
		if s > 0: g[N+M][N+j] = 0
		if s < C[j]: g[N+j][N+M] = 0
	
	for k in xrange(V):
		for i in xrange(V):
			for j in xrange(V):
				if g[i][j] > g[i][k] + g[k][j]:
					g[i][j] = g[i][k] + g[k][j]
					prev[i][j] = prev[k][j]
					if i == j and g[i][j] < 0:
						for z in xrange(V):
							used[z] = False
						v = i
						while not used[v]:
							used[v] = True
							if v != N + M and prev[i][v] != N + M:
								if v >= N:
									E[prev[i][v]][v-N] += 1
								else:
									E[v][prev[i][v]-N] -= 1
							v = prev[i][v]
						print 'SUBOPTIMAL'
						for x in xrange(N):
							for y in xrange(M):
								print E[x][y],
							print
						return
	print 'OPTIMAL'

if __name__ == '__main__':
	solve()
