# coding: utf-8

'''
最大流問題 (Ford-Fulkerson)
隣接リストによる表現
 edge := [行き先, 容量, 逆辺]
'''

inf = float('inf')

N = 3
M = 1
A = [1, 2, 10]
B = [10, 10, 3]
a = [2]
b = [3]
w = [1000]

V = N + 2

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
	s = N
	t = s + 1
	for i in xrange(N):
		add_edge(i, t, A[i])
		add_edge(s, i, B[i])
	
	for i in xrange(M):
		add_edge(a[i]-1, b[i]-1, w[i])
		add_edge(b[i]-1, a[i]-1, w[i])
	
	print max_flow(s, t)
