# coding: utf-8

MAX_WH = 200

W = 2
H = 2

mem = [[-1 for j in xrange(MAX_WH)] for i in xrange(MAX_WH)]

def grundy(w, h):
	if mem[w][h] != -1: return mem[w][h]
	
	s = set()
	for i in xrange(2, w-1):
		s.add(grundy(i, h) ^ grundy(w-i, h))
	for i in xrange(2, h-1):
		s.add(grundy(w, i) ^ grundy(w, h-i))
	
	res = 0
	while res in s: res += 1
	mem[w][h] = res
	return res

if __name__ == '__main__':
	if grundy(W, H) != 0: print 'WIN'
	else: print 'LOSE'
