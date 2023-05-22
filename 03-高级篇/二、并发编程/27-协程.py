# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA

import time

# 计算密集型
# 串行执行：1.1131649017333984
# def f1():
#     n = 0
#     for i in range(10000000):
#         n += i
#
#
# def f2():
#     n = 0
#     for i in range(10000000):
#         n += i
#
#
# start = time.time()
# f1()
# f2()
# end = time.time()
# print(end - start)

# 切换：1.8425521850585938
# def f1():
#     n = 0
#     for i in range(10000000):
#         n += i
#         yield
#
#
# def f2():
#     g = f1()
#     n = 0
#     for i in range(10000000):
#         n += i
#         next(g)
#
#
# start = time.time()
# f2()
# end = time.time()
# print(end - start)


# IO密集型
from gevent import monkey
monkey.patch_all()
from gevent import spawn
import time


def da():
    for _ in range(3):
        print('哒')
        time.sleep(2)


def mie():
    for _ in range(3):
        print('咩')
        time.sleep(2)


def buyao():
    for _ in range(3):
        print('不要')
        time.sleep(3)


start = time.time()
g1 = spawn(da)
g2 = spawn(mie)
g3 = spawn(buyao)
g1.join()
g2.join()
g3.join()
end = time.time()
# print(end - start)  # 12.029063940048218
print(end - start)  # 6.019258975982666
print(end - start)  # 9.015071868896484



