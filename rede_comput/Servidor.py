#!/usr/bin/env python3
import socket


HOST = '127.0.0.1'  # localhost = esta máquina
PORT = 65432          # portas abaixo de 1023 exigem permissão de root

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen
    conn,addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)