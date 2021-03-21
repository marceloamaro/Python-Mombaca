"""Utilizando dic conprehension e list comprehension construa uma função que gere o seguinte dicionário: O dicionario deve ter como chave as letras de um nome inserido como argumento e como valor uma lista de pares dentro de um range, passado também como argumento """

nome="marcelo"

def estrutura(nome):
    dic = {x : [x for x in range(7) ] for x in nome}   
    print(dic) 
estrutura(nome)    
