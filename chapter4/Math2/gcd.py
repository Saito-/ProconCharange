# coding: utf-8

import sys

P1 = (1, 11)
P2 = (5,  3)

def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

if __name__ == '__main__':
	x = abs(P2[0] - P1[0])
	y = abs(P2[1] - P1[1])

	if x == 0 and y == 0:
		print 0
		sys.exit()
	print gcd(x, y)
