import sys

f = open(sys.argv[1], "r")
N = int(f.readline()[:-1])
S = f.readline()[:-1]
T = []
f.close()
print N
print S
head = 0
tail = N-1
for i in range(N):
	s = S[head]
	t = S[tail]
	if s < t:
		T.append(s)
		head+=1
	else:
		T.append(t)
		tail-=1




