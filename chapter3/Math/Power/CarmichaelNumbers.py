# coding: utf-8

import math

def is_prime(n):
	for i in xrange(2, int(math.sqrt(n))):
		if n % i == 0: return False
	return n != 1

def mod_pow(x, n, mod):
	res = 1
	while n > 0:
		if n & 1:
			res = res * x % mod
		x = x * x % mod
		n >> 1
	return res

def CarmichaelNumber(n):
	if is_prime(n): return False
	for x in xrange(1, n):
		pow_x = mod_pow(x, n, n)
		if pow_x != x: return False
	return True

if __name__ == '__main__':
	print CarmichaelNumber(17)
	print CarmichaelNumber(561)
	print CarmichaelNumber(4)

