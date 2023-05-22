# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket
import select

# select.poll
# select.epoll

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)
server.setblocking(False)

input_list = [server]
while True:
    rlist, wlist, xlist = select.select(input_list, [], [])
    print(rlist)
    for i in rlist:
        # 判断，对不同的对象做不同的处理
        if i is server:
            conn, addr = i.accept()
            input_list.append(conn)
            continue

        try:
            data = i.recv(1024)
            if not data:
                i.close()
                input_list.remove(i)
                continue
            i.send(data.upper())
        except ConnectionResetError:
            i.close()
            input_list.remove(i)
            continue



