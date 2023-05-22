# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# 死锁
from threading import Thread, Lock, current_thread, RLock
import time


mutex1 = Lock()
mutex2 = Lock()


def task():

    mutex1.acquire()
    print(current_thread().name, '抢到锁1')
    mutex2.acquire()
    print(current_thread().name, '抢到锁2')
    mutex2.release()
    mutex1.release()
    task2()


def task2():
    mutex2.acquire()
    print(current_thread().name, '抢到锁2')
    time.sleep(1)
    mutex1.acquire()
    print(current_thread().name, '抢到锁1')
    mutex1.release()
    mutex2.release()


if __name__ == '__main__':
    for i in range(8):
        t = Thread(target=task)
        t.start()


