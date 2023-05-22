# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from multiprocessing import Process


age = 18


def func():
    global age
    age = 16


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.join()
    print(age)


