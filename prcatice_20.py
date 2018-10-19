#登陆豆瓣获取用户自己看过和想看电影的名字
import requests
from bs4 import BeautifulSoup
import html5lib
import re
from lxml import etree
import string

s =  requests.Session()   #Session这个命令能够自动保存cookies，可以设置请求参数，下次请求时自动带上参数
url_login = 'https://accounts.douban.com/login'     #豆瓣的登陆url

formdata = {                            #利用formdata提交数据表单---这里提交登陆的数据表单
	'redir':'https://www.douban.com',   #登陆后加载该豆瓣首页
	'form_email':'18482150898',          #登陆账号   form_email为name名：后面为value值
	'form_password':'zrf123456',         #登陆密码
    'login':u'登陆'                     #按登陆键
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}   #头请求---用于让服务器识别是否为该浏览器发出的请求

r = s.get(url_login)  #向该网也前提交请求
content = r.text      #获取登陆网页的信息
soup = BeautifulSoup(content,'html5lib')   #以浏览器的方式解析文档
captcha = soup.find('img',id = 'captcha_image')    #从html5文档中寻找是否带有上述字符的位置
if captcha:             #判断是否有验证码---captcha为是否找到验证码
	captcha_url = captcha['src']   #属性src内存有验证图片的url
	re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'   #匹配验真码信息
	captcha_id  = re.findall(re_captcha_id,content)             #查找验证码信息
	print(captcha_url)
	print(captcha_id[0])                                          
	captcha_text = input('please input the captcha:')   #输入验证码
	formdata['captcha-solution'] = captcha_text         #将验证码的信息放入数据表单中
	formdata['captcha-id'] = captcha_id[0]
	for key,value in formdata.items():
		print(key+':'+value)
r = s.post(url_login,data = formdata,headers = headers)
print(r.url)
with open('contacts.txt','w+',encoding = 'utf-8') as f:
	f.write(r.text)

#with open('contacts.txt','r',encoding = 'utf-8') as f:
#	contact = f.read()

#利用cookies来进行登陆
s = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}   #头请求---用于让服务器识别是否为该浏览器发出的请求
cookies = {'cookies':'ll="118172"; bid=FjMunXEwf0o; _ga=GA1.2.1882155233.1539827128; _gid=GA1.2.512831730.1539827176; ps=y; __yadk_uid=DQpjzEpFWxKD4QHHufEKkIdO5ClYnXDT; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18605; __utmc=30149280; douban-profile-remind=1; ap_v=0,6.0; __utmz=30149280.1539950469.8.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/186057567/; _vwo_uuid_v2=DD84B7B69644B42BBE3C75029BE83D918|f1a093ade26464c5b0d43d4ffea89856; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1539955892%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1882155233.1539827128.1539950469.1539956192.9; __utmt=1; _gat_UA-7019765-1=1; _pk_id.100001.8cb4=7028fafa714db693.1539827127.9.1539956489.1539953184.; __utmb=30149280.7.10.1539956192; dbcl2="186057567:0A7XiWQsDXQ"'}
url = 'https://www.douban.com'
r = s.get(url,cookies = cookies,headers = headers)     #利用cookies的方式打开网页
with open('contacts_2.txt','w+',encoding = 'utf—8') as f:
	f.write(r.text)


r.encoding = 'utf—8'
#print(r.text)
root = etree.HTML(r.text)
#print(root)
my_douban_url  = root.xpath('//*[@id="db-nav-sns"]/div/div/div[3]/ul/li[2]/a//@href')

movie = s.get(my_douban_url[0],cookies = cookies,headers = headers)
#print(movie.text)
root = etree.HTML(movie.text)
my_movie_url = root.xpath('//*[@id="movie"]/h2/span//@href')
print(my_movie_url)
for url in my_movie_url:
	r = s.get(url,cookies = cookies,headers = headers)
	root = etree.HTML(r.text)
	names = root.xpath('//*[@id="content"]/div[2]//li[@class="title"]/a/em/text()')
	for name in names:
		print(name)




