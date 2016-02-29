# coding: utf-8

def solve(mat):
	n = len(mat)
	a = [ -1 ] * n
	res = 0
	for i in xrange(n):
		for j in xrange(n):
			if mat[i][j] == 1: a[i] = j
	
	for i in xrange(n):
		pos = -1
		for j in xrange(i, n):
			if a[j] <= i:
				pos = j
				break
		for j in xrange(pos, i, -1):
			tmp = a[j]
			a[j] = a[j-1]
			a[j-1] = tmp
			res += 1;
	return res

if __name__ == '__main__':
	m1 = [
		[1, 0],
		[1, 1],
	]
	m2 = [
		[0, 0, 1],
		[1, 0, 0],
		[0, 1, 0],
	]
	m3 = [
		[1, 1, 1, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[1, 0, 0, 0],
	]
	print solve(m1)
	print solve(m2)
	print solve(m3)
