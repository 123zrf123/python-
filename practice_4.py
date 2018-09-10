def hanoi(x,A,B,C):
	if x == 1:
		print('%r-->%r' %(A,C))
	if x == 2:
	    print('%r-->%r  %r-->%r  %r-->%r' %(A,B,A,C,B,C))
	if x > 2:
		 return hanoi(x-1,A,C,B),hanoi(1,A,B,C),hanoi(x-1,B,A,C)


x = int(input('hanoi的起始个数：'))
A = 1
B = 2
C = 3
hanoi(x,A,B,C)