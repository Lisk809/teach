# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os


# pool = ThreadPoolExecutor(10)  # 不传参的话，默认开设的线程数量，是当前cpu的个数乘以5
pool = ProcessPoolExecutor(3)  # 不传参的话，默认开设的进程数量，是当前cpu的个数


def task(name):
    print(name, os.getpid())
    time.sleep(3)
    return name + 10


def call_back(res):
    print('call_back', res.result())


if __name__ == '__main__':
    # f_list = []
    for i in range(50):
        # future = pool.submit(task, i)  # 往线程池中提交任务
        pool.submit(task, i).add_done_callback(call_back)  # 往线程池中提交任务
        # f_list.append(future)

    # pool.shutdown()  # 关闭线程池，等待线程池中所有任务运行完毕
    # for f in f_list:
    #     print('任务结果：', f.result())


# 信号量：锁，线程自己创建，控制线程执行，阻塞
# 线程池：线程由线程池创建，控制线程数量
