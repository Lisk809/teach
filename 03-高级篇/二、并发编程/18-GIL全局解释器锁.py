# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA

from threading import Thread, Lock
# from multiprocessing import Lock
import time

num = 180
mutex = Lock()


def task():
    global num

    # mutex.acquire()
    with mutex:
        temp = num
        time.sleep(0.05)
        num = temp - 1
    # mutex.release()


if __name__ == '__main__':
    l = []
    for i in range(180):
        t = Thread(target=task)
        t.start()
        l.append(t)

    for t in l:
        t.join()

    print(num)
