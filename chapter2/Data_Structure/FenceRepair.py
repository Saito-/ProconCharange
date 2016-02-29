# coding: utf-8

from pqueue import PQueue

if __name__ == '__main__':
	N = 3
	L = [8, 5, 8]

	que = PQueue(L)
	ans = 0

	while len(que.buff) > 1:
		l1 = que.pop()
		l2 = que.pop()
		ans += (l1 + l2)
		que.push(l1 + l2)
	
	print ans
