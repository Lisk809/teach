# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA

# 内置函数
# enumerate 枚举
# li = ['a', 'b', 'c', 'd']
# for index, value in enumerate(li, 100):
#     print(index, value)

# zip 拉链
# li = ['a', 'b', 'c', 'd']
# li2 = [1, 2, 3, 4]
# li3 = [11,22,33]
# for i in zip(li, li2, li3):
#     print(i)


# __import__
# name = 'time'
# time = __import__(name)
# print(time.time())


# globals()		locals()
# print(globals())
# def func():
#     a = 1
#     print(locals())
# func()

# eval()
# b = 3
# g = {'b': b}
# l = {'b': 4}
# res = eval('1+2+b', g, l)
# print(res)
# print(l)


# exec()
# def func():
#     b = 3
#     g = {'b': b}
#     l = {}
#     exec('a=1+2+b', g, l)
#     print(l)
#
#
# func()

# def func():
#     g = locals()
#     g['age'] = 18
#     print(age)
# func()


# eval() exec()
# g = {}
# g['__builtins__'] = None
# res = eval(input('>>>'), g)
# # print(res, type(res))


# class Human:
#     star = 'earth'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# obj = Human('张大仙', 73)
# print(vars(Human))
# print(Human.__dict__)

# print(vars())
# print(locals())

# s = frozenset({1, 2, 3})


# 异常处理
# 实战项目 GUI编程（带界面的程序）
# Python全栈高级篇
