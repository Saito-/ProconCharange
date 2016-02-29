# coding: utf-8

n = 6
A = [-45, -41, -36, -36, 26, -32]
B = [22, -27, 53, 30, -38, -54]
C = [42, 56, -37, -75, -10, -6]
D = [-16, 30, 77, -46, 62, 45]

CD = [0] * (n*n)

''' 
二分探索モジュール
 既ソート済みリスト a に対し
 bisect.bisect_left(a, x):
  a[i] >= x となるような最小の i を返す
 bisect.bisect_right(a, x):
  a[i] <= x となるような最大の i を返す
 bisect.insort_hoge(a, x) で 挿入も可能
'''
import bisect

if __name__ == '__main__':
	for i in xrange(n):
		for j in xrange(n):
			CD[i*n + j] = C[i] + D[j]
	CD.sort()

	res = 0
	for i in xrange(n):
		for j in xrange(n):
			cd = -(A[i] + B[j])
			upper = bisect.bisect_right(CD, cd)
			lower = bisect.bisect_left(CD, cd)
			res += (upper - lower)
	print res
