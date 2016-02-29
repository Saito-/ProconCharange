# coding: utf-8

from pqueue import PQueue

inf = float("inf")

G = [
	[(0, 1, 100)],
	[(1, 0, 100), (1, 2, 250), (1, 3, 200)],
	[(2, 1, 250), (2, 3, 100)],
	[(3, 1, 200), (3, 2, 100)],
]

V = 4

dist = [ inf ] * 4
dist2 = [ inf ] * 4
prev = [ 0 ] * 4


def Dijkstra(s):
	que = PQueue([(0, s)])
	dist[s] = 0
	
	while not que.isEmpty():
		p = que.pop()
		v = p[1]
		d = p[0]
		if dist2[v] < d: continue
		for i in xrange(len(G[v])):
			e = G[v][i]
			d2 = d + e[2]
			if dist[e[1]] > d2:
				tmp = dist[e[1]]
				dist[e[1]] = d2
				d2 = tmp
				que.push((dist[e[1]], e[1]))
			if dist2[e[1]] > d2 and dist[e[1]] < d2:
				dist2[e[1]] = d2
				que.push((dist2[e[1]], e[1]))

if __name__ == '__main__':
	Dijkstra(0)
	print dist2
