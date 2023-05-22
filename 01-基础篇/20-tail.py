# coding: utf-8
# @Author: 小飞有点东西

import time

with open('data/user.log', mode='rb')as f:
    # 1、控制文件指针跳到末尾
    # f.read()    #不可取
    f.seek(0, 2)
    while True:
        res = f.readline()
        if res:
            print(res.decode('utf-8'), end='')
        time.sleep(0.2)
