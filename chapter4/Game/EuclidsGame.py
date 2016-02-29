# coding: utf-8
a = 15
b = 24

if __name__ == '__main__':
	f = True
	while True:
		if a > b:
			tmp = a
			a = b
			b = tmp
		if b % a == 0: break
		if b - a > a: break
		b -= a
		f = not f
	
	if f: print 'Stan wins'
	else: print 'Ollie wins'
