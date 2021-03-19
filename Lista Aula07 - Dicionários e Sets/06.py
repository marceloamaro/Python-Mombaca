"""Escreva uma função que receba como argumento uma lista e uma tupla e retorne um set composto pelas duas coleções."""

lista = [1, 2, 3, 4]
tupla = (5, 6, 7, 8)

def uniao(lista, tupla):
    set1 = set(lista)
    set2 = set(tupla)
    print("lista convertida em set->", set1)
    print("tupla convertida em set->", set2)
    print("A união dos dois set->", set1  | set2)
uniao(lista, tupla)   