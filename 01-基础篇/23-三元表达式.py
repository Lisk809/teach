# coding: utf-8
# @Author: 小飞有点东西


# 三元表达式: 条件成立时返回的值 if 条件 else 条件不成立时返回的值
def func(x, y):
    if x > y:
        return x
    else:
        return y


x = 6
y = 9
res = func(x, y)
print(res)


def a():
    return 10


def b():
    return 20


res = a() if x > y else b()
print(res)





