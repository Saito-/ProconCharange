# coding: utf-8

inf = float('inf')

dx = [-1, -1, 1, 1]
dy = [-1, 0, -1, 0]

M = 2 
N = 3
V = N * M

G = [[] for i in xrange(V)]
used = [False] * V 
match = [-1] * V


seat = [
['x', '.', 'x'],
['x', '.', 'x'],
]

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
	num = 0
	for y in xrange(M):
		for x in xrange(N):
			if seat[y][x] == '.':
				num += 1
				for k in xrange(4):
					x2 = x + dx[k]
					y2 = y + dx[y]
					in_x = 0 <= x2 and x2 < N
					in_y = 0 <= y2 and y2 < M
					if in_x and in_y:
						if seat[y2][x2] == '.':
							add_edge(x*M+y, x2*M+y2)
	print num - bipartite_matching()
