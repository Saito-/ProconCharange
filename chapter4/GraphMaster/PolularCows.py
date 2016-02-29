# coding: utf-8

N = 3
M = 3
A = [1, 2, 2]
B = [2, 1, 3]

V = N
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
	for i in xrange(M):
		add_edge(A[i] - 1, B[i] - 1)
	n = scc()

	u = 0
	num = 0
	for v in xrange(V):
		if comp[v] == n:
			u = v
			num += 1

	for v in xrange(V): used[v] = False
	rdfs(u, 0)
	for v in xrange(V):
		if not used[v]:
			num = 0
			break
	print num
