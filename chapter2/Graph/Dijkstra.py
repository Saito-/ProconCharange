# coding: utf-8

from pqueue import PQueue

inf = float("inf")

G = [
	[(0, 1, 2), (0, 2, 5)],
	[(1, 0, 2), (1, 2, 4), (1, 3, 6), (1, 4, 10)],
	[(2, 0, 5), (2, 1, 4), (2, 3, 2)],
	[(3, 1, 6), (3, 2, 2), (3, 5, 1)],
	[(4, 1, 10), (4, 5, 3), (4, 6, 5)],
	[(5, 3, 1), (5, 4, 3), (5, 6, 9)],
	[(6, 4, 5), (6, 5, 9)],
]

V = 7

d = [ inf ] * 7
prev = [ 0 ] * 7


def Dijkstra(s):
	que = PQueue([(0, s)])
	d[s] = 0

	while not que.isEmpty():
		p = que.pop()
		v = p[1]
		if d[v] < p[0]: continue
		for i in xrange(len(G[v])):
			e = G[v][i]
			t = e[1]
			cost = e[2]
			if d[t] > d[v] + cost:
				d[t] = d[v] + cost
				prev[t] = v
				que.push((d[t], t))

if __name__ == '__main__':
	Dijkstra(0)
	print d
	print prev
