"""Escreva uma função que receba uma string e converta as letras em seus respectivos números posicionais no alfabeto: Por exemplo (a = 1, b =2, c =3). """

input = input('Escreva qualquer coisa: ')
input = input.lower()
output = []
def troca(output):
    for caracteres in input:
        numero = ord(caracteres) - 96
        output.append(numero)
        
troca(output)
print (output)
