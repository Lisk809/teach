# coding: utf-8
# @Author: 小飞有点东西


# 代码冗余
# 组织结构不清晰、可读性差
# 可维护性、可扩展性差

# 函数（具备某一功能的工具）
# 先定义
# 后调用

# 函数的使用
"""

def 函数名(参数1,参数2,.....):
    '''
    文档描述
    '''
    函数体
    return 值

"""

# def func1():
# print(a
# print('这是我的第一个函数')


# func1()
# print(func1)
# func1()


# def func1():
#     # print(func2)
#     func2()
#     print('我是func1')
# func1()
# def func2():
#     print('我是func2')


# def func1(x, y):  # x=6 y=8
#     print(x, y)
# func1(6, 8)


# def add(x, y):
#     # x = 26
#     # y = 10
#     res = x + y
#     # print(res)
#     return res
# s = add(100, 200)
# print(s)

# def func():
#     name = input('请输入你的姓名>>>')
#     age = input('请输入你的年龄>>>')
#     gender = input('请输入你的性别>>>')
#     res = f'姓名：{name}  年龄：{age}  性别：{gender}'
#     print(res)
# func()
# func()
# func()
# func()


# def add(x, y):
#     res = x + y
#     return res
# s = add(6, 8)*2
# print(s)
# print(add(add(6, 8), 2))


# def 生产轮胎(橡胶, 钢铁):
#     # 经过一系列处理
#     return 轮胎


#
# def 生产底盘(钢铁):
#     # 经过一系列处理
#     return 底盘
#
#
# def 生产发动机(钢铁):
#     # 经过一系列处理
#     return 发动机
#
#
# def 打扫卫生():
#     pass
#
#
# a = 橡胶
# b = 钢铁
# 轮胎 = 生产轮胎(a, b)
# xxx
# xxxx
# 底盘 = 生产底盘(b)
# xxxxxx
# 打扫卫生()
# 组装


# def func():
#     print('aaa')
#     while True:
#         while True:
#             while True:
#                 return 18, '张大仙', True, [1, 2, 3]
#     print('bbb')
# res = func()
# print(res, type(res))


# 定义函数阶段的参数：形式参数，简称：形参
# def func(x, y):  # x=6 y=8
#     pass
# 调用函数阶段传入的参数：实际参数，简称：实参
# a = 6
# b = 8
# func(int('10'), b)


# 位置参数
# 位置形参：定义函数的时候，从左往右依次定义的形参，必须传值，不能多也不能少
# def func(x, y, z):
#     print(x, y, z)

# 默认参数（默认形参）：在定义函数阶段，就为其赋了默认值的形参
# def func(x, y=2):
#     print(x, y)
# func(1, y=3)

# 默认参数的值是在函数定义阶段被赋值的
# a = [2, 3]
# def func(x, y=a):
#     print(x, y)
#
# a.append(4)
#
# func(1)

# Python里面所有的值的传递，都是内存地址的传递，内存地址是对值的引用
# Python里面所有的值的传递，都是引用传递

# 位置实参：在调用函数的时候，从左往右依次传入的值
# func(3, 2, 1)
# 关键字参数（关键字实参）：可以不按顺序传值，按key=value
# func(z=3, x=1, y=2)
# 混用
# func(1, 2, z=3)


# 虽然函数默认参数的值可以指定成任意数据类型，但是不建议指定成可变类型
# append

# def my_append(x, y, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     l.append(y)
#     print(l)
# l2 = [3, 4, 5]
# my_append(1, 2, l=l2)


# 默认参数：默认形参
# 关键字参数：关键字实参


# 什么时候用位置形参？什么时候用默认形参？
# open()


# 可变长度的参数：在调用函数的时候，传入的实参的个数是不固定的
# 可变长度的位置参数
# 用法：*形参名
# def func(x, y, *z):  # z = (3,4,5)
#     print(x, y, z)
# func(1, 2, 3, 4, 5)

# 求和功能
# def func(*args):
#     res = 0
#     for i in args:
#         # res = res + i
#         res += i
#     return res
# s = func(1, 2, 3)
# print(s)

# 可变长度的关键字参数
# 用法：**kwargs
# def func(x, y, **kwargs):   # kwargs = {'a':1,'b':2,'c':3,'name':'张大仙‘)
#     print(x, y, kwargs)
#
#
# func(1, y=2, a=1, b=2, c=3, name='张大仙')


