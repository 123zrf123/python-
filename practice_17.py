#获取各省邮政编码初步的爬虫
import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

#一般处理器使用start_element，end_element，char_data即可，具体内容依据所需爬去内容进行编写对于XML编写的类型
class DefaultSaxHandler(object):
	def __init__(self,provinces):
		self.provinces = provinces

	#处理开始标签---start_element事件，在读取<a href="/">时；
	def start_element(self,name,attrs):
		if name != 'map':
			name = attrs['title']
			number= attrs['href']
			self.provinces.append((name,number))
		pass

	#处理标签结束--- end_element事件，在读取</a>时
	def end_element(self,name):
		pass

	#w文本处理==char_data事件，在读取中间文本
	def char_data(self,text):
		pass


url = 'http://www.ip138.com/post'
def get_province_entry(url):

	#获取文本，并用gb232解码
	#get获取该网站资源，器返回200表示成功   .content:表示获取资源的内容   .text:与content类似 但有差别  .decode():表示选择存储是编码方式
	content = requests.get(url).content.decode('gb2312')
	#确定要查找的字符串的开始和结束的位置，并进行切片
	start = content.find('<map name=\"map_86\" id=\"map_86\">')
	end = content.find('</map>')
	content = content[start:end+len('</map>')].strip()
	provinces = []
	#生成SAT处理器---简单快速处理但需要自己处理
	handler = DefaultSaxHandler(provinces)
	#初始化解析器---怎么读取文本的内容
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	#解析数据
	parser.Parse(content)
	return provinces

provinces = get_province_entry('http://www.ip138.com/post')
print(provinces)

