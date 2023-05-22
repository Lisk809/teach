# coding: utf-8
# @Author: 小飞有点东西


# 迭代器：不依赖于索引的迭代取值方式
# num = 0
# while True:
#     print(num)
#     num += 1


# l = ['a', 'b', 'c']
# num = 0
# while num < len(l):
#     print(l[num])
#     num += 1


# 可迭代对象：可以转换为迭代器的对象，就称之为可迭代对象
# 只要内置有__iter__()方法的就可以称之为可迭代对象
# l = [1, 2, 3]
# # l.__iter__()
# s = '张大仙'
# # s.__iter__()
# t = (1, 2, 3)
# # t.__iter__()
# d = {'key1': 1}
# # d.__iter__()
# s2 = {1, 2, 3}
# # s2.__iter__()
# with open('data/user_data.txt', mode='rt',encoding='utf-8')as f:
#     # f.__iter__()
#     # f.__next__()
#     pass


# d = {'key1': 1, 'key2': 2, 'key3': 3}
# res = d.__iter__()
# # print(res)
# # print(res.__next__())
# # print(res.__next__())
# # print(res.__next__())
# # print(res.__next__())
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break
#
# res = d.__iter__()
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break


# 迭代器对象：内置有__next__()方法，并且还内置有__iter__()方法的对象
# 迭代器对象调用__next__()方法，就会得到迭代器的下一个值
# 迭代器对象调用__iter__()方法，得到的是迭代器本身（和没调一样）
# s = {1, 2, 3}
# res = s.__iter__()
# print(res.__iter__() is res)
# for i in 可迭代对象.__iter__()
# for i in 迭代器对象.__iter__()

# d = {'key1': 1, 'key2': 2, 'key3': 3}
# # 1、调用对象的__iter__()方法，得到一个它的迭代器版本
# # 2、调用该迭代器的__next__()方法，拿到一个返回值，赋值给key
# # 3、循环执行第2步，直到抛出异常，就捕获异常，并结束循环
# for key in d:
#     print(key)


# list(文件对象)
# tuple('张大仙')


# l = [1, 2, 3]
# l = range(10000000)
# l.__iter__()
# 生成器
# def func():
#     print('第一次执行')
#     yield 1
#     print('第二次执行')
#     yield 2
#     print('第三次执行')
#     yield 3
#     print('第四次执行')
#     yield 4
#     print('第五次执行')
#
#
# res = func()
# # print(res)
# res = iter(res)
# print(next(res))
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
#
# # a = [1,2,3]
# # # a.__len__()
# # len(a)


# yield表达式
# def func(x):
#     print(f'{x}开始执行')
#     while True:
#         y = yield None
#         print('\n', x, y, '\n')
#
#
# g = func(1)
# g2 = func(1)
# g3 = func(1)
# g4 = func(1)
# g5 = func(1)
# g.send(None)    # next(g)
# # g.send(None)
# # next(g)
# g.send(10)
# ajlasjkfa
# asfjlkajfa
# jklafj
# jlkaf
# 20
#
#
# g.send(20)






