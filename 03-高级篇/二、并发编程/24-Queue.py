# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import queue
from multiprocessing import Queue


# 先进先出Queue
# q = queue.Queue()
# q.put()
# q.get()
# q.get(timeout=3)
# q.get_nowait()
# q.put_nowait()
# q.full()
# q.empty()


# 后进先出Queue
# q = queue.LifoQueue()   # last in first out
# q.put('a')
# q.put('b')
# q.put('c')
# print(q.get())


# 优先级Queue
q = queue.PriorityQueue()
q.put((18, 'a'))
q.put((69, 'b'))
q.put((36, 'c'))
q.put((-1, 'd',))
print(q.get())
print(q.get())
