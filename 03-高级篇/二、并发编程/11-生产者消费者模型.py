# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from multiprocessing import Process, Queue, JoinableQueue
import time
import random

'''
JoinableQueue
在Queue的基础上多了一个计数器机制，每put一个数据，计数器就加一
每调用一次task_done，计数器就减一
当计数器为0的时候，就会走q.join后面的代码
'''


def producer(name, food, q):
    for i in range(8):
        time.sleep(random.randint(1, 3))
        print(f'{name}生产了{food}{i}')
        q.put(f'{food}{i}')


def consumer(name, q):
    while True:
        food = q.get()
        time.sleep(random.randint(1, 3))
        print(f'{name}吃了{food}')
        # if food == '鹤顶红':
        #     break
        q.task_done()   # 告诉队列，已经拿走了一个数据，并且已经处理完了


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=('中华小当家', '黄金炒饭', q))
    p2 = Process(target=producer, args=('神厨小福贵', '佛跳墙', q))
    c1 = Process(target=consumer, args=('八戒', q))
    c2 = Process(target=consumer, args=('悟空', q))
    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    # q.put('鹤顶红')
    # q.put('鹤顶红')

    q.join()    # 等待队列中所有的数据被取完，计数器变成0
    # 主进程死了，消费者也要跟着陪葬，守护进程