# 命名关键字形参（命名关键字参数）


# def func(x, y, z):
#     print(x, y, z)
# l = [1, 2, 3]
# func(*l)    # func(1, 2, 3)


# def func(x, y, *args):
#     print(x, y, args)

# func(1, 2, *'abc')      # func(1,2,3,4,5)
# func(*'愿疫情早点结束！')


# def func(x, y, **kwargs):
#     print(x, y, kwargs)
# func(**{'x': 1, 'y': 2, 'z': 3})        # func(x=1,y=2,z=3)


# 可变长参数混用
# **kwargs必须放在*args之后
# def func(x, y=2, *args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# func(1, 2, 3, 4, 5, 6, a=7, b=8, c=9)


# 重中之重
# def func1(x, y, z):
#     print('func1>>>', x, y, z)
#
#
# def func2(*args, **kwargs): # args = (1,2)  kwargs={'z':3}
#     func1(*args, **kwargs)      # func1(1,2,z=3)
#
#
# # func2(1, 2, 3)
# func2(1, 2, z=3)


# 名称空间（namespaces）和作用域
# import this


# x = 5


# 1、Python解释器启动：Python内置的名字，如：print，input等
# 2、把文本内容读入内存
# 3、开始识别Python语法：产生变量名，产生函数名，产生模块名
# import time
# import os

# 内置名称空间：Python解释器内置的名字
# Python解释器启动，就会创建内置名称空间。Python解释器关闭，内置名称空间就会被销毁


# 全局名称空间：Python文件（模块）内定义的变量名，包括函数名，类名，模块名
# 要排除掉函数内部定义的名字（包括函数的参数）
# 总结：只要不是函数内部定义的名字，也不是内置的名字，剩下的就都属于全局名称空间的名字
# 全局名称空间，会在Python文件执行之前产生，Python文件运行完毕后销毁


# 局部名称空间：函数内部定义的名字（包括函数的参数）
# 在函数调用时产生，函数调用结束后销毁
# import os
# import time
#
#
# def func(x, y):
#     z = 3
#
#
# a = 1
# b = 2
# func()
# func()


# 名称空间的查找优先级
# 局部名称空间>全局名称空间>内置名称空间
# input = 1
# def func():
#     input = '张大仙'
#
# print(input)
#
# func()


# def func():
#     print(x)
#
#
# func()
# x = 10


# x = 10
# def func1():
#     print(x)
#
#
# def func2():
#     x = 20
#     func1()
#
#
# func2()


# input = 10
# def func1():
#     # input = 20
#     def func2():
#         # input = 30
#         print(input)
#
#     func2()
#     input = 20
#
#
# func1()


# 作用域
# 全局作用域：内置名称空间，全局名称空间
# 1、全局存活
# 2、全局有效
# z = 30
# def func1():
#     x = 10
#     print(z, id(z))
#
#
# def func2():
#     y = 20
#     print(z, id(z))
#
# print(z, id(z))
# func1()
# func2()


# 局部作用域：局部名称空间
# 1、临时存活
# 2、局部有效

# 内置：built-in
# 全局：global
# def func1(x):
#     # enclosing
#     def func2():
#         # enclosing
#         def func3():
#             # local
#             print(x)

# def func4():
#     print(x)


# LEGB
# B:built-in
# G:global
# E:enclosing
# L:local


# x = 10
# def func():
#     global x
#     x = 20
#
# func()
# print(x)


# l = [1,2,3]
# def func():
#     l.append(4)
#
# func()
# print(l)


# nonlocal
# x = 10
# def func1():
#     # x = 20
#     def func2():
#         nonlocal x
#         x = 30
#     print('调用func2之前的x：', x)
#     func2()
#     print('调用func2之后的x：', x)


# func1()
# print('全局的x', x)


# 变量名：指向的是变量值的内存地址
# 函数名：指向的是函数的内存地址
# def func():
#     print('我是func')
# # x = func
# # print(x, func)
# # x()
# def func2(x):
#     # print(x)
#     # x()
#     return x
# a = 10
# res = func2(func)    # func2(func的内存地址)
# # print(res)
# res()


