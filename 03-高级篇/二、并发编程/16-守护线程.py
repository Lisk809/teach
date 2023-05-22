# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


"""
主线程运行完毕之后，它不会立刻结束，要等待所有子线程运行完毕之后才会结束；
因为主线程结束，就意味着主线程所在的进程结束了
"""

# from threading import Thread
# import time
#
#
# def task(name):
#     print(f'{name} 还活着')
#     time.sleep(3)
#     print(f'{name} 正常死亡')
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('妲己',))
#     t.daemon = True
#     t.start()
#     print('纣王驾崩了')


# 例子：
from threading import Thread
import time


def f1():
    print('任务1开始')
    time.sleep(3)
    print('任务1结束')


def f2():
    print('任务2开始')
    time.sleep(2)
    print('任务2结束')


if __name__ == '__main__':
    t1 = Thread(target=f1)
    t2 = Thread(target=f2)
    t1.daemon = True
    t1.start()
    t2.start()
    print('主线程')

