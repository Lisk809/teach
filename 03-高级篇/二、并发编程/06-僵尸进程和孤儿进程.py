# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from multiprocessing import Process
import time


def task():
    print('任务开始')
    time.sleep(5)
    print('任务结束')


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print('主进程')

