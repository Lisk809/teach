# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA
# pid号（进程号）

from multiprocessing import Process, current_process
import time
import os


def task(name='子进程'):
    # print(f'任务{current_process().pid}执行中')
    print(f'{name}{os.getpid()}执行中')
    print(f'{name}的父进程{os.getppid()}执行中')
    # time.sleep(100)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()   # 杀死当前进程（win: taskkill pid,  mac/linux: kill -9 pid)
    time.sleep(0.001)
    print(p.is_alive())
    print('主进程')
    # task('主进程')
