# coding: utf-8

R = 3
C = 3

A = [
	[2, 2, 1],
	[3, 4, 3],
	[2, 3, 2],
]

def total(a, n):
	res = 0
	if n % 3 == 1 or n % 3 == 2:
		for i in xrange(0, n, 3):
			res += a[i]
	else:
		for i in xrange(1, n, 3):
			res += a[i]
	return res

def center(a, n):
	if n % 3 == 1:
		res = total(a, n)
		for i in xrange(1, n/2, 3):
			res -= a[i]
			res -= a[n - i - 1]
	elif n % 3 == 2:
		res = total(a, n)
		for i in xrange(0, n/2, 3):
			res -= a[i]
			res -= a[n - i - 1]
	else:
		res = 0
		for i in xrange(0, n/2, 3):
			res += a[i]
			res += a[n - i - 1]
		res -= total(a, n)
	return res

if __name__ == '__main__':
	rows = [0] * 49
	for i in xrange(R):
		rows[i] = total(A[i], C)
	
	ans = center(rows, R)
	print ans
