"""Faça o mesmo que que se pede na questão anterior, mas a terceira lista não pode ter itens repetidos. """

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8, 9]


def lista_final(lista1,lista2):
    lista3 = []
    lista3.extend(lista1)
    lista3.extend(lista2)
    lista3 = set(lista3)
    print(f"{lista3}")

lista_final(lista1,lista2)