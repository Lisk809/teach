# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket


client = socket.socket()
client.connect(('127.0.0.1', 8080))

while True:
    input()
    client.send(b'hello')
    data = client.recv(1024)
    print(data)




