import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9999))

while True:
    try:
        cmd = input('>>:').strip()
        if len(cmd) == 0:continue
        client.send(cmd.encode('utf-8'))
        recv_data = client.recv(1024)
        print('recv_size:',recv_data.decode())
        client.send('准备好接受了'.encode('utf-8'))
        result_size = 0
        result_data = b''
        while result_size < int(recv_data.decode()):
            data = client.recv(1024)
            result_size += len(data)
            result_data += data
        else:
            print(result_data.decode())
            print('data done',result_size)
    except ValueError as e:
        pass
