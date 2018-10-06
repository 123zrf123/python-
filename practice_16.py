#美国亚利桑那州Pima印第安女人患有糖尿病状况分析
from sklearn import svm,datasets    #svm表示支持向量机   datasets表示sklearn自带的数据集
import os
import sys
import pickle
from pickle import load
from numpy import *
from functools import reduce
from sklearn.metrics import roc_curve, auc,accuracy_score
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




class Dataset(object):     #创造一个dataset的类，这里引用sklearn自带的数据集
	"""docstring for Dataset"""
	def __init__(self,name,data = [],target = []):
		self.name = name
		self.data = data
		self.target = target
		#self.downloaded_data = downloaded_data

	def download_data(self):
		if self.name == 'Pima':
			with open('F:\python练习\practice_11\pima-indians-diabetes.txt','r') as f:
				for line in f:
					l = len(line)
					l_x = line[:l-3]
					y_data = int(line[l-2:l-1])		
					x_data = l_x.split(',')
					x_data = list(map(float,x_data))
					self.data.append(x_data)
					self.target.append(y_data)

#将输入的数据集分为输入和输出
	def generate_xy(self):
		self.download_data()
		x = self.data
		y = self.target
		print('\nOriginal data looks like this: \n', x)
		print('\nlabels looks like this: \n', y)
		return x,y
		pass

	def serialize_and_deserialization(self,ratio):
		x,y = self.generate_xy()
		n_samples = len(x)
		n_train = int(n_samples*ratio )   #取整的问题
		x_train = x[:n_train]    #从开始到n_train
		y_train = y[:n_train]
		x_test = x[n_train:]
		y_test = y[n_train:]		
		with open('./practice_11/x_train.txt','wb') as f_1:
			pickle.dump(x_train,f_1)
		with open('./practice_11/y_train.txt','wb') as f_2:
			pickle.dump(y_train,f_2)
		with open('./practice_11/x_test.txt','wb') as f_3:
			pickle.dump(x_test,f_3)
		with open('./practice_11/y_test.txt','wb') as f_4:
			pickle.dump(y_test,f_4)
		pass

	def get_train_test_set(self,ratio):     #划分训练集和测试集
		self.serialize_and_deserialization(ratio)
		with open('./practice_11/x_train.txt','rb') as f_1:
			x_train = load(f_1)
		with open('./practice_11/y_train.txt','rb') as f_2:
			y_train = load(f_2)
		with open('./practice_11/x_test.txt','rb') as f_3:
			x_test = load(f_3)
		with open('./practice_11/y_test.txt','rb') as f_4:
			y_test = load(f_4)
		return x_train,y_train,x_test,y_test
		pass


#SVM学习
data = Dataset('Pima')      #实例化
x_train,y_train,x_test,y_test = data.get_train_test_set(0.7)
clf = svm.SVC(probability=True)   #这里 clf 是 classifier的简称，SVC指的是SVM的classification版本probability=True显示概率
clf.fit(x_train,y_train)          #对数据集进行学习
y_predict = clf.predict(x_test)   #对测试集进行预测
accuracy_score(y_test, y_predict) #ACC--准确率
pro = clf.predict_proba(x_test)   #获取决策值---这里即2类的隶属度
fpr,tpr,thresholds = roc_curve(y_test,pro[:,1])   #fpr--原本是0的认成1的概率（假报警率---假正率） tpr---原本是1的认成1的概率 （命中率---真正率）
roc_auc = auc(fpr, tpr)    #计算AUC---ROC曲线下方的面积大小越大越好
m = len(y_test)
MSE = list(map(lambda x,y:pow((x-y),2),y_test,y_predict))   #计算MSE----平均误差
MSE = (reduce(lambda x,y:x+y,MSE))/(m)

#------------------------------------------------------------#画ROC曲线图
lw = 2
plt.figure(figsize=(10,10))
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc) ###假正率为横坐标，真正率为纵坐标做曲线
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")   #设置图例显示位置
plt.savefig('roc_auc曲线分析.png')
#plt.show()



#-------------------------------------------------发送邮箱
mail_host = 'smtp.qq.com'    #设置服务器，先连接到SMP服务器
mail_user = '125780546'      #用户名
mail_pass = 'skyseakgorpubhbd'     #用户授权码
 
def send_mail(to_list,sub,content):      #to_list:收件人  sub:主题   content:内容
	sender = '125780546@qq.com'           #发送者的邮箱
	msg = MIMEMultipart('mixed')
	#msg =MIMEText(content,'html','utf-8')  #三个参数：第一个为文本内容，第二个html设置文本格式，第三个utf-8设置编码
	msg['Subject'] = sub
	msg['From'] = sender
	msg['To'] = ';'.join(to_list)
	s = smtplib.SMTP()    #实例化smtplib中的SMTP模块
	s.connect(mail_host)  #连接服务器
	s.ehlo()
	s.starttls()
	s.login(mail_user,mail_pass)  #登陆服务器
	fp = open('roc_auc曲线分析.png', 'rb')
	msgImage = MIMEImage(fp.read())    #读入图片
	fp.close()
	msgImage.add_header('Content-ID', '<image1>')
	msgImage.add_header("Content-Disposition", "attachment", filename=("gbk", "", "roc_auc曲线分析.png"))
	msg.attach(msgImage)    #添加图片
	try:
		s.sendmail(sender,to_list,msg.as_string())  #利用该函数发送邮件
		print('邮件发送成功')
	except smtplib.SMTPException:
		print('Error:无法发送邮件')
	s.close()

to_list = '2693338623@qq.com'
sub = '美国亚利桑那州Pima印第安女人患有糖尿病状况分析'
content = 'roc_auc曲线分析'
send_mail(to_list,sub,content)

