# coding: utf-8

from pqueue import PQueue
import sys

if __name__ == '__main__':
	N = 4
	L = 25
	P = 10
	A = [10, 14, 20, 21]
	B = [10, 5, 2, 4]

	A.append(L)
	B.append(0)

	que = PQueue(order=-1)
	ans = 0
	pos = 0
	tank = P

	for i in range(N):
		d = A[i] - pos
		while tank < d:
			if que.isEmpty():
				print -1
				sys.exit()
			tank += que.pop()
			ans += 1
	
		tank -= d
		pos = A[i]
		que.push(B[i])
	
	print ans

