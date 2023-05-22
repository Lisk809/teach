# coding: utf-8
# @Author: 小飞有点东西


# 有名函数(需要重复调用)
# def func(x, y):
#     return x + y

# 匿名函数(临时调用一次)
# res = (lambda x, y=1: x + y)(1)
# print(res)

# func = lambda x, y=1: x + y
# res = func(1)
# print(res)


# lambda x, y=1: x + y


# info = {
#     'jack': 5000,
#     'tony': 2500,
#     'andy': 8000,
#     'amy': 6000,
#     'lucy': 11000
# }


# def func(k):
#     return info[k]


# res = max(info, key=lambda k: info[k])
# print(res)
#
# res = min(info, key=lambda k: info[k])
# print(res)


# l = [3, 1, 4, 5, 9, 2, 6]
# l.sort(reverse=True)
# l = [(1, 2), (3, 4), (2, 1), (4, 3)]
# l.sort(key=lambda item: item[1])
# print(l)
# sorted()


# l = ['康师傅', '统一', '大今野', '白象']
# new_l = (name+'_老坛酸菜' for name in l)
# print(new_l)
#
# res = map(lambda name: name+'_老坛酸菜', l)
# print(res)
# print(res.__next__())

# python是一门解释型的强类型动态语言
# 1、编译型or解释型
# 2、强类型or弱类型
# 3、动态型or静态型

# 函数参数的类型提示（3.5以后）
def func(name: str, age: int=88) -> int:
   print(name)
   print(age)
   return 10


# func(3.14, [1, 2, 3])
print(func.__annotations__)















