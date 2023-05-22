# coding:utf-8
# 字符编码

# 一、计算机三大核心硬件
# CPU、内存、硬盘

# 二、文本编辑器读取文件的三个步骤
#     1、启动文本编辑器
#     2、把文件内容从硬盘读入内存
#     3、把数据显示到屏幕上

# 三、运行python程序的步骤
#     1、启动python解释器
#     2、把test.py文件内容从硬盘读入内存
#     3、把文件内容当成python语法识别


# 字符编码发展史（天下大势，合久必分，分久必合）
# 高电平->1
# 低电平->0
# 字符编码表
# 仙---->10086
#                 内存
# 仙---->翻译---->1010100
# 仙<----翻译<----1010100

# ASCII码表
#       内存      硬盘
# abc---->1010---->1010
# abc<----1010<----1010

# GBK（中文字符、英文字符）
# print(2**16)
# 10101010
# 1010101010101010

# 日本：Shift_JIS
# 韩国：Euc-kr

# 秦始皇：灭六国

# 通用标准
# 1988，unicode
# 1989，UCS
# 1990-1994,unicode(万国码)
# 1bit-->1位二进制数
# 8bit = 1Bytes(字节)
# 1KB = 1024Bytes
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 电信运营商Mbps(兆比特每秒）
# 下载速度MBps(兆字节每秒)
# 100/8 = 12

# unicode
# 2Bytes表示一个字符
# 4Bytes、8Bytes
#         内存        硬盘
# abc---->unicode---->unicode
#                     老文件

# abc---->unicode---->unicode中介---->其他编码格式的文件
# XXX韩文---->unicode---指定gbk--->GBK编码的文件


# GB2312
# 大五码(Big-5)
# GB18030

# I/O问题

# 平均寻道时间
# 7200/60 = 120
# 1000/120 = 8ms/2 = 4ms

# 平均寻址时间
# 5ms

# I/O延迟 = 平均寻道时间 + 平均寻址时间


# 计算机的三大核心硬件
# CPU
# 寄存器、高速缓存等
# 内存
# 硬盘


# UTF-8
# 编码：字符--编码-->unicode--编码-->UTF-8\GBK....
# 解码：字符<--解码--unicode<--解码--UTF-8\GBK....


# 微软：(ANSI)
# 中国：GBK
# 韩国：EUC-KR
# ...

# Unicode           UTF-8
# 0000 - 007F     0xxxxxxx
# 0080 - 07FF     110xxxxx 10xxxxxx
# 0800 - FFFF     1110xxxx 10xxxxxx 10xxxxxx

# 仙---->4ED9---->1110-0100 10-111011 10-011001
# 1110-0100 10-111011 10-011001---->E4BB99

# 联通---->C1AA CDA8
# C1---->1100 0001
# AA---->1010 1010
# CD---->1100 1101
# A8---->1010 1000

# 0000 0000 0110 1010---->006A--->j
# 0000 0011 0110 1000---->0368--->不存在


# Python文件乱码问题
# 指定文件头


# 第三个阶段的乱码问题
# 'x人bb'
# 01001100 10011001 11011101 01100011 01100011
# c8cb ---> 11001000 11001011
# 1001000 ---> 48
# 1001011 ---> 4b


# 编码和解码
# 文件头
# python3
# python2:u''
# a = '人'
# res = a.encode('gbk')
# print(res,type(res))
# print(res.decode('gbk'))


# 文件介绍

# 用户和应用程序
# 操作系统
# 硬件

# open()
# 一、控制文件读写操作的模式
'''
    r:只读模式
    w:只写模式
    a:只追加写模式
    +:r+、w+、a+
'''
# 二、控制文件读写内容的模式
'''
    t模式:
        读写都是以字符串（unicode）为单位的
        指定参数encoding = 'utf-8'
        只针对文本文件
    b模式：bytes模式/二进制模式
'''

# '\n \t \a'
# print('\a')
# 1、打开文件
# open('D:\\teach\\a.txt')
# open('D:/teach/a.txt')
# open(r'D:\teach\a.txt') # 绝对路径
# f = open('data/a.txt', mode='rt', encoding='utf-8')  # 相对路径
# print(f)

# 2、操作文件（读、写）
# res = f.read()
# print(res)

# 3、关闭文件
# f.close()

# with语法(上下文管理器)
# with open('data/a.txt', mode='rt', encoding='utf-8')as f,\
#     open('data/b.txt', mode='rt', encoding='utf-8')as f2:
#     res = f.read()
#     print(res)
#
#     res2 = f2.read()
#     print(res2)

# t\b
# rt
# with open('data/a.txt', mode='rt', encoding='utf-8')as f:
#     # pass
#     print('第1次读'.center(80, '-'))
#     res1 = f.read()
#     print(res1)
#
#     print('第2次读'.center(80, '-'))
#     res2 = f.read()
#     print(res2)

# 登录案例优化
# username = 'd1303544500'
# password = '123456'
# input_username = input('请输入账号>>>').strip()
# input_password = input('请输入密码>>>').strip()
# with open('data/user.txt', mode='rt', encoding='utf-8')as f:
#     res = f.read()
#     username, password = res.split('----')
#     # print(res)
# if input_username == username and input_password == password:
#     print('登录成功')
# else:
#     print('账号或密码错误')


# input_username = input('请输入账号>>>').strip()
# input_password = input('请输入密码>>>').strip()
# with open('data/user.txt', mode='rt', encoding='utf-8')as f:
#     for line in f:
#         # print(line, end='')
#         username, password = line.strip().split('----')
#         # print(l)
#         if input_username == username and input_password == password:
#             print('登录成功')
#             break
#     else:
#         print('账号或密码错误')


# wt
# with open('data/c.txt', mode='w', encoding='utf-8')as f:
#     # f.read()
#     f.write('晓看天色暮看云\n')
#
# with open('data/c.txt', mode='w', encoding='utf-8')as f:
#     f.write('行也思君坐也思君\n')

# at
# with open('data/d.txt', mode='at', encoding='utf-8')as f:
#     # f.read()
#     f.write('那么短，还站那么远\n')
#     f.write('那么短，还站那么远\n')

# 注册功能
# username = input('请输入账号>>>')
# password = input('请输入密码>>>')
# with open('data/user_data.txt', mode='a', encoding='utf-8')as f:
#     f.write(f'{username}----{password}\n')

# 拷贝功能
# old_path = input('请输入原文件路径>>>').strip()
# new_path = input('请输入新文件路径>>>').strip()
# with open(fr'{old_path}', mode='rt', encoding='utf-8')as f1,\
#     open(fr'{new_path}', mode='wt', encoding='utf-8')as f2:
#     res = f1.read()
#     f2.write(res)

# +模式
# r+
# with open('data/d.txt', mode='w+t', encoding='utf-8')as f:
#     f.write('abc\n')
#     f.write('def\n')
#     res = f.read()
#     print(res)
# f.write('嘿嘿嘿')

# w+
# a+

# x
# with open('data/g.txt', mode='x', encoding='utf-8')as f:
#     # f.read()
#     f.write('x模式\n')

# \r
# \n
# windows:\r\n
# linux:\n
# mac os 9:\r
# mac os 9之后：\n

# b
# with open('data/超级爱你.jpg', mode='rb')as f:
#     res = f.read()
#     print(res)
#     print(type(res))

# with open('data/a.txt', mode='rb')as f:
#     res = f.read()
#     print(res,type(res))
#     print(res.decode('utf-8'))

# with open('data/h.txt', mode='wb')as f:
#     f.write('天下没有白吃的午餐'.encode('utf-8'))
#     f.write('天下没有白吃的午餐'.encode('gbk'))

# 拷贝功能
# old_path = input('请输入原文件路径>>>').strip()
# new_path = input('请输入新文件路径>>>').strip()
# with open(fr'{old_path}', mode='rb')as f1,\
#     open(fr'{new_path}', mode='wb')as f2:
#     # for line in f1:
#     #     f2.write(line)
#     while 1:
#         res = f1.read(1024)
#         if not res:
#             break
#         f2.write(res)

# with open('data/超级爱你.jpg', mode='rb')as f:
#     for line in f:
#         print(line)

# with open('data/超级爱你.jpg', mode='rb')as f:
#     while 1:
#         res = f.read(1024)
#         if not res:
#             break
#         print(res)
#         print(len(res))


# readline、readlines
# with open('data/user.txt', mode='rt', encoding='utf-8')as f:
    # res = f.readline()
    # print(res)
    # res = f.readline()
    # print(res)
    # while True:
    #     line = f.readline()
    #     if len(line) == 0:
    #         break
    #     print(line)
    # res = f.readlines()
    # print(res)
    # f.read(1024)

# writelines
# with open('data/i.txt', mode='wb')as f:
#     l = [
#         b'abc\n',
#         b'12a\n',
#         b'222\n',
#         bytes('人\n', encoding='utf-8')
#          ]
#     f.writelines(l)

# print('1a2b3c\n'.encode('utf-8'))
# print('1a2b3c\n'.encode('gbk'))
# print('人'.encode('utf-8'))
# print(bytes('人', encoding='utf-8'))


# with open('data/j.txt', mode='wt', encoding='utf-8')as f:
    # f.write('a')
    # f.flush()
    # print(f.readable())
    # print(f.writable())
    # print(f.closed)
    # print(f.encoding)
    # print(f.name)
# print(f.closed)



# f.readable()  # 判断文件是否可读
# f.writable()  # 判断文件是否可读
# f.closed  # 判断文件是否关闭
# f.encoding  # 获取当前编码方式，如果文件打开模式为b,则没有该属性
# f.name  # 获取当前文件名


# with open('data/j.txt', mode='rb')as f:
#     f.seek(5, 0)
#     f.seek(4, 0)
#     print(f.tell())
#     res = f.read()
#     s = res.decode('utf-8')
#     print(s)

# f.seek(n,参照位置)
# 模式0
# f.seek(5,0) #5
# f.seek(2,0) #2
# 模式1
# f.seek(5,1) #5
# f.seek(2,1) #7
# 模式2
# f.seek(-5,2) #7
# f.seek(-2,2) #10

# tail(监控文件内容)
# while True:
#     money = input('你要充值多少>>>')
#     with open('data/user.log', mode='at', encoding='utf-8') as f:
#         f.write(f'20351008061010----张大仙充值了{money}w\n')


# 修改文件
# 第一种修改文件的方式（文本编辑器修改文件的方式）
# with open('data/a.txt', mode='rt', encoding='utf-8')as f:
#     res = f.read()
    # print(res)
    # l = list(res)
    # l.insert(3, '不')
    # print(l)
    # new_res = ''.join(l)
    # print(new_res)
#     new_res = res.replace('我喜欢你', '我不喜欢你')
#     print(new_res)
# with open('data/a.txt', mode='wt', encoding='utf-8')as f1:
#     f1.write(new_res)
# 第二种修改文件的方式
import os
with open('data/k.txt', mode='rt', encoding='utf-8')as f,\
        open('data/.k.txt.swap', mode='wt', encoding='utf-8')as f1:
    for line in f:
        res = line.replace('一天', '一年')
        f1.write(res)
os.remove('data/k.txt')
os.rename('data/.k.txt.swap', 'data/k.txt')











