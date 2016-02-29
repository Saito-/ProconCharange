# coding: utf-8

'''
Binary Indexed Tree (BIT)
'''

n = 8
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
	a = [-1, 5, 3, 7, 9, 6, 4, 1, 2]
	
	for i in xrange(1, n+1):
		Add(i, a[i])
	print bit
	for i in xrange(1, n+1):
		print Sum(i)
