# coding: utf-8

N = 2
S = [8*60, 8*60 + 15]
T = [9*60, 9*60]
D = [30, 20]

V = N * 2
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
	for i in xrange(N):
		for j in xrange(i):
			if min(S[i] + D[i], S[j] + D[j]) > max(S[i], S[j]):
				add_edge(i, N+j)
				add_edge(j, N+i)
			if min(S[i] + D[i], T[j]) > max(S[i], T[j] - D[j]):
				add_edge(i, j)
				add_edge(N+j, N+i)
			if min(T[i], S[j] + D[j]) > max(T[i] - D[i], S[j]):
				add_edge(N+i, N+j)
				add_edge(j, i)
			if min(T[i], T[j]) > max(T[i] - D[i], T[j] - D[j]):
				add_edge(N+i, j)
				add_edge(N+j, i)
	scc()

	for i in xrange(N):
		if comp[i] == comp[N+i]:
			print 'NO'
			return
	
	print 'YES'
	for i in xrange(N):
		if comp[i] > comp[N+i]:
			s = ''
			s += format(S[i] / 60, '02d')
			s += ':'
			s += format(S[i] % 60, '02d')
			s += ' '
			s += format((S[i] + D[i])/60, '02d')
			s += ':'
			s += format((S[i] + D[i]) % 60, '02d')
			print s
		else:
			s = ''
			s += format((T[i] - D[i]) / 60, '02d')
			s += ':'
			s += format((T[i] - D[i]) % 60, '02d')
			s += ' '
			s += format(T[i]/60, '02d')
			s += ':'
			s += format(T[i] % 60, '02d')
			print s

if __name__ == '__main__':
	solve()
