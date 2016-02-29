# coding: utf-8

from union_find import UnionFind

inf = float("inf")

N = 5
M = 4
V = N + M

R = [
	(4, 3, 6831), (1, 3, 4583), (0, 0, 6592), (0, 1, 3063), 
	(3, 3, 4975), (1, 3, 2049), (4, 2, 2104), (2, 2,  781), 
]

E = len(R)
es = []

for x, y, d in R:
	es.append((x, y+N, -d))

def Kruskal():
	edges = sorted(es, key=lambda es: es[2])
	s = UnionFind(V)
	res = 0
	for i in xrange(E):
		e = edges[i]
		u = e[0]
		v = e[1]
		if not s.same(u, v):
			s.union(u, v)
			res += e[2]
	return res

if __name__ == '__main__':
	print 10000 * V + Kruskal()

