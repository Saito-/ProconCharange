# coding: utf-8

import time
import random

''' Union-Find 木のクラス '''
class UnionFind:
	''' 
	コンストラクタ 
	 size: 集合の大きさ
	 負の数 -> 集合の代表値 (集合の個数)
	 正の数 -> 次の要素
	'''
	def __init__(self, size):
		self.table = [-1 for _ in xrange(size)]

	'''
	Find (集合の代表値を求める)
	 x: キー値
	'''
	def find(self, x):
		if self.table[x] < 0:
			return x
		else:
			self.table[x] = self.find(self.table[x])
			return self.table[x]

	'''
	Union (集合の併合)
	 x, y: 集合
	'''
	def union(self, x, y):
		s1 = self.find(x)
		s2 = self.find(y)
		if s1 != s2:
			if self.table[s1] <= self.table[s2]:
				self.table[s1] += self.table[s2]
				self.table[s2] = s1
			else:
				self.table[s2] += self.table[s1]
				self.table[s1] = s2
			return True
		return False
	
	'''
	部分集合と要素数
	'''
	def subsetall(self):
		a = []
		for i in xrange(len(self.table)):
			if self.table[i] < 0:
				a.append((i, -self.table[i]))
		return a

def test_union(func, data, size):
	a = time.clock()
	for x, y in data:
		func(x, y)
	print time.clock() - a

def make_grid(size):
	table = [[] for _ in xrange(size*size)]
	for x in xrange(size):
		for y in xrange(size):
			n = y * size + x
			for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
				if random.random() < 0.34:
					x1 = x + dx
					y1 = y + dy
					if 0 <= x1 < size and 0 <= y1 < size:
						n1 = y1 * size + x1
						if n1 not in table[n]:
							table[n].append(n1)
							table[n1].append(n)
	return table

def print_grid(s, size):
	for y in xrange(size):
		for x in xrange(size):
			print "%3d" % s.find(y * size + x),
		print

if __name__ == '__main__':
	for size in [1000, 2000, 4000]:
		data = [(random.randint(0, size-1), random.randint(0, size-1)) for _ in xrange(size)]
		print size
		s = UnionFind(size)
		test_union(s.union, data, size)
	
	a = make_grid(20)
	s = UnionFind(20*20)
	for x in xrange(20*20):
		for n in a[x]:
			if x < n: s.union(x, n)
	print s.subsetall()
	print_grid(s, 20)
