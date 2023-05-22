# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 数据报协议（udp协议）

# 2、绑定地址
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 5004))

# 5、数据传输

data, addr = sk.recvfrom(3)
print('客户端发过来的数据：', data)

data, addr = sk.recvfrom(2)
print('客户端发过来的数据：', data)

# sk.close()  # 可选

# 1472 Byte
# 512 Byte

# dns
# udp


