# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket
import selectors


def accept(server):
    conn, addr = server.accept()
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn):
    try:
        data = conn.recv(1024)
        if not data:
            conn.close()
            sel.unregister(conn)
            return
        conn.send(data.upper())
    except ConnectionResetError:
        conn.close()
        sel.unregister(conn)
        return


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)
server.setblocking(False)

sel = selectors.DefaultSelector()
sel.register(server, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj)
