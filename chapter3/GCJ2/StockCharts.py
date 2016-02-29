# coding: utf-8

inf = float('inf')

N = 5 
K = 2
V = N * 2
P = [
[1, 1],
[2, 2],
[5, 4],
[4, 4],
[4, 1],
]

G = [[] for i in xrange(V)]
used = [False] * V 
match = [-1] * V

'''
frm から to への辺を追加する
'''
def add_edge(frm, to):
	G[frm].append(to)
	G[to].append(frm)

'''
増加パスを DFS で探す
'''
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

'''
二部グラフの最大マッチングを求める
'''
def bipartite_matching():
	res = 0
	for i in xrange(V): match[i] = -1
	for v in xrange(V):
		if match[v] < 0:
			for i in xrange(V): used[i] = False
			if dfs(v): res += 1
	return res

if __name__ == '__main__':
	for i in xrange(N):
		for j in xrange(N):
			if i == j: continue
			f = True
			for k in xrange(K):
				if P[j][k] >= P[i][k]: f = False
			if f:
				add_edge(i, N + j)
	
	print N - bipartite_matching()
