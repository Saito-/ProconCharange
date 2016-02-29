# coding: utf-8

from union_find import UnionFind

if __name__ == '__main__':
	N = 100
	K = 7
	info = [
		(1, 101, 1),
		(2, 1, 2),
		(2, 2, 3),
		(2, 3, 3),
		(1, 1, 3),
		(2, 3, 1),
		(1, 5, 5),
	]

	s = UnionFind(3*N)

	ans = 0
	for i in xrange(K):
		t = info[i][0]
		x = info[i][1]-1
		y = info[i][2]-1
		if x < 0 or x >= N or y < 0 or y >= N:
			ans += 1
			continue
		rx = s.find(x)
		ry = s.find(y)
		print rx, ry
		ry1 = s.find(y+N)
		ry2 = s.find(y+2*N)
		if t == 1:
			if rx == ry1 or rx == ry2:
				ans += 1
			else:
				s.union(x, y)
				s.union(x + N, y + N)
				s.union(x+2*N, y+2*N)
		else:
			if rx == ry or rx == ry2:
				ans += 1
			else:
				s.union(x, y + N)
				s.union(x + N, y + 2 * N)
				s.union(x + 2*N, y)

	print ans

