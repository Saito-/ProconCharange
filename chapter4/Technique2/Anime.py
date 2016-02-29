# coding: utf-8

import math

N = 3
M = 10

MAX_LOG_N = int(math.floor(math.log(N, 2)))

s = [0, 3, 7, -1, -1, -1]
t = [3, 7, 0, -1, -1, -1]

ps = []
nxt = [[0 for j in xrange(N*2)] for i in xrange(MAX_LOG_N)]

if __name__ == '__main__':
	res = 0
	
	for i in xrange(N):
		if t[i] < s[i]: t[i] += M
		s[N + i] = s[i] + M
		t[N + i] = t[i] + M
	
	for i in xrange(N*2):
		ps.append((t[i], i))
	for i in xrange(N*2):
		ps.append((s[i], N*2+i))
	ps.sort()

	last = -1
	for i in xrange(N*4-1, 0-1, -1):
		idx = ps[i][1]
		if idx < N * 2:
			nxt[0][idx] = last
		else:
			idx -= N * 2
			if last < 0 or t[last] > t[idx]:
				last = idx
	
	for k in xrange(MAX_LOG_N - 1):
		for i in xrange(N*2):
			if nxt[k][i] < 0:
				nxt[k+1][i] = -1
			else:
				nxt[k+1][i] = nxt[k][nxt[k][i]]
	
	for i in xrange(N):
		tmp = 0
		j = i
		for k in xrange(MAX_LOG_N -1, 0-1, -1):
			j2 = nxt[k][j]
			if j2 >= 0 and t[j2] <= s[i] + M:
				j = j2
				tmp |= 1 << k
		res = max(res, tmp + 1)
	
	print res
