"""Escreva as seguintes funções lambda.

Uma função que receba um nome e retorne o seu equivalente maiúsculo
Uma função que receba dois parâmetros e retorne o primeiro elevado ao segundo
Uma função que receba um dado e retorne seu tipo
A questão 9 e 14 da lista 2 """

palavra = input("Digite uma palavra: ")

conv = lambda palavra: palavra.upper
print(palavra.upper())

n1 = int(input("digite o 1 numero:"))
n2 = int(input("digite o 2 numero:"))

elevação = lambda n1, n2 : n1**n2
print("o primeiro elevado ao segundo é:", elevação(n1, n2))

