# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socketserver
import time


class RequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print('客户端发来的数据：', self.request[0])
        time.sleep(int(self.request[0]))
        self.request[1].sendto(self.request[0].upper(), self.client_address)


sk = socketserver.ThreadingUDPServer(('127.0.0.1', 5006), RequestHandle)
sk.serve_forever()


