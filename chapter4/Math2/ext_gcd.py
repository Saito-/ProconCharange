# coding: utf-8

import sys

a = 4
b = 11

def extgcd(a, b):
	(x, lastx) = (0, 1)
	(y, lasty) = (1, 0)
	while b != 0:
		q = a / b
		(a, b) = (b, a % b)
		(x, lastx) = (lastx-q*x, x)
		(y, lasty) = (lasty-q*y, y)
	return (lastx, lasty, a)

if __name__ == '__main__':
	ans = [0, 0, 0, 0]
	nx, ny, a = extgcd(a, b)
	if nx > 0:
		ans[0] = nx
	else:
		ans[1] = -nx
	if ny > 0:
		ans[2] = ny
	else:
		ans[3] = -ny
	print ans
