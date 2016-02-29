# coding: utf-8
'''
 包除原理
'''

n = 100
m = 3
a = [2, 3, 7]

def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

if __name__ == '__main__':
	res = 0
	for i in xrange(1, 1 << m):
		num = 0
		j = i
		while j != 0:
			num += j & 1
			j >>= 1
		lcm = 1
		for j in xrange(m):
			if i >> j & 1:
				lcm = lcm / gcd(lcm, a[j]) * a[j]
				if lcm > n: break
		if num % 2 == 0:
			res -= n / lcm
		else:
			res += n / lcm
	print res
