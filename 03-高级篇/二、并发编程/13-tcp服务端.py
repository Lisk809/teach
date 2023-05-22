# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket
from multiprocessing import Process
from threading import Thread


s = socket.socket()
s.bind(('127.0.0.1', 8002))
s.listen(5)


def task(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
        except:
            break
        if not data:
            break
        print(data.decode('utf-8'))
        conn.send(data.upper())
    conn.close()


if __name__ == '__main__':

    while True:
        conn, addr = s.accept()
        # p = Process(target=task, args=(conn,))
        p = Thread(target=task, args=(conn,))
        p.start()



