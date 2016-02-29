# coding: utf-8

import math

g = 10.0

N = 2
H = 10
R = 10
T = 100

y = [0] * N

def calc(T):
	if T < 0: return H
	t = math.sqrt(2 * H / g)
	k = int(T/t)
	if k % 2 == 0:
		d = T - k*t
		return H - g * d*d / 2
	else:
		d = k * t + t - T
		return H - g * d*d /2

if __name__ == '__main__':
	for i in xrange(N):
		y[i] = calc(T - i)
	y.sort()
	for i in xrange(N):
		print '%.2f' % (y[i] + 2 * R * i / 100.0),
	print
