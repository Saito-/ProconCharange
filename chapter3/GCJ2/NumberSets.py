# coding: utf-8

from union_find import UnionFind

A = 10
B = 20
P = 3

n = 10000000
prime = [0] * n
is_prime = [ True ]*(n+1)

def Furui(n):
	p = 0
	is_prime[0] = False
	is_prime[1] = False
	for i in xrange(2, n+1):
		if is_prime[i]:
			prime[p] = i
			p += 1
			for j in xrange(2*i, n+1, i):
				is_prime[j] = False
	return p

p = Furui(n)

if __name__ == '__main__':
	l = B - A + 1
	U = UnionFind(l)

	for i in xrange(p):
		if prime[i] >= P:
			start = (A + prime[i] - 1) / prime[i] * prime[i]
			end = B / prime[i] * prime[i]
			for j in xrange(start, end+1, prime[i]):
				U.union(start-A, j-A)
	res = 0
	for i in xrange(A, B+1):
		if (U.find(i-A) == i-A): res += 1
	print res
