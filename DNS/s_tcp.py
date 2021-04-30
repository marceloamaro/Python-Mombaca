#servidor​  
from socket import *
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 65432
print(f'HOST: {HOST} , PORT {PORT}')
serv = socket(AF_INET, SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)
while 1:
    con, adr = serv.accept()
    while 1:
        msg = con.recv(1024)
        print(msg.decode())