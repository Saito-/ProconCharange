import sys

f = open(sys.argv[1], "r")
line = f.readline()[:-1]
L = int(line[4:])
line = f.readline()[:-1]
n = int(line[4:])
line = f.readline()[5:-2]
f.close()

x = []
for num in line.split(', '):
	x.append(int(num))

ans = 0
for i in range(n):
	ans = max(ans, min(x[i], L - x[i]))
print 'min = ', ans

ans = 0
for i in range(n):
	ans = max(ans, max(x[i], L-x[i]))
print 'max = ', ans

