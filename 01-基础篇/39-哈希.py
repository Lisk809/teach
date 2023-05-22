# coding: utf-8
# @Author: 小飞有点东西


# hash(哈希)
# md5
# sha1
# sha256
# sha512


# hash值
# 1、输入敏感
# 2、不可逆
# 3、计算极快而长度固定

# 用途：
# 1、密码加密
    # 8位纯数字：1亿种组合
    # i5四核：每秒200亿次
    # 密码库
# 2、文件完整性校验


# import hashlib

# h1 = hashlib.sha512()
# h1.update('abc'.encode('utf-8'))
# h1.update('123'.encode('utf-8'))
# print(h1.hexdigest())
#
# h2 = hashlib.sha512('ab'.encode('utf-8'))
# h2.update('c'.encode('utf-8'))
# h2.update('1'.encode('utf-8'))
# h2.update('23'.encode('utf-8'))
# print(h2.hexdigest())


# import hashlib

# with open('d:/Desktop/【淘宝】python-3.10.5-amd64.exe', 'rb')as f:
#     f.seek()
#     m1 = hashlib.md5(f.read())
#     print(m1.hexdigest())


# import os
#
# path = 'd:/Desktop/【官网】python-3.10.5-amd64.exe'
# print(os.path.getsize(path))
#
#
# m = hashlib.md5()
# with open(path, 'rb')as f:
#     f.seek(0, 2)
#     size = f.tell()
#     print(size)
#
#     one_tenth = size//10
#     for i in range(10):
#         f.seek(i*one_tenth, 0)
#         res = f.read(100)
#         m.update(res)
#     print('e034da3c35d6b2f6d73b576c86552f5a')
#     print(m.hexdigest())


# 密码加盐
pwd = 'xyxy520'
'xy'
'天青色等烟雨'
'xy'
'而我在等你'
'520'



import hashlib

m = hashlib.md5()
m.update(pwd[:2].encode('utf-8'))
m.update('天青色等烟雨'.encode('utf-8'))
m.update(pwd[2:4].encode('utf-8'))
m.update('而我在等你'.encode('utf-8'))
m.update(pwd[4:].encode('utf-8'))

print(m.hexdigest())






