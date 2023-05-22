# coding: utf-8
# @Author: 小飞有点东西
# 资料下载：https://active.clewm.net/FrcyFA


import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 流式协议（tcp协议）

# 2、绑定地址
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 5004))

# 3、监听连接请求（开始营业）
sk.listen(5)    # 5：半连接池大小
print('服务端启动成功，在5001端口等待客户端连接')

# 4、取出连接请求，开始服务

# 持续提供服务，并发提供服务
while True:
    conn, addr = sk.accept()
    print('客户端ip+端口：', addr)

    # 5、数据传输
    while True:
        try:
            data = conn.recv(1024)
        except:
            break
        if not data:
            break
        data = data.decode('utf-8')
        print('客户端发过来的数据：', data)

        conn.send(data.upper().encode('utf-8'))

    # 6、结束服务
    conn.close()

# sk.close()  # 可选




