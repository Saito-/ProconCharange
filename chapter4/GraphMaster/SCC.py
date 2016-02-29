# coding: utf-8

'''
強連結成分 (Strongly Connected Component)
 グラフは隣接リスト表現 　
'''

V = 12
G = [[] for v in xrange(V)] 
rG = [[] for v in xrange(V)]
vs = []
used = [False] * V
comp = [-1] * V

def add_edge(frm, to):
	G[frm].append(to)
	rG[to].append(frm)

def dfs(v):
	used[v] = True
	for i in xrange(len(G[v])):
		if not used[G[v][i]]: dfs(G[v][i])
	vs.append(v)

def rdfs(v, k):
	used[v] = True
	comp[v] = k
	for i in xrange(len(rG[v])):
		if not used[rG[v][i]]: rdfs(rG[v][i], k)

def scc():
	for v in xrange(V): used[v] = False
	for v in xrange(V):
		if not used[v]: dfs(v)
	for v in xrange(V): used[v] = False
	k = 0
	for i in xrange(len(vs)-1, 0-1, -1):
		if not used[vs[i]]: 
			rdfs(vs[i], k+1)
			k += 1
	return k

if __name__ == '__main__':
	add_edge(1, 2)
	add_edge(2, 1)
	add_edge(3, 0)
	add_edge(4, 6)
	add_edge(5, 2)
	add_edge(5, 3)
	add_edge(5, 4)
	add_edge(6, 5)
	add_edge(7, 9)
	add_edge(8, 7)
	add_edge(8, 6)
	add_edge(9, 8)
	add_edge(10, 7)
	add_edge(10, 9)
	add_edge(11, 10)
	print scc()
