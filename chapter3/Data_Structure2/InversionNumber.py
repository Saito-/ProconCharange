# coding: utf-8

'''
Binary Indexed Tree (BIT)
'''

n = 4
bit = [0] * (n + 1) 

'''
Sum(i):
 a1 + a2 + ... + ai を計算する
'''
def Sum(i):
	s = 0
	while i > 0:
		s += bit[i]
		i -= i & -i
	return s

'''
Add(i, x):
 ai += x とする
'''
def Add(i, x):
	while i <= n:
		bit[i] += x
		i += i & -i

if __name__ == '__main__':
	a = [4, 3, 2, 1]
	
	ans = 0
	for j in xrange(n):
		print a[j], Sum(a[j])
		ans += j - Sum(a[j])
		Add(a[j], 1)
	print ans
