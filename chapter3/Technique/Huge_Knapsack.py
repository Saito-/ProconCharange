# coding: utf-8

import bisect

inf = float('inf')

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5

ps = []

if __name__ == '__main__':
	n2 = n / 2
	for i in xrange(1 << n2):
		sw = 0
		sv = 0
		for j in xrange(n2):
			if i >> j & 1:
				sw += w[j]
				sv += v[j]
		ps.append((sw, sv))
	ps.sort()
	m = 1
	for i in xrange(1, 1 << n2):
		if ps[m-1][1] < ps[i][1]:
			ps[m] = ps[i]
			m += 1
	res = 0
	for i in xrange(1 << (n - n2)):
		sw = 0
		sv = 0
		for j in xrange(n - n2):
			if i >> j & 1:
				sw += w[n2 + j]
				sv += v[n2 + j]
		if sw <= W:
			lower = bisect.bisect_left(ps, (W - sw, inf), hi=m)-1
			print ps[lower]
			tv = ps[lower][1]
			res = max(res, sv + tv)
	print res
