# coding: utf-8

'''
上へ向かうヒープ構築
 buff: ヒープ
 n:    要素数 (探索開始点)
'''

def _upheap(buff, n, idx):
	while True:
		p = (n - 1) / 2	# 親のインデックス
		if p < 0 or buff[p] <= buff[n]: break
		temp = buff[n]
		buff[n] = buff[p]
		buff[p] = temp
		idx[buff[n]] = n
		idx[buff[p]] = p
		n = p

''' 
下へ向かうヒープ構築
 buff: ヒープ
 n:    要素数 (探索開始点)
'''
def _downheap(buff, n, idx):
	size = len(buff)
	while True:
		c = 2 * n + 1
		if c >= size: break
		if c + 1 < size:
			if buff[c] > buff[c+1]: c+=1
		if buff[n] <= buff[c]: break
		temp = buff[n]
		buff[n] = buff[c]
		buff[c] = temp
		idx[buff[c]] = c
		idx[buff[n]] = n
		n = c

''' 
プライオリティキューのクラス
'''
class PQueue:
	'''
	コンストラクタ
	 buff: ヒープ
	 order: 格納順 (1 のとき昇順, -1 のとき降順)
	'''
	def __init__(self, buff=[], order=1):
		self.order = order
		self.buff = buff[:] * order
		self.idx = {}
		for x in xrange(len(buff)):
			self.idx[buff[x]] = x
		for n in xrange(len(self.buff) / 2 - 1, -1, -1):
			_downheap(self.buff, n, self.idx)
	
	'''
	データの追加
	 data: 追加データ
	'''
	def push(self, data):
		data *= self.order
		self.buff.append(data)
		self.idx[data] = len(self.buff) - 1
		_upheap(self.buff, len(self.buff) - 1, self.idx)
	
	'''
	最小 (最大) 値の取り出し
	'''
	def pop(self):
		if len(self.buff) == 0: raise IndexError
		value = self.buff[0] * self.order
		del self.idx[value]
		last = self.buff.pop()
		if len(self.buff) > 0:
			self.buff[0] = last
			self.idx[last] = 0
			_downheap(self.buff, 0, self.idx)
		return value
	
	'''
	最小 (最大) 値の出力
	'''
	def peek(self):
		if len(self.buff) == 0: raise IndexError
		return self.buff[0]*self.order
	
	'''
	空かどうか
	'''
	def isEmpty(self): return len(self.buff) == 0

	'''
	ヒープを返す
	'''
	def content(self): return self.buff

	'''
	キー値を減算する
	'''
	def decrease_key(self, x, d):
		x.decrease_key(d)
		if d > 0:
			_upheap(self.buff, self.idx[x], self.idx)
		else:
			_downheap(self.buff, self.idx[x], self.idx)


if __name__ == '__main__':
	import random
	a = PQueue()
	for x in xrange(10):
		n = random.randint(0, 100)
		a.push(n)
		print n, 'min data =', a.peek()
	while not a.isEmpty():
		print a.pop(),
	print
	data = [random.randint(0, 100) for x in range(10)]
	print data
	a = PQueue(data)
	while not a.isEmpty():
		print a.pop(),
	print
	
