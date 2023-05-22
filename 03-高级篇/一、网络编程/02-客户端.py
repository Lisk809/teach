# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 流式协议（tcp协议）

# 2、建连接
sk.connect(('127.0.0.1', 5004))

# 3、传输数据
while True:
    msg = input('请输入>>>').strip()
    sk.send(msg.encode('utf-8'))
    if not msg:
        continue
    if msg == 'q':
        break

    data = sk.recv(1024)
    print(data.decode('utf-8'))

# 4、关闭连接
sk.close()

