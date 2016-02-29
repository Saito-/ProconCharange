# coding: utf-8

n = 10
S = 15
a = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

if __name__ == '__main__':
	res = n + 1
	s = 0
	t = 0
	Sum = 0

	while True:
		while t < n and Sum < S:
			Sum += a[t]
			t += 1
		if Sum < S: break
		res = min(res, t-s)
		Sum -= a[s]
		s += 1
	
	if res > n:
		res = 0
	print res
