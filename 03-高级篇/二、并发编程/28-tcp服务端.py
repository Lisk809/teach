# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


from gevent import monkey;monkey.patch_all()
import socket
from gevent import spawn


def comm(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except:
            break
    conn.close()


def run(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        spawn(comm, conn)


if __name__ == '__main__':
    # run('127.0.0.1', 8001)
    g = spawn(run, '127.0.0.1', 8002)
    g.join()


# 在多进程下面创建多线程
# 多线程下面创建协程
