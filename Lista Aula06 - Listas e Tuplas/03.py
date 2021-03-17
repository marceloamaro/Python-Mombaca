"""Escreva uma função que receba uma lista com itens repetidos e retorne a mesma lista com itens únicos"""

lista = [1,1,2,5,9,0,2,0,10,5,3,4,3,10]

def repetidos(lista):
    lista = set(lista)
    print(lista)

repetidos(lista)