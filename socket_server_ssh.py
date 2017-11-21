import os
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print('new conn:',addr)
    while True:
        print('等待新指令')
        data = conn.recv(1024)
        print(data)
        if not data:
            print('客户端已断开')
            break
        cmd_send = os.popen(data.decode()).read()
        if len(cmd_send) == 0:
            cmd_send = b'cmd_send is null'
        try:
            conn.send(str(len(cmd_send.encode('utf-8'))).encode('utf-8'))
            client_ack = conn.recv(1024)#解决粘包问题
            print('客户端已收到',client_ack.decode())
            conn.send(cmd_send.encode('utf-8'))
        except AttributeError as e:
            conn.send(b'No found command')



