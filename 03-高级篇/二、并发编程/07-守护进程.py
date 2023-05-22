# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from multiprocessing import Process
import time


def task(name):
    print(f'{name}还活着')
    time.sleep(5)
    print(f'{name}正常死亡')


if __name__ == '__main__':
    p = Process(target=task, kwargs={'name': '苏妲己'})
    p.daemon = True
    p.start()
    time.sleep(1)
    print('纣王驾崩了')

