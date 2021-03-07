"""
Gere as seguintes listas utilizando for e o metodo range():
    • Uma lista de ímpares de 10 a 12o
    • Uma lista pares de 2 a 1000
    • Uma lista de multiplos de 2 em um intervalo de decrescente de 100 até 40
    • Uma lista de primos de 44 até 99
OBS: Pesquise pelo método append() na documentação
"""
multiplo = [] 
for i in range (40, 101):
    if i % 2 == 0:
            multiplo.append(i)
    print("numeros multiplo de 2:", multiplo))
