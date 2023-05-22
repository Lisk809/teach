# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA
import time
from threading import Thread, current_thread, active_count
import os


age = 18


def task():
    # print('子线程', os.getpid())
    # global age
    # age = 16
    print(current_thread().name)
    time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    # print('主线程', os.getpid())
    # print(age)
    print('当前线程的名字', current_thread().name)
    print('进程中活跃的线程数量', active_count())
