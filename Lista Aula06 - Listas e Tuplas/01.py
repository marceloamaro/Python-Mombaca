"""Faça uma função que receba duas listas e que gere uma terceira com os elementos das duas primeiras. """
"""
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]


soma = list(map(lambda x, y: (x + y), lista1, lista2))

print(soma)   

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]
for i in range(len(lista2)):
    lista1.append(lista2[i])
print(lista1) 
"""
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]


def lista_final(lista1,lista2):
    lista3 = []
    lista3.extend(lista1)
    lista3.extend(lista2)
    print(f"{lista3}")

lista_final(lista1,lista2)