# def func():
#     print('我是func')
# # l = [func]
# # # print(l)
# # l[0]()
# d = {'k1':func}
# # print(d)
# d['k1']()


# 电子钱包功能
# def login():
#     print('执行登录功能')
#
#
# def scan():
#     print('执行扫码支付功能')
#
#
# def transfer():
#     print('执行转账功能')
#
#
# def query():
#     print('执行查询余额功能')
#
#
# def recharge():
#     print('执行充值功能')
#
#
# func_dic = {
#     '0': (None, '退出'),
#     '1': (login, '登录'),
#     '2': (scan, '扫码支付'),
#     '3': (transfer, '转账'),
#     '4': (query, '查询余额'),
#     '5': (recharge, '充值')
# }
# # func_dic['1']()
# while True:
#     for key in func_dic:
#         print(key, func_dic[key][1])
#     opt = input('请输入功能编号>>>')
#     if opt == '0':
#         break
#
#     if opt not in func_dic:
#         print('此功能不存在，傻子')
#         continue
#
#     func_dic[opt][0]()


# 闭包函数
# 闭函数：闭，封闭的意思，函数被封闭起来的
# 包函数：函数内部包含对外层函数作用域名字的引用
# def f1(x):
#
#     def f2():
#         print(x)
#
#     return f2
#
#
# res = f1(10)
# # print(res)
# x = 20
# res()


# 装饰器
# 器：器具，工具
# 装饰：为其他事物添加额外的功能
# 定义一个函数，这个函数的功能就是用来装饰其他函数的
# 也就是说这个函数是用来给其他函数添加额外的功能的

# 开放封闭原则
# 开放：对扩展功能（增加功能）开放，扩展功能的意思是在源代码不做任何改变的情况下，为其增加功能
# 封闭：对修改源代码是封闭的
# def inside(x, y):
#     print(x)
#     print(y)


# 应用程序
# 操作系统（linux）
# 硬件


# 装饰器：不修改被装饰对象的源代码，也不修改调用方式的前提下，给被装饰对象添加新的功能
# import time

# 方案一：
# 问题：没有修改调用方式，但是修改了源代码
# def inside(group, s):
#     start = time.time()
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print('全军出击')
#     end = time.time()
#     print(end-start)
#
#
# # inside('红色', 5)
# inside('蓝色', s=3)


# 方案二：
# 问题：没有修改源代码，也没有修改调用方式，同时还加上了新的功能，但是有大量重复代码，代码冗余
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# start = time.time()
# inside('蓝色', s=3)
# end = time.time()
# print(end-start)
#
# start = time.time()
# inside('蓝色', s=3)
# end = time.time()
# print(end-start)
#
# start = time.time()
# inside('蓝色', s=3)
# end = time.time()
# print(end-start)
#
# start = time.time()
# inside('蓝色', s=3)
# end = time.time()
# print(end-start)
#
# start = time.time()
# inside('蓝色', s=3)
# end = time.time()
# print(end-start)


# 方案三：
# 问题：解决了方案二的代码冗余问题，也没有修改被装饰对象的源代码，同时还为其增加了新的功能
# 但是被装饰对象的调用方式被修改了
# import time
#
#
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# def wrapper():
#     start = time.time()
#     inside('蓝色', s=3)
#     end = time.time()
#     print(end-start)
#
#
# wrapper()


# 方案四
# import time
#
#
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# def wrapper(*args, **kwargs):
#     start = time.time()
#     inside(*args, **kwargs)
#     end = time.time()
#     print(end-start)
#
#
# wrapper('蓝色', 3, '炮车')


# 方案五
# import time
#
#
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# # print('原来的inside的内存地址：', inside)
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#     return wrapper
#
#
# inside = outer(inside)
# # print('新的inside的内存地址：', inside)
# inside('蓝色', s=3, z='炮车')


# 方案六
# import time
# #
# #
# # def inside(group, s, z):
# #     print('欢迎来到王者荣耀')
# #     print(f'你出生在{group}方阵营')
# #     print(f'敌军还有{s}秒到大战场')
# #     time.sleep(s)
# #     print(f'{z}出击')
#
#
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量：{"▉"*i} {i}%', end='')
#     print('电量已充满！')
#
#
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#     return wrapper
#
#
# recharge = outer(recharge)
#
#
# recharge(20)
# #
# #
# # inside = outer(inside)
# # inside('蓝色', s=3, z='炮车')


