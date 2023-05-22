# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    cmd = input('请输入终端命令>>>').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 先拿到总长度
    data_size = int(client.recv(8).decode('utf-8'))
    recv_size = 0
    data = b''
    while recv_size < data_size:
        res = client.recv(1024)
        recv_size += len(res)
        data += res
    print(data.decode('utf-8'))
    print(len(data))

