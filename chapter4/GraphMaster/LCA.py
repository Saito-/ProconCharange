# coding: utf-8

'''
Lowest Common Ancestor (LCA)
'''

import math

V = 8
MAX_LOG_V = int(math.floor(math.log(V, 2)))

G = [
	[1, 2],
	[0, 3, 4],
	[0, 5],
	[1],
	[1, 6, 7],
	[2],
	[4],
	[4],
]

root = 0
parent = [[0 for j in xrange(V)] for i in xrange(MAX_LOG_V)]
depth = [0] * V

def dfs(v, p, d):
	parent[0][v] = p
	depth[v] = d
	for i in xrange(len(G[v])):
		if G[v][i] != p:
			dfs(G[v][i], v, d+1)

def init(V):
	dfs(root, -1, 0)
	for k in xrange(MAX_LOG_V-1):
		for v in xrange(V):
			if parent[k][v] < 0:
				parent[k+1][v] = -1
			else:
				parent[k+1][v] = parent[k][parent[k][v]]

def lca(u, v):
	if depth[u] > depth[v]:
		tmp = u
		u = v
		v = tmp
	for k in xrange(MAX_LOG_V):
		if (depth[v] - depth[u]) >> k & 1:
			v = parent[k][v]
	if u == v: return u
	for k in xrange(MAX_LOG_V-1, 0-1, -1):
		if parent[k][u] != parent[k][v]:
			u = parent[k][u]
			v = parent[k][v]
	return parent[0][u]

if __name__ == '__main__':
	init(V)
	print lca(4-1, 7-1)
	print lca(8-1, 6-1)
	print lca(5-1, 8-1)

