import string
def function(x,y):
	l = len(y)
	for i in range(0,l-1):
		for j in range(i,l):
			if x(y[i],y[j]) == 1:
				a = y[i]
				y[i] = y[j]
				y[j] = a
	return y

def cmp(x,y):
	if x ==y :
		return 0
	elif x < y:
		return -1
	else :
		return 1

x = input('输入数字：')
x_list = x.split(' ')
print(function(cmp,x_list))