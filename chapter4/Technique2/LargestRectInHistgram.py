# coding: utf-8

n = 7
h = [2, 1, 4, 5, 1, 3, 3]

L = [0] * n
R = [0] * n

st = [0] * n

if __name__ == '__main__':
	t = 0
	for i in xrange(n):
		while t > 0 and h[st[t-1]] >= h[i]: t -= 1
		if t == 0:
			L[i] = 0
		else:
			L[i] = st[t-1] + 1
		st[t] = i
		t += 1
	
	t = 0
	for i in xrange(n-1, 0-1, -1):
		while t > 0 and h[st[t-1]] >= h[i]: t -= 1
		if t == 0:
			R[i] = n
		else:
			R[i] = st[t-1]
		st[t] = i
		t += 1
	
	res = 0
	for i in xrange(n):
		res = max(res, h[i] * (R[i] - L[i]))
	print res
		
