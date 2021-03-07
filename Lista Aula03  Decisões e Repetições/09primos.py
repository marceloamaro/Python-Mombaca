"""
Gere as seguintes listas utilizando for e o metodo range():
    • Uma lista de ímpares de 10 a 12o
    • Uma lista pares de 2 a 1000
    • Uma lista de multiplos de 2 em um intervalo de decrescente de 100 até 40
    • Uma lista de primos de 44 até 99
OBS: Pesquise pelo método append() na documentação
"""
"""
primos = []
divisores = 0
for divisores in range(1, 10):
    if primos % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
                primos.append(i)
print("numeros primos", primos)  
"""
"""
lista_numeros = [x for x in range(100)]

lista_primos = list()

lista_divisores = [x for x in lista_numeros if x != 0]

for number in lista_numeros: 

    soma_divisores = 0 

    for divisor in lista_divisores:

        if number % divisor == 0: 
            soma_divisores += 1
        
        elif number < divisor:
            break

    if soma_divisores == 2: 
        lista_primos.append(number)

print(lista_primos)
"""
lista_primos = []

for x in range(44,100):
    cont=0

    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
            lista_primos.append(x)

print(lista_primos)