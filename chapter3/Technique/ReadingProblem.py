# coding: utf-8

P = 5
a = [1, 8, 8, 8, 1]

if __name__ == '__main__':
	All = set(a)
	n = len(All)

	s = 0
	t = 0
	num = 0
	count = {}
	res = P

	for key in All:
		count[key] = 0
	while True:
		while t < P and num < n:
			if count[a[t]] == 0: num += 1
			count[a[t]] += 1
			t += 1
		if num < n: break
		res = min(res, t-s)
		if count[a[s]] - 1 == 0: num -= 1
		count[a[s]] -= 1
		s += 1
	
	print res

