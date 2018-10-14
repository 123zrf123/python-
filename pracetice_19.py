#获取http://hz.17zwd.com/index.htm的女衣商店数
from selenium import webdriver
import time
import xml

driver = webdriver.Chrome('C:\\Users\\12578\\AppData\\Local\\Google\\Chrome\\Application\\Chromedriver.exe')   #打开谷歌浏览器作为测试浏览器
driver.get('https://hz.17zwd.com/sks.htm?so=女衣')    #打开该网页
#driver.implicitly_wait(30)   隐性等待
driver.set_page_load_timeout(30)   #等待加载时间
driver.set_script_timeout(30)           #另一种等待加载时间--- 等待加载防止页面加载没有彻底完成，继续进行下一步操作
pages_info = driver.find_element_by_css_selector('#pages__pager_2')   #利用CSS元素定位器来定位所需要抓取的元素
#print(pages_info.text)   #打印抓取的内容  #这里答应页数
#pages = pages_info.text.split()[2]

for page in range(1,11):   #抓取网站前10页的地址
	url = 'https://hz.17zwd.com/sks.htm?so=女衣' + '&page=' +str(page)   #获取该page页的url地址
	driver.get(url)      #获得该url的信息
	driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')   #该命令为滚动网页页面---用于加载数据
	time.sleep(3)    #强制等待三秒
	goods = driver.find_element_by_css_selector('body > div.web-container > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container').find_elements_by_class_name('huohao-item')
	print('第%d页有%d个商品' %(page,len(goods)))
	for good in goods:    #获取每个商品的信息
		title = good.find_element_by_css_selector('div.huohao-img-container > a').get_attribute('title')   #get_attribute获得标签内容或者属性
		price = good.find_element_by_class_name('price-tag').text
		name = good.find_element_by_css_selector('div:nth-child(4) > div.shop-name-wrapper > a').get_attribute('data-market-name')
		good_link = good.find_element_by_css_selector('div.huohao-img-container > a').get_attribute('href')
		shop_link = good.find_element_by_css_selector('div:nth-child(4) > div.shop-name-wrapper > a').get_attribute('href')
		print('商品名称：%s/\n价格：¥%s\n店铺名字：%s\n商品链接：%s\n店铺链接：%s\n\n\n' %(title,price,name,good_link,shop_link))

