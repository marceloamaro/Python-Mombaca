"""
2 ​ - Escreva uma função que receba dois números como argumento e retorne a
metade do quádruplo do primeiro dividida pelo quadrado do segundo
"""
print('Digite primeiro numero:')
num1 = int(input())
print('Digite segundo numero:')
num2 = int(input())

def quadruplo_divisao(num1):
    return (num1 **4)/2

def quadrado(num2):
    return num2 **2

def produto(quadruplo_divisao, quadrado):
    return ((num1 **4)/2) / num2 **2

x = produto(quadruplo_divisao, quadrado)
print("o resultado:")
print(x)