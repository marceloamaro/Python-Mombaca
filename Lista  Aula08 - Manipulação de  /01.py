"""Crie um arquivo que contenha todos os números de de 2 a 1000: A partir desse arquivo gerado faça o que se pede:
    • Gere um arquivo apenas com múltiplos de 2
    • Inverta a ordem do arquivo de múltiplos de 2
    • Gere um arquivo com ímpares maiores que 10 e menores que 800
    • Gere um arquivo somente com números primos
    • Gere 3 arquivos, sendo (divisores de 2, 3 e 5) """
"""
arquivo = open("numero.txt", "w") 

for linha in range(2, 1000):
  arquivo.write(f"{linha}\n")
arquivo.close()

#Gere um arquivo apenas com múltiplos de 2
with open("multiplos_dois.txt", "w") as multiplos2:
    with open("numero.txt") as linha:
        for l in linha.readlines():
            if int(l) % 2 == 0:
                multiplos2.write(l)

#Inverta a ordem do arquivo de múltiplos de 2
with open("numReverse.txt", "w") as numReverse:
    with open("multiplos_dois.txt") as multiplos2:
        for l in multiplos2.readlines():
            numReverse.reverse() 
            numReverse.write(l)

#Gere um arquivo com ímpares maiores que 10 e menores que 800
with open("impares_dois.txt", "w") as impares2:
    with open("numero.txt") as linha:
        for l in linha.readlines():
            if int(l) >= 10 and int(l) <= 800 : 
                if int(l) % 2 != 0:
                    impares2.write(l)    
"""            

#Gere um arquivo somente com números primos
