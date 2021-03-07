"""
Gere as seguintes listas utilizando for e o metodo range():
    • Uma lista de ímpares de 10 a 12o
    • Uma lista pares de 2 a 1000
    • Uma lista de multiplos de 2 em um intervalo de decrescente de 100 até 40
    • Uma lista de primos de 44 até 99
OBS: Pesquise pelo método append() na documentação
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