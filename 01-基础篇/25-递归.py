# coding: utf-8
# @Author: 小飞有点东西


# 函数嵌套：
# 1、定义的时候嵌套（装饰器）
# 2、调用的时候嵌套

# 递归
# 在调用一个函数的过程中，又调用到了自己本身这个函数
# import sys
#
# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())

# 直接调用
# def func():
#     print('张大仙')
#     func()
#
#
# func()


# 间接调用
# def func1():
#     print('func1')
#     func2()
#
#
# def func2():
#     print('func2')
#     func1()
#
#
# func1()

# def func():
#     print(111)
#     print(222)
#     print(333)
#     if 条件：
#         pass
#     else:
#         func()


# 计算1到10的和
# i = 100
# def my_sum(i):
#     if i == 0:
#         return i
#     return i + my_sum(i - 1)
#
#
# res = my_sum(i) # 10 + 9 + 8 + .....+1 + None
# print(res)


# 一、要求：把下面列表的每一个值单独打印出来
l = [1, 2, [3, [4, [5, [6, [7, [8, [9, [10, [11, 12]]]]]]]]]]
# l = [1, 2, [3, 4]]
# def func(li):
#     for i in li:
#         if type(i) is list:
#             func(i)
#         else:
#             print(i)
#
#
# func(l)


# 二、要求：把下列的字符串做全排列
# s = 'abc'
# l = list(s)
# def permutation(l, level):
#     if level == len(l):
#         print(l)
#     for i in range(level, len(l)):
#         l[level], l[i] = l[i], l[level]
#         permutation(l, level+1)
#         l[level], l[i] = l[i], l[level]
#
#
# permutation(l, 0)


# 二分法

# 番茄炒鸡蛋
# 1、准备食材
# 2、炒鸡蛋
# 3、加番茄
# 4、加盐、糖、葱花
# 5、出锅

# 花费的时间、消耗的资源


l = [-5, -3, -1, 0, 2, 4, 6, 8, 9, 11, 13]
l = [6, 8, 9, 11, 13]
l = [6, 8]
l = [8]
l = []  # 结束递归调用
# for i in l:
#     if i == 8:
#         print('找到了')
#         break
l.sort()





