#翻转单项列表（利用类的方式）
#单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域
class Node(object):
	"""docstring for ListNode"""
	def __init__(self, val,p = None):
		self.data = val
		self.next = p

class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):
		self.head = 0

	def __getitem__(self,key):                 #控制getitem函数
		if self.is_empty():
			print('linklist is empty')
			return
		elif key<0 or key>self.getlength():
			print('the given key is error')
			return
		else:
			return self.getitem(key)
		pass

	def __setitem__(self, key, value):
		if self.is_empty():
			print ('linklist is empty.')
			return
		elif key <0  or key > self.getlength():
			print ('the given key is error')
			return
		else:
			self.delete(key)
			return self.insert(key)

	def is_empty(self):
		if self.getlength() == 0:
			return True
		else:
			return False
		pass

	def getlength(self):                #求该单向链表的长度
		if self.head == 0:
			return 0
		p = self.head                   #指向一开始的链表的地址即链表的头结
		length = 0                      #设定初始值
		while p != None:                #判断该链表的末尾是否为零---这里改成none 判断链的末端指针域是否存在，因为开结只有地址所以直接用P
			length = length + 1         
			p = p.next                  #地址指向下一个
		return length
		pass

	def initlist(self,data):
		if data == []:
			return 
		self.head = Node(data[0])       #实例化Node类    这里返回的值一般是该类指向的地址
		p = self.head                   #p就相当于实例化了Node类   
		for i in data[1:]:              #相当于重复创建单节链
			node = Node(i)              #这里node给Node做实例化 node这里指向的是data[i]的地址 其地址内存储着（val,next）
			p.next = node               #这里给p.next赋值node地址  记录date[i]的地址
			p = p.next                  #p指向该地址 即跳转到下一个地址
		p.next = None


	def getitem(self,index):
		if self.is_empty():
			return 'LinkList is empty'
		j = 0
		p = self.head
		while p.next!=None and j<index:
			p = p.next
			j = j+1
		if j == index:
			return p.data
		else:
			print('target is not exit')

	def append(self,item):           #在链表对的末尾添加元素
		q = Node(item)               #q指向该元素的地址
		if self.head == None:        #判断首地址是否为空None
			self.head = q            #是则头结指向该地址
		else:  
			p = self.head            #否则指向下一个链的地址
			while p.next!=None:      #判断该链下一个链的地址是否为空Node
				p = p.next           #指向下个链的地址
			p.next = q               #找到末尾链将新加入的地址存入
		pass

	def insert(self,index,item):     #插入链表
		if self.is_empty() or index<0 or index>self.getlength(): #判断输入是否合理
			print('Linklist is empty')
			return
		if index == 0:               #若在顶部插入则改变头结的地址并且在该地址的某位插入下一结的地址
			q = Node(item,self.head)
			self.head = q
			return
		p = self.head                #之后post表示该位置前一个地址，p表示要插入位置的地址
		post = self.head
		j = 0
		while p.next!=None and j<index:
			post = p
			p = p.next
			j = j +1
		if index == j:
			q = Node(item,p)
			post.next = q
			q.next = p
		pass

	def delete(self,index):              #删除链中的某个位置--和插入类似
		if self.is_empty() or index<0 or index>self.getlength(): #判断输入是否合理
			print('Linklist is empty')
			return
		if index == 0:
			q = Node(item,self.head)
			self.head = q
		p = self.head
		j = 0
		post = self.head
		while p.next!=None and j<index:
			post = p
			p = p.next
			j = j + 1
		if index == j:
			post.next = p.next

	def index(self,value):
		if self.is_empty():
			print('Linklist is empty')
			return
		p = self.head
		i = 0
		while p.next!=None and not p.data == value:
			 p = p.next
			 i = i + 1
		if p.data == value:
			return i 
		else:
			return -1

	def last(self):           #在链表对的末尾添加元素
		if self.head == None:        #判断首地址是否为空None
			print('Linklist is empty')
			return
		else:  
			p = self.head            #否则指向下一个链的地址
			while p.next!=None:      #判断该链下一个链的地址是否为空Node
				p = p.next           #指向下个链的地址
			p.next = q               #找到末尾链将新加入的地址存入
		pass

	def reversal(self):       #利用循环的方式翻转
		address = self.head
		p = address
		post = address
		j = 0
		if self.is_empty():
			print('LinkList is empty')
			return
		while p.next!=None:
			post = p
			p = p.next
			j = j+1
		p.next = post
		post.next = None
		n = p
		m = j
		for i in range(m,0,-1):
			p = address
			post = address
			j = 0
			while p.next!=None:
				post = p
				p = p.next
				j = j+1
			p.next = post
			post.next = None
		self.head = n





l = LinkList()         #实例化这个类 LinkList--定义单向链表的一系列操作
l.initlist([])   #调用LinkList中的initlist函数---实现单向链表的创建
print(l.getitem(1))
l.reversal()


