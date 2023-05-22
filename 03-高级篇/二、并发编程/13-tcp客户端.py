# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket
import time


c = socket.socket()
c.connect(('127.0.0.1', 8002))
while True:
    c.send(b'hello')
    data = c.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)


