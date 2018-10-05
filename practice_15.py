#计算日期之间的工作日
import time 
import datetime



class workday(object):
	"""docstring for ClassName"""
	def __init__(self, start_day,end_day):
		super(workday, self).__init__()
		self.start_day = start_day
		self.end_day = end_day
		self.days_off = 5,6
        # 每周工作日列表
		self.days_work = [x for x in range(7) if x not in self.days_off]
		
	def caltime(self):
		day1 = time.strptime(self.start_day,'%Y-%m-%d')
		day2 = time.strptime(self.end_day,'%Y-%m-%d')
		day1 = datetime.datetime(*day1[:3])
		day2 = datetime.datetime(*day2[:3]) - datetime.timedelta(days = 1)
		tag_day = day1

		while True:
			if tag_day > day2:
				break
			if tag_day.weekday() not in self.days_off:
				yield tag_day
			tag_day = tag_day + datetime.timedelta(days = 1)


	def dayscount(self):
		return len(list(self.caltime()))
		pass





def is_date(data):
	try:
		time.strptime(data,'%y-%m-%d')
		return True
	except:
		return False
	pass


if __name__ == '__main__':
	print('print-start day1(格式：xxxx-xx-xx):') 
	day1 = input()
	print(type(day1))
	if is_date(day1) == True:
		pass
	else:
		print("输入正确格式：xxxx-xx-xx")


	print('print-end day2(格式：xxxx-xx-xx):')
	day2 = input()
	if is_date(day2) == True:
		 pass
	else:
		print("输入正确格式：xxxx-xx-xx")
	day = workday(day1,day2)

	print(day.dayscount())
