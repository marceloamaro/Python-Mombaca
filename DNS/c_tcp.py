#cliente​
from socket import *
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 65432
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((HOST, PORT))
while 1:
    msg = input("Digite: ")
    cli.send(msg.encode())