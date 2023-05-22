# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


# import queue
# queue.Queue()

# from multiprocessing import queues
# queues.Queue()

from multiprocessing import Queue


q = Queue(6)
q.put('a')
q.put('b')
q.put('c')
q.put('d')
# print(q.full())
# print(q.empty())
q.put('e')
q.put('f')
# q.put('g', timeout=3)
# q.put_nowait('g')
# print(q.full())

v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
v6 = q.get()
# v7 = q.get(timeout=3)
# q.get_nowait()
print(v1, v2, v3, v4, v5, v6)

print(q.empty())

"""
q.put()
q.get()

再多进程的条件下不够准确
q.put_nowait()
q.get_nowait()
q.full()
q.empty()
"""



