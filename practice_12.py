#高级面向对象--- 实现一个类支持for循环输出素数
class prime_number(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(prime_number, self).__init__()
		self.arg = 1

	def __iter__(self):       #__iter__函数可以实现类具有for....in的效果。for n in prime_number():
		return self
		pass

	def __next__(self):       #__iter__函数可以实现循环的特点，其会不断调用__next__函数来进行迭代
		self.arg = self.arg + 1
		i = self.function(self.arg)
		if self.arg < 1000:
			if i != 1:
				return self.arg
			else:
				return ''
		else:
			raise StopIteration()
		pass

	def function(self,x):     #定义一个素数判断函数
		x = self.arg
		i = 0
		for y in range(1,x+2):
			if (x != y) & (y != 1):
				if x%y == 0:
					i = 1
		return i

for n in prime_number():    #开始进行迭代
	print(n)

