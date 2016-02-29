# coding: utf-8

'''
(a or not b) and (b or c) and (not c or not a) を解く
'''

V = 6
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

def solve():
	add_edge(3, 4)
	add_edge(1, 0)
	add_edge(4, 2)
	add_edge(5, 1)
	add_edge(2, 3)
	add_edge(0, 5)
	
	scc()

	for i in xrange(3):
		if comp[i] == comp[3+i]:
			print 'NO'
			return
	
	print 'YES'
	for i in xrange(3):
		if comp[i] > comp[3+i]:
			print 'true'
		else:
			print 'false'

if __name__ == '__main__':
	solve()
