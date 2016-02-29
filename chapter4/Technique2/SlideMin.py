# coding: utf-8

n = 5
k = 3
a = [1, 3, 5, 4, 2]

b = [0] * n
deq = [0] * n

if __name__ == '__main__':
	s = 0
	t = 0

	for i in xrange(n):
		while s < t and a[deq[t-1]] >= a[i]: t -= 1
		deq[t] = i
		t += 1

		if i - k + 1 >= 0:
			b[i - k + 1] = a[deq[s]]

			if deq[s] == i - k + 1:
				s += 1

	for i in xrange(n - k + 1):
		print b[i],
	print
