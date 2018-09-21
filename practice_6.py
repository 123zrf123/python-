#螺旋矩阵
from numpy import *
m = mat([[1,2,3],[4,5,6],[7,8,9]])
k = 0
i = len(m)
j = len(m.T)
print(i)
print(j)
n = []
x = 0
y = 0
while x < i:
	formal_x = x
	formal_y = y
	if i == 1:
		for y in range(formal_y,j):
			n.append(m[x,y])
		x = x + 1
	else:


		for y in range(formal_y,j):
			n.append(m[x,y])
		for x in range(x+1,i):
			n.append(m[x,y])
		for y in range(y-1,formal_y-1,-1):
			n.append(m[x,y])
		for x in range(x-1,formal_x,-1):
			n.append(m[x,y])

		y = y + 1
		i = i - 1
		j = j - 1

print(n)

		


