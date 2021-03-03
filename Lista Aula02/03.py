"""
2 - Escreva uma função que receba dois números como argumento e retorne o produto do dobro
do primeiro pelo triplo do segundo
3 - Crie uma função que retorne o resto da divisão do resultado da função da questão anterior
por 2
"""
print('Digite primeiro numero')
num1 = int(input())
print('Digite segundo numero')
num2 = int(input())

def dobro(num1):
    return num1 *2

def triplo(num2):
    return num2 *3

def resto( num1,num2):
    return (num1 *2)%(num2 *3)

#print("o dobro do primeiro", dobro(num1))
#print("o triplo do segundo",triplo(num2))
print("o resto da divisao dos dois numeros",resto(num1,num2))