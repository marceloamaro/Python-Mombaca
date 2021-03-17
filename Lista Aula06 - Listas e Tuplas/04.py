"""Faça uma função que receba uma lista e 3 números, esses números devem ser índices válidos dessa lista. A função deve retornar uma tupla composta pelos valores dos índices indicados. """
def tranformar(lista): 
    return tuple(lista) 
   
lista = [7, 20, 24] 
tranformar(lista)
print(tranformar(lista)) 