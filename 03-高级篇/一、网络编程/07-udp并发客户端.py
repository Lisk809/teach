# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 流式协议（tcp协议）

# 3、传输数据
while True:
    msg = input('请输入>>>').strip()
    sk.sendto(msg.encode('utf-8'), ('127.0.0.1', 5006))
    data, addr = sk.recvfrom(1024)
    print(data.decode('utf-8'))

# 4、关闭连接
sk.close()

