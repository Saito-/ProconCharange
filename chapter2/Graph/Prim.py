# coding: utf-8

inf = float("inf")

V = 7

cost = [
	[   0, inf,   1, inf, inf, inf, inf ],
	[ inf,   0,   2, inf,  10, inf, inf ],
	[   1,   2,   0,   3, inf,   7, inf ],
	[ inf, inf,   3,   0, inf,   1,   5 ],
	[ inf,  10, inf, inf,   0,   5, inf ],
	[ inf, inf,   7,   1,   5,   0,   8 ],
	[ inf, inf, inf, inf,   5,   8,   0 ]
]

mincost = [ inf ] * V
used = [ False ] * V

def Prim():
	mincost[0] = 0
	res = 0

	while True:
		v = -1
		for u in xrange(V):
			if not used[u] and (v == -1 or mincost[u] < mincost[v]):
				v = u

		if v == -1: break
		used[v] = True
		res += mincost[v]

		for u in xrange(V):
			mincost[u] = min(mincost[u], cost[v][u])
	
	return res

if __name__ == '__main__':
	print Prim()
