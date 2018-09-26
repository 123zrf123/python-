#高级面向对象---使类具有list的切片效果---即可以截取其中的一段
class Fib(object):
	"""docstring for Fib"""
	def __init__(self, n):
		super(Fib, self).__init__()
	
	def __getitem__(self,n):    #使其具有像列表一样能够取出元素
		if isinstance(n,int):   #判断其是否为整数型
			a,b = 1,1
			for x in rang(n):
				a,b = b,a+b
			return a

		if isinstance(n,slice): #判断其是否为切片型
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			l = []
			for x in range(stop):
				if x >= start:
					l.append(a)
				a,b = b,a+b
			return l
		pass
