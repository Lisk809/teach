# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# 方式一
from multiprocessing import Process
from threading import Thread
import time


def task(name):
    print(f'{name} 任务开始')
    time.sleep(3)
    print(f'{name} 任务结束')


if __name__ == '__main__':
    t = Thread(target=task, args=('悟空',))
    t.start()
    t.join()
    print('主线程')



