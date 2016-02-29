# coding: utf-8
'''
最小費用流問題
ポテンシャル + ダイクストラ法 (計算量 O(F|E|log|V|) or O(F|V|^2))
 辺 edge := [行き先 to, 容量 cap, コスト cost, 逆辺 rev]
 ポテンシャル h[v] := 残余グラフ上における 開始点 s から 点 v までの最短距離
'''

from pqueue import PQueue

inf = float('inf')

N = 3
K = 1
a = [1, 2, 3]
b = [3, 3, 4]
w = [2, 4, 8]

x = []
for i in xrange(N):
	x.append(a[i])
	x.append(b[i])
x.sort()
x = list(set(x))
m = len(x)

V = m + 2
G = [[] for i in xrange(V)]
h = [0] * V
dist = [inf] * V
prev_v = [0] * V
prev_e = [0] * V

def add_edge(frm, to, cap, cost):
	G[frm].append([to, cap, cost, len(G[to])])
	G[to].append([frm, 0, -cost, len(G[frm]) - 1])

def min_cost_flow(s, t, f):
	res = 0
	for i in xrange(V):
		h[i] = 0
	while f > 0:
		for i in xrange(V):
			dist[i] = inf
		dist[s] = 0
		que = PQueue([(0, s)])
		while not que.isEmpty():
			p = que.pop()
			v = p[1]
			if dist[v] < p[0]: continue
			for i in xrange(len(G[v])):
				e = G[v][i]
				to = e[0]
				cap = e[1]
				cost = e[2]
				nxt = dist[v] + cost + h[v] - h[to]
				if cap > 0 and dist[to] > nxt:
					dist[to] = nxt
					prev_v[to] = v
					prev_e[to] = i
					que.push((dist[to], to))
		if dist[t] == inf:
			return -1
		for v in xrange(V): h[v] += dist[v]

		d = f
		v = t
		while v != s:
			d = min(d, G[prev_v[v]][prev_e[v]][1])
			v = prev_v[v]
		f -= d
		res += d * h[t]
		v = t
		while v != s:
			e = G[prev_v[v]][prev_e[v]]
			G[prev_v[v]][prev_e[v]][1] -= d
			G[v][e[3]][1] += d
			v = prev_v[v]
	return res

if __name__ == '__main__':
	s = m
	t = s + 1
	res = 0
	add_edge(s, 0, K, 0)
	add_edge(m-1, t, K, 0)
	for i in xrange(m-1):
		add_edge(i, i+1, inf, 0)
	for i in xrange(N):
		u = x.index(a[i])
		v = x.index(b[i])
		add_edge(v, u, 1, w[i])
		add_edge(s, v, 1, 0)
		add_edge(u, t, 1, 0)
		res -= w[i]
	
	res += min_cost_flow(s, t, K+N)
	print -res
