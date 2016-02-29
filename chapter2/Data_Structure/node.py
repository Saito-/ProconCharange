# coding: utf-8

''' 二分探索木における節点を表すクラス '''
class Node:
	'''       
	コンストラクタ        
	 data:  格納されているデータ 
	 left:  左の子               
	 right: 右の子               
	'''
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
	

'''
二分探索
 node: 探索点
 x:    キー値
'''
def search(node, x):
	while node:
		if node.data == x: return True
		if x < node.data:
			node = node.left
		else:
			node = node.right
	return False

'''
データの挿入
 node: 挿入点
 x:    挿入値
'''
def insert(node, x):
	if node is None: return Node(x)
	elif x == node.data: return node
	elif x < node.data:
		node.left = insert(node.left, x)
	else:
		node.right = insert(node.right, x)
	return node

'''
最小値の探索
 node: 探索点
'''
def search_min(node):
	if node.left is None: return node.data
	return search_min(node.left)

'''
最小値の削除
 node: 探索点
'''
def delete_min(node):
	if node.left is None: return node.right
	node.left = delete_min(node.left)
	return node

'''
節点の削除
 node: 探索点
 x:    削除値
'''
def delete(node, x):
	if node:
		if x == node.data:
			if node.left is None:
				return node.right
			elif node.right is None:
				return node.left
			else:
				node.data = search_min(node.right)
				node.right = delete_min(node.right)
		elif x < node.data:
			node.left = delete(node.left, x)
		else:
			node.right = delete(node.right, x)
	return node

'''
巡回
 node: 巡回点
'''
def traverse(node):
	if node:
		for x in traverse(node.left):
			yield x
		yield node.data
		for x in traverse(node.right):
			yield x
