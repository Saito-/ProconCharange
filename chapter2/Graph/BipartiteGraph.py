# coding: utf-8

import sys

G1 = [
	[1, 2],
	[0, 2],
	[0, 1],
]

G2 = [
	[1, 3],
	[0, 2],
	[1, 3],
	[0, 2],
]

colors1 = [0, 0, 0]
colors2 = [0, 0, 0, 0]

def dfs(v, c):
	colors2[v] = c
	for i in xrange(len(G2[v])):
		if colors2[G2[v][i]] == c: return False
		if colors2[G2[v][i]] == 0 and not dfs(G2[v][i], -c): return False
	return True

if __name__ == '__main__':
	for i in xrange(len(G2)):
		if colors2[i] == 0:
			if not dfs(i, 1):
				print 'no'
				sys.exit()
	print 'yes'
