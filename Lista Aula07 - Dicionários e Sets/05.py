"""Utilizando o dicionário criado na questão anterior faça: Uma função que retorne apenas os valores pares do dicionario da questão anterior Uma função que retorne apenasas chaves vogais do dicionário da questão anterior """

nome="marcelo"

def estrutura(nome):
    dic = {x : [x for x in range(7) ] for x in nome}   
    print("\n", dic) 
estrutura(nome) 

lista_vogais=['a','e','i','o','u','A','E','I','O','U']
def vogais(nome,lista_vogais):
    for i in nome:
        if i in lista_vogais:
            print(i)

vogais(nome,lista_vogais)

def numeros(nome):
    b = {x : [x for x in range(7) if x %2 == 0 ] for x in nome}
    print("\n",b)

numeros(nome)