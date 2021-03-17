"""Escreva uma função que receba uma lista de vários inteiros e retorne um único inteiro composto por todos os itens da lista informada."""

s = '0,1,2,3,4,5,6,7,8,9,10,11,15,100,111'
digits = []
for symbol in s:
    if '12345'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
