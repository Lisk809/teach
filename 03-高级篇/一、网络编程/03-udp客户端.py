# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 流式协议（tcp协议）

# 3、传输数据

sk.sendto(b'hello', ('127.0.0.1', 5004))
sk.sendto(b'abc', ('127.0.0.1', 5004))

# 4、关闭连接
sk.close()

