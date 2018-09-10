import string
str1 = 'I love , china '
str1_list = str1.split(' ')
print(str1_list)
length = len(str1_list)
str2_list=[]
for x in range(length-1,-1,-1):
	str2_list.append(str1_list[x])
str2 = ' '.join(str2_list)
print(str2)

