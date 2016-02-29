# coding: utf-8

n = 1000000
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

if __name__ == '__main__':
	print Furui(n)
