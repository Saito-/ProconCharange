# coding: utf-8

from union_find import UnionFind

inf = float("inf")

es = [
	(0, 2, 1),
	(1, 2, 2), (1, 4, 10),
	(2, 0, 1), (2, 1, 2), (2, 3, 3), (2, 5, 7),
	(3, 2, 3), (3, 5, 1), (3, 6, 5),
	(4, 1, 10), (4, 5, 5),
	(5, 2, 7), (5, 3, 1), (5, 4, 5), (5, 6, 8),
	(6, 4, 5), (6, 5, 8),
]

V = 7
E = len(es)

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
	print Kruskal()
