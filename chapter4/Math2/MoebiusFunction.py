# coding: utf-8

def mod_pow(x, n, mod):
	res = 1
	while n > 0:
		if n & 1:
			res = res * x % mod
		x = x * x % mod
		n >> 1
	return res

def moebius(n):
	res = {}
	primes = []
	
	i = 2
	while i * i <= n:
		if n % i == 0:
			primes.append(i)
			while n % i == 0: n /= i
		i += 1
	if n != 1: primes.append(n)
	
	m = len(primes)
	for i in xrange(1 << m):
		mu = 1
		d = 1
		for j in xrange(m):
			if i >> j & 1:
				mu *= -1
				d *= primes[j]
		res[d] = mu
	return res

MOD = 10009
n = 2

if __name__ == '__main__':
	res = 0
	mu = moebius(n)
	for key, val in mu.iteritems():
		res += val * mod_pow(26, n / key, MOD)
		res = (res % MOD + MOD) % MOD
	print res
