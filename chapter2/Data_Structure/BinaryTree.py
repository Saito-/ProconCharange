# coding: utf-8

import node
''' 二分木を表すクラス '''

class BinaryTree:
	def __init__(self):
		self.root = None
	
	def search(self, x):
		return node.search(self.root, x)
	
	def insert(self, x):
		self.root = node.insert(self.root, x)

	def delete(self, x):
		self.root = node.delete(self.root, x)
	
	def traverse(self):
		for x in node.traverse(self.root):
			yield x

	def __str__(self):
		if self.root is None: return 'BinaryTree()'
		buff = 'BinaryTree('
		for x in node.traverse(self.root):
			buff += '%s, ' % x
		buff = buff.rstrip(', ')
		buff += ')'
		return buff

if __name__ == '__main__':
	import random
	tree = BinaryTree()
	data = [random.randint(0, 100) for x in range(10)]
	print data
	print tree
	for x in data: tree.insert(x)
	print tree
	for x in data:
		print 'search', x, tree.search(x)
		print 'delete', x
		tree.delete(x)
		print 'search', x, tree.search(x)
		print tree
