# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from multiprocessing import Process, Queue


def task1(q):
    q.put('宫爆鸡丁')


def task2(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=task1, args=(q,))
    p2 = Process(target=task2, args=(q,))
    p1.start()
    p2.start()

    # print(q.get())






