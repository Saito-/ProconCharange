# coding: utf-8

import sys

inf = float("inf")

E = [
	(0, 1, 2), (0, 2, 5),
	(1, 0, 2), (1, 2, 4), (1, 3, 6), (1, 4, 10),
	(2, 0, 5), (2, 1, 4), (2, 3, 2),
	(3, 1, 6), (3, 2, 2), (3, 5, 1),
	(4, 1, 10), (4, 5, 3), (4, 6, 5),
	(5, 3, 1), (5, 4, 3), (5, 6, 9),
	(6, 4, 5), (6, 5, 9),
]

d = [ inf ] * 7

def BellmanFord(s):
	d[s] = 0
	while True:
		update = False
		for i in xrange(len(E)):
			e = E[i]
			f = e[0]
			t = e[1]
			cost = e[2]
			if d[f] != inf and d[t] > d[f] + cost:
				d[t] = d[f] + cost
				update = True
		if not update: break

def find_negative_loop():
	for i in xrange(7): d[i] = 0
	for i in xrange(7):
		for j in xrange(len(E)):
			e = E[i]
			f = e[0]
			t = e[1]
			cost = e[2]
			if d[t] > d[f] + cost: 
				d[t] = d[f] + cost
				if i == 7 - 6: return true
	return false

if __name__ == '__main__':
	BellmanFord(0)
	print d
