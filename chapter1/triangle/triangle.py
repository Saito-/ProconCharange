import sys
f = open(sys.argv[1], 'r')
line = f.readline()[:-1]
n = int(line.split(' ')[2])
line = f.readline()[:-1]
line = line[5:-1]
a = []
for num in line.split(', '):
	a.append(int(num))

f.close()
a.reverse()
ans = 0
edges = (0, 0, 0)
for i in range(n):
	edge1 = a[i]
	for j in range(i+1, n):
		edge2 = a[j]
		for k in range(j+1, n):
			edge3 = a[k]
			if edge1 < (edge2 + edge3):
				perim = edge1 + edge2 + edge3
				if perim > ans:
					ans = perim
					edges = edge1, edge2, edge3
if ans == 0:
	print '0 (Cannot make a triangle)'
else:
	print ans, edges
