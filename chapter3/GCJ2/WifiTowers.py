# coding: utf-8

'''
最大流問題 (Ford-Fulkerson)
隣接リストによる表現
 edge := [行き先, 容量, 逆辺]
'''

inf = float('inf')

n = 5
x = [0, 0, 5, 10, 15]
y = [1, -1, 1, 6, 2]
r = [7, 7, 1, 6, 2]
s = [10, 10, -15, 10, -20]

V = n + 2

G = [[] for i in xrange(V)]
used = [False] * V 

def sqr(a):
	return a*a

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
	ans = 0

	for i in xrange(n):
		if s[i] < 0:
			add_edge(n, i, -s[i])
		else:
			ans += s[i]
			add_edge(i, n+1, s[i])
		
		for j in xrange(n):
			if i == j: continue
			if sqr(x[i] - x[j]) + sqr(y[i] - y[j]) <= sqr(r[i]):
				add_edge(j, i, inf)
	
	ans -= max_flow(n, n+1)
	print ans

