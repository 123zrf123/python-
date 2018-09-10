def function(x):
	i = 0
	for y in range(1,x+2):
		if (x != y) & (y != 1):
			if x%y == 0:
				i = 1
	if i != 1:
		print('%d' %x)


for x in range(1,100000):
	function(x)



