#机器学习--支持向量机SVM
from sklearn import svm,datasets     #svm表示支持向量机   datasets表示sklearn自带的数据集

class Dataset(object):     #创造一个dataset的类，这里引用sklearn自带的数据集
	"""docstring for Dataset"""
	def __init__(self,name):
		self.name = name
		#self.downloaded_data = downloaded_data

	def download_data(self):
		if self.name == 'iris':     #这是sklearn自带的分类数据 鸢尾花的数据集，该数据集有4个特征，3个类别
			self.downloaded_data = datasets.load_iris()
		elif self.name == 'digits':  #这是一个sklearn自带的分类数据集  数字识别。
			self.downloaded_data = datasets.load_digits()
		else:
			print('Dateset Error:NO named datasets')
		pass
#将输入的数据集分为输入和输出
	def generate_xy(self):
		self.download_data()
		x = self.downloaded_data.data
		y = self.downloaded_data.target
		print('\nOriginal data looks like this: \n', x)
		print('\nlabels looks like this: \n', y)
		return x,y
		pass

	def get_train_test_set(self,ratio):     #划分训练集和测试集
		x,y = self.generate_xy()
		n_samples = len(x)
		n_train = int(n_samples*ratio )   #取整的问题
		x_train = x[:n_train]    #从开始到n_train
		y_train = y[:n_train]
		x_test = x[n_train:]
		y_test = y[n_train:]
		return x_train,y_train,x_test,y_test
		pass

data = Dataset('digits')      #实例化
x_train,y_train,x_test,y_test = data.get_train_test_set(0.7)

clf = svm.SVC()   #这里 clf 是 classifier的简称，SVC指的是SVM的classification版本
clf.fit(x_train,y_train)
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
# decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#  max_iter=-1, probability=False, random_state=None, shrinking=True,
#  tol=0.001, verbose=False)
print(x_test[12])
test_point = x_test[12]
y_true = y_test[12]

y_predict = clf.predict(x_test)

m = len(y_test)
n = 0
for i in range(m):
	if y_test[i] == y_predict[i]:
		n = n+1

print('probability :%f' %(n/m))