# 方案七
# import time
# #
# #
# # def inside(group, s, z):
# #     print('欢迎来到王者荣耀')
# #     print(f'你出生在{group}方阵营')
# #     print(f'敌军还有{s}秒到大战场')
# #     time.sleep(s)
# #     print(f'{z}出击')
#
#
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量：{"▉"*i} {i}%', end='')
#     print('电量已充满！')
#     return 100
#
#
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return response
#     return wrapper
#
#
# recharge = outer(recharge)
#
#
# res = recharge(20)
# print(res)
# #
# #
# # inside = outer(inside)
# # inside('蓝色', s=3, z='炮车')


# 语法糖
# import time
#
#
# def count_time(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return response
#     return wrapper
#
#
# @count_time  # inside = outer(inside)
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方阵营')
#     print(f'敌军还有{s}秒到大战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# @count_time
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量：{"▉"*i} {i}%', end='')
#     print('电量已充满！')
#     return 100
#
#
# # inside = outer(inside)
# # recharge = outer(recharge)
#
#
# inside('红色', 3, '炮车')
# recharge(50)


# from functools import wraps
import time


# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper


# def auth(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         name = input('请输入账号>>>').strip()
#         pwd = input('请输入密码>>>').strip()
#         if name == 'jack' and pwd == '123':
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('账号或密码错误！')
#
#     # wrapper.__name__ = func.__name__
#     # wrapper.__doc__ = func.__doc__
#     return wrapper


# @auth
# def home():
#     """这是主页2"""
#     time.sleep(2)
#     print('welcome')
#
#
# # home()
#
#
# # print(home.__name__)
# # print(home.__doc__)
# print(home)


# 1、直接通过参数传递
# 2、闭包函数

# def g_outer(x):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return outer
#
#
# @g_outer('张大仙', 18)    # @outer  home = outer(home)  home = wrapper
# def home():
#     """这是主页2"""
#     time.sleep(2)
#     print('welcome')
#
#
# @g_outer('李白', 19)
# def index():
#     pass
#
# home()
# index()

# 有参装饰器应用
# def auth(source):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             name = input('请输入账号>>>').strip()
#             pwd = input('请输入密码>>>').strip()
#
#             if source == 'file':
#                 print('基于文件的登录验证')
#                 if name == 'jack' and pwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('账号或密码错误！')
#             elif source == 'mysql':
#                 print('基于mysql的登录验证')
#             elif source == 'ldap':
#                 print('基于ldap的登录验证')
#             else:
#                 print('不支持此类验证')
#         return wrapper
#     return outer
#
#
# @auth('file')       # 文件
# def home():
#     print('welcome')
#
#
# @auth('mysql')       # mysql
# def index():
#     pass
#
#
# @auth('ldap')       # ldap
# def default():
#     pass
#
#
# home()
# index()
# default()


# 装饰器叠加使用
# def outer1(func1):
#     def wrapper1(*args, **kwargs):
#         print('开始执行outer1.wrapper1')
#         res1 = func1(*args, **kwargs)    # func1 = 原home
#         print('outer1.wrapper1执行完毕')
#         return res1
#     return wrapper1
#
#
# def outer2(x):
#     def outer(func2):
#         def wrapper2(*args, **kwargs):
#             print('开始执行outer2.wrapper2')
#             res2 = func2(*args, **kwargs)    # func2 = outer1.wrapper1
#             print('outer2.wrapper2执行完毕')
#             return res2
#         return wrapper2
#     return outer
#
#
# def outer3(func3):
#     def wrapper3(*args, **kwargs):
#         print('开始执行outer3.wrapper3')
#         res3 = func3(*args, **kwargs)    # func3 = outer2.wrapper2
#         print('outer3.wrapper3执行完毕')
#         return res3
#     return wrapper3
#
#
# @outer3 # home = outer3(home)   # outer3.wrapper3
# @outer2(10) # outer = outer2(10) => @outer => home = outer(home)   # outer2.wrapper2
# @outer1 # home = outer1(home)   # outer1.wrapper1
# def home(z):
#     print('执行home功能', z)
#     return '张大仙'
#
#
# res = home(0)
# print(res)


