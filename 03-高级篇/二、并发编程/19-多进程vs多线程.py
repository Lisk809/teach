# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# # 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import time
#
#
# def task():
#     res = 0
#     for i in range(10000000):
#         res += i
#
#
# if __name__ == '__main__':
#     l = []
#     start = time.time()
#     for i in range(10):
#         # p = Process(target=task)    # 花费时间： 0.7160739898681641
#         p = Thread(target=task)    # 花费时间： 5.394115924835205
#         p.start()
#         l.append(p)
#     for p in l:
#         p.join()
#     end = time.time()
#     print('花费时间：', end - start)


# IO密集型
from multiprocessing import Process
from threading import Thread
import time


def task():
    time.sleep(1)


if __name__ == '__main__':
    l = []
    start = time.time()
    for i in range(4000):
        # p = Process(target=task)    # 花费时间： 19.719253063201904
        p = Thread(target=task)    # 花费时间： 1.9106950759887695
        p.start()
        l.append(p)
    for p in l:
        p.join()
    end = time.time()
    print('花费时间：', end - start)
