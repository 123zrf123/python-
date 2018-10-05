#电话号码的正则匹配
import re

def match_phone(phone_number):
	match_p = re.match(r'(\+0086\d{11})|(\+\d{8}\d{10})|(\+\d{8}\d{5})',i)
	if match_p:
		return match_p
	pass
phone = ['+008613112345678','+861795101023231212','+8608715432231','01023459764','06346046499','010120']
for i in phone:
	match_p = match_phone(i)
	if match_p:
		print(match_p.group())