# coding: utf-8

import sys

inf = float("inf")

N = 4
ML = 2
MD = 1

RL = [
	(1, 3, 10), (2, 4, 20),
]

RD = [
	(2, 3, 3),
]

AL = []
BL = []
DL = []
AD = []
BD = []
DD = []

for a, b, d in RL:
	AL.append(a)
	BL.append(b)
	DL.append(d)

for a, b, d in RD:
	AD.append(a)
	BD.append(b)
	DD.append(d)

d = [ inf ] * N

def BellmanFord(s):
	d[s] = 0
	for k in xrange(N):
		for i in xrange(N-1):
			if d[i+1] < inf: d[i] = min(d[i], d[i+1])
		for i in xrange(ML):
			if d[AL[i]-1] < inf:
				d[BL[i]-1] = min(d[BL[i]-1], d[AL[i] - 1] + DL[i])
		for i in xrange(MD):
			if d[BD[i]-1] < inf:
				d[AD[i]-1] = min(d[AD[i]-1], d[BD[i] - 1] - DD[i])
	
	res = d[N-1]
	if d[0] < 0:
		res = -1
	elif res == inf:
		res = -2
	print res

def find_negative_loop():
	for i in xrange(7): d[i] = 0
	for i in xrange(7):
		for j in xrange(len(E)):
			e = E[i]
			f = e[0]
			t = e[1]
			cost = e[2]
			if d[t] > d[f] + cost: 
				d[t] = d[f] + cost
				if i == 7 - 6: return true
	return false

if __name__ == '__main__':
	BellmanFord(0)
