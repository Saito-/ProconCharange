# coding: utf-8

import math

N = 3
X = [20, 20, 40]
Y = [10, 20, 10]
R = [2, 2, 3]

def cover(x, y, r):
	S = 0
	for i in xrange(N):
		if R[i] <= r:
			dx = x - X[i]
			dy = y - Y[i]
			dr = r - R[i]
			if dx*dx + dy*dy <= dr*dr:
				S |= (1 << i)
	return S

def C(r):
	cand = [0]
	for i in xrange(N):
		for j in xrange(i):
			if R[i] < r and R[j] < r:
				x1 = X[i]
				y1 = Y[i]
				r1 = r - R[i]
				x2 = X[j]
				y2 = Y[j]
				r2 = r - R[j]
				dx = x2 - x1
				dy = y2 - y1
				a = dx*dx + dy*dy
				b = ((r1*r1 - r2*r2)/ a + 1) / 2
				d = r1 * r1 / a - b * b
				if d >= 0:
					d = math.sqrt(d)
					x3 = x1 + dx * b
					y3 = y1 + dy * b
					x4 = -dy * d
					y4 = dx * d
					ij = 1 << i | 1 << j
					cand.append(cover(x3 - x4, y3 - y4, r) | ij)
					cand.append(cover(x3 + x4, y3 + y4, r) | ij)
	for i in xrange(N):
		if R[i] <= r:
			cand.append(cover(X[i], Y[i], r) | 1 << i)
	
	for i in xrange(len(cand)):
		for j in xrange(i):
			if (cand[i] | cand[j]) == ((1 << N) - 1):
				return True
	return False

if __name__ == '__main__':
	lb = 0
	ub = 10000
	for i in xrange(100):
		mid = (lb + ub) / 2
		if C(mid): 
			ub = mid
		else:
			lb = mid
	print format(ub, '.6f')
