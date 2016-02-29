# coding: utf-8

from numpy import log2

''' 
セグメントツリーによる Range Mean Query (RMQ)
 葉が対象とする数列を保持し,
 各親は区間 (子) の最小値を保持する
'''

inf = float('inf')

a = [5, 3, 7, 9, 6, 4, 1, 2]
n = len(a)
dat = [inf] * (2*n-1)

'''
make_RMQ(a):
 配列 a から区間木を構築する
'''
def make_SegTree(a):
	for i in xrange(n):
		dat[i+n-1] = a[i]

	m = int(log2(n)) - 1 
	while m >= 0:
		i = 2**m-1
		for j in xrange(i, i+2**m):
			dat[j] = min(dat[j*2+1], dat[j*2+2])
		m -= 1

'''
update(k, a): k 番目の値を a に変更
 親の値も更新する必要がある
'''
def update(k, a):
	k += n - 1
	dat[k] = a
	while k > 0:
		k = (k - 1) / 2
		dat[k] = min(dat[k*2+1], dat[k*2+2])
'''
query(a, b, k, l, r): 区間 [a, b) の最小値を求める
 k: 節点番号
 l, r: 節点 k が 区間 [l, r) に対応していることを表す
 そうでなければ, 子ノードについて再帰的に計算する
 query(a, b, 0, 0, n) として呼ぶ
'''
def query(a, b, k, l, r):
 	# [a, b) と [l, r] が交差しなければ inf を返す
	if a >= r or b <= l: return inf
	
 	# [a, b) が完全に [l, r) を含んでいれば, 節点 k の値を返す
	if a <= l and b >= r: return dat[k]
	
	# そうでなければ, 2つの子の最小値
	v1 = query(a, b, k*2+1, l, (l+r)/2)
	v2 = query(a, b, k*2+2, (l+r)/2, r)
	return min(v1, v2)

if __name__ == '__main__':
	make_SegTree(a)
	print query(0, 4, 0, 0, 8)
