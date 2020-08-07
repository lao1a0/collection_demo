'''
@Time : 2020/5/9 20:05
@Author : laolao
@FileName: md5加密写法.py
'''
'''
@Time : 2020/5/9 19:10
@Author : laolao
@FileName: laji.py
'''

import hashlib


def get_md5(v):
    import hashlib
    # Message Digest Algorithm MD5（中文名为消息摘要算法第五版）为计算机安全领域广泛使用的一种散列函数，用以提供消息的完整性保护
    md5 = hashlib.md5()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来

    ## update需要一个bytes格式参数
    md5.update(v.encode('utf-8'))  # 要对哪个字符串进行加密，就放这里
    value = md5.hexdigest()  # 拿到加密字符串

    return value

a= "0123456789"
for o in a:
    for p in a:
        for q in a:
            for r in a:
                for s in a:
                    for t in a:
                        for u in a:
                            b = str(o)+str(p)+str(q)+str(r)+str(s)+str(t)+str(u)
                            md5 = hashlib.md5(b.encode('utf-8')).hexdigest()
                            '''
                            hashlib.md5(data)函数中，data参数的类型应该是bytes。也就是说我们在进行hash前必须把数据转换成bytes类型
                            '''
                            if ((md5[0:6])=='6d0bc1'):
                                print(b)
