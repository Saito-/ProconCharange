# coding: utf-8

import math

a = 22
b = 37

is_prime = [True] * (b-a)
is_prime_small = [True] * int(math.sqrt(b))

def Interval_Furui(a, b):
	for i in xrange(2, int(math.sqrt(b))):
		if is_prime_small[i]:
			for j in xrange(2*i, int(math.sqrt(b)), i):
				is_prime_small[j] = False
			s = max(2, (a + i - 1)/i) * i
			for j in xrange(s, b, i):
				is_prime[j - a] = False

if __name__ == '__main__':
	Interval_Furui(a, b)
	p = 0
	for i in is_prime:
		if i: p += 1
	print p
