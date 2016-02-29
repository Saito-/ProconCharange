# coding: utf-8

import math

def is_prime(n):
	for i in xrange(2, int(math.sqrt(n))):
		if n % i == 0: return False
	return n != 1

def divisors(n):
	res = []
	for i in xrange(1, int(math.sqrt(n))):
		if (n % i) == 0:
			res.append(i)
			if i != n/i: res.append(n/i)
	return res

def prime_factor(n):
	primes = {}
	for i in xrange(2, int(math.sqrt(n))):
		while n % i == 0:
			primes[i] = 1
			n /= i
	
	if n != 1: primes[n] = 1
	return primes

if __name__ == '__main__':
	print is_prime(53)
	print is_prime(295927)
	print divisors(295927)
	print prime_factor(295927)
