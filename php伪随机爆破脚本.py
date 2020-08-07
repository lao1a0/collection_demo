'''
@Time : 2020/4/24 13:41
@Author : laolao
@FileName: php伪随机爆破脚本.py
'''
str1 = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2 = 'vUPxZbEjFK'
str3 = str1[::-1]
length = len(str2)
res = ''
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res += str(j) + ' ' + str(j) + ' ' + '0' + ' ' + str(len(str1) - 1) + ' '
            break

print(res)
