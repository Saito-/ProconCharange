# coding: utf-8

inf = float('inf')

V = 5

N = 3
M = 3

V = N * M + 2

cld = [
'.?.',
'.?.',
'.#.',
]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

G = [[] for i in xrange(V)]
used = [False] * V 

'''
frm から to への 容量 cap の辺を追加する
'''
def add_edge(frm, to, cap):
	G[frm].append([to, cap, len(G[to])])
	G[to].append([frm, 0, len(G[frm])-1])

'''
増加パスを DFS で探す
'''
def dfs(v, t, f):
	if v == t: return f
	used[v] = True
	for i in xrange(len(G[v])):
		e = G[v][i]
		to = e[0]
		cap = e[1]
		rev = e[2]
		if not used[to] and cap > 0:
			d = dfs(to, t, min(f, cap))
			if d > 0:
				G[v][i][1] -= d
				G[to][rev][1] += d
				return d
	return 0

def max_flow(s, t):
	flow = 0
	while True:
		for i in xrange(V): used[i] = False
		f = dfs(s, t, inf)
		if f == 0: return flow
		flow += f

if __name__ == '__main__':
	res = 0
	s = N * M
	t = s + 1
	for i in xrange(N):
		for j in xrange(M):
			if (i + j) % 2 == 0:
				if cld[i][j] == '#':
					res += 4
					add_edge(s, i*M+j, inf)
				elif cld[i][j] == '.':
					add_edge(i*M+j, t, inf)
				else:
					res += 4
					add_edge(s, i*M+j, 4)
				for k in xrange(4):
					i2 = i + dx[k]
					j2 = j + dy[k]
					if 0 <= i2 and i2 < N and 0 <= j2 and j2 < M:
						add_edge(i*M+j, i2*M+j2, 2)
			else:
				if cld[i][j] == '#':
					res += 4
					add_edge(i*M+j, t, inf)
				elif cld[i][j] == '.':
					add_edge(s, i*M+j, inf)
				else:
					res += 4
					add_edge(i*M+j, t, 4)
	res -= max_flow(s, t)
	print res

