
import socket
import sys

HOST = '127.0.0.1'  # localhost = esta máquina
PORT = 9999           # portas abaixo de 1023 exigem permissão de root

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5)

print('aguardando conexoes em ', PORT)
conn, addr = s.accept()

print('recebi uma conexao de ', addr)

#--------------------------
# insira aqui o codigo para tratar uma conexao
#--------------------------

print('o cliente encerrou')
conn.close()