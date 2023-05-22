# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socketserver


class RequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)        # self.request => conn
        print(self.client_address)
        # 5、数据传输
        while True:
            try:
                data = self.request.recv(1024)
            except:
                break
            if not data:
                break
            data = data.decode('utf-8')
            print('客户端发过来的数据：', data)

            self.request.send(data.upper().encode('utf-8'))

        # 6、结束服务
        self.request.close()



sk = socketserver.ThreadingTCPServer(('127.0.0.1', 5001), RequestHandle)
sk.serve_forever()
# ==
# while True:
#     conn, addr = sk.accept()
#     起一个线程(conn, addr)


# sk.close()  # 可选




