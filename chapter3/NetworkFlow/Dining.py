# coding: utf-8

'''
最大流問題 (Ford-Fulkerson)
隣接リストによる表現
 edge := [行き先, 容量, 逆辺]
'''

inf = float('inf')

N = 4 
F = 3
D = 3

likeF = [
[True, True, False],
[False, True, True],
[True, False, True],
[True, False, True],
]

likeD = [
[True, False, True],
[True, True, False],
[True, True, False],
[False, False, True],
]

V = N * 2 + F + D + 2

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
	s = N * 2 + F + D
	t = s + 1

	for i in xrange(F):
		add_edge(s, N*2+i, 1)
	for i in xrange(D):
		add_edge(N*2+F+i, t, 1)
	for i in xrange(N):
		add_edge(i, N+i, 1)

		for j in xrange(F):
			if likeF[i][j]: add_edge(N*2+j, i, 1)
		for j in xrange(D):
			if likeD[i][j]: add_edge(N+i, N*2+F+j, 1)
	print max_flow(s, t)
