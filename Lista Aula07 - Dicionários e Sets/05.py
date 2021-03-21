"""Utilizando o dicionário criado na questão anterior faça: Uma função que retorne apenas os valores pares do dicionario da questão anterior Uma função que retorne apenasas chaves vogais do dicionário da questão anterior """

nome="marcelo"

def estrutura(nome):
    dic = {x : [x for x in range(7) ] for x in nome}   
    print("\n", dic) 
estrutura(nome) 

def vogais(nome):
    i = 0
    j = 0
    for i in nome:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
            j+=1
    print("\n vogais:\n ", j)
vogais(nome)

def numeros(nome):
    b = {x : [x for x in range(7) if x %2 == 0 ] for x in nome}
    print("\n",b)

numeros(nome)