# coding: utf-8

N = 8
P = [1, 5, 6, 7, 9, 12, 14, 17]

if __name__ == '__main__':
	if N % 2 == 1:
		P[N] = 0
		N += 1
	P.sort()

	x = 0
	for i in xrange(0, N-1, 2):
		x ^= (P[i+1] - P[i] - 1)
	if x == 0: print 'Bob will win'
	else: print 'Georgia will win'
