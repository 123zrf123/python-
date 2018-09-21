#构建子矩阵元素和矩阵
#子矩阵：从一个矩阵当中选取某些行和某些列交叉位置所组成的新矩阵（保持行与列的相对顺序）被称为原矩阵的一个子矩阵。
from numpy import *
def sum_matrix(A,x,y):
	B = zeros((x,y))
	for i in range(x):
		for j in range(y):
			sum = 0
			for n in range(i+1):
				for m in range(j+1):
					sum =sum + A[n,m]
			B[i,j] = sum
	return B


A = mat([[1,2,3],[4,5,6],[7,8,9]])
x = len(A)
y = len(A.T)
print(sum_matrix(A,x,y))
