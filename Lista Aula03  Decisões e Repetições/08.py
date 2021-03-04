"""
Faça uma função que receba uma lista de números inteiros e retorne o maior elemento desta lista. Utilize o for
"""
lista = []
for i in range(0, 10):
    lista.append(int(input(f"digite um valor para prosição {i}:")))

print(f"Voce digitou os valores da {lista}")
print ("O maior elemento: ", max(lista))