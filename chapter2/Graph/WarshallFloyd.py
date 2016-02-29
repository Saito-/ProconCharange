# coding: utf-8

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

d = [
	[   0,   2,   5, inf, inf, inf, inf ],
	[   2,   0,   4,   6,  10, inf, inf ],
	[   5,   4,   0,   2, inf, inf, inf ],
	[ inf,   6,   2,   0, inf,   1, inf ],
	[ inf,  10, inf, inf,   0,   3,   5 ],
	[ inf, inf, inf,   1,   3,   0,   9 ],
	[ inf, inf, inf, inf,   5,   9,   0 ]
]

def WarshallFloyd():
	for k in xrange(V):
		for i in xrange(V):
			for j in xrange(V):
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])

if __name__ == '__main__':
	WarshallFloyd()
	for line in d:
		for cost in line:
			print '%3d' % cost,
		print
