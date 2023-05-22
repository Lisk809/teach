# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from threading import Thread, Semaphore
import time
import random


sp = Semaphore(5)


def task(name):
    sp.acquire()
    print(name, '抢到车位')
    time.sleep(random.randint(3, 5))
    sp.release()


if __name__ == '__main__':
    for i in range(25):
        t = Thread(target=task, args=(f'宝马{i+1}号',))
        t.start()


