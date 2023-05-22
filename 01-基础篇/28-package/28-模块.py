# coding: utf-8
# @Author: 小飞有点东西


# 模块：一系列功能的集合体
# import time
# import os


# 一、Python内置的模块
# 二、第三方模块
# 三、自定义模块

"""
模块：python文件就是一系列功能的集合体，就可以称之为一个模块
包：把文件夹作为模块使用，文件夹里面必须有__init__.py
"""
# x = 10
# y = 20
# import module
# del module
#
# name = '李白'
# # print(module.name)
# # module.func1()
# module.func2()
# # print(module.name)
# module.get()
# # func1()
# # func2()


# import time
# import os
#
# def func():
#
#     import pymysql
#     import requests
#
# import module as m  # m = module
# import modulefjalfjlkafjkla as mod
#
# m.name
# m.func1()


# import module
# from 模块名 import 功能名
# import module
# from module import name
# from module import func1
# from module import func2
# from module import get

# print(name)
# print(func1)
# print(func2)
# print(get)

# module.get()


# from module import name
# from module import func1
# from module import func2
# from module import get
#
# # name = '李白'
# func2()
# # from module import name
#
# get()
# print(name)


# from module import name, func1, func2, get

# name = '李白'

# from module import *
# print(name)
# print(func1)
# print(func2)
# print(get)

# get()
# print(name)
# func1()


# from module import func1 as f1
# f1()


# 循环导入问题

# 模块的查找顺序
# import sys
# print(sys.path)
# import time
# import module
# module.get()
# time.sleep(10)
#
# import module
# module.get()

# 1、内存
# 2、硬盘

# import sys
# sys.path.append(r'D:\teach\28-package\mm')
#
# import module
#
# module.get()


# 1、创建名称空间
# 2、执行Python文件
# 3、在执行文件的名称空间中创建一个名字，指向前面产生的名称空间
# 包
# import pack
# # from pack import
#
# print(pack.name)

import sys
sys.path.append(r'D:\teach\28-package\mm')
# print(sys.path)
# import game
#
# game.chat()
# game.kanpsack()
# game.map()

from game import chat
from game import kanpsack
from game import map
from game import brilliant
from game import sell


chat()
kanpsack()
map()
print(brilliant)
sell()






