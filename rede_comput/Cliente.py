#!/usr/bin/env python3
import socket


HOST = '127.0.0.1'  # localhost = esta máquina
PORT = 65432          # portas abaixo de 1023 exigem permissão de root

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello, word')
    data = s.recv(1024)
    
print('Received', repr(data))    