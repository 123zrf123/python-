#多线程爬取网站
import requests
import threading    #多线程的python库

#获取相应股票的url内的信息
def display_info(code):
	url = 'http://hq.sinajs.cn/list=' + code
	response = requests.get(url).text    #利用text方式读取--能根据头做相应的编码识别
	print(response)
	pass

#进行相关的多线程操作
def single_thread(codes):
	for code in codes:
		code = code.strip()
		display_info(code)
	pass

def multi_thread(tasks):
	#用列表推导生成线程，threading.Thread(target = single_thread,args = (codes,)):线程表示方式。target:为目标函数  args:参数。注意codes后面的‘， ’
	threads = [threading.Thread(target = single_thread, args = (codes,)) for codes in tasks]
	#启动线程
	for t in threads:
		t.start()
	for t in threads:
		t.join()    #.join方法的作用是阻塞主进程（挡住，无法执行join以后的语句），专注执行多线程。
	pass

if __name__ == '__main__':      #相当于主函数
	codes = ['sh600001','sh600002','sh600003','sh600004','sh600005','sh600006']
	#计算每个线程要做的工作量
	thread_len = int(len(codes)/4)
	t1 = codes[0:thread_len]
	t2 = codes[thread_len:thread_len*2]
	t3 = codes[thread_len*2:thread_len*3]
	t4 = codes[thread_len*3:]

	#启动多线程
	multi_thread([t1,t2,t3,t4])