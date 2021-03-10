"""
9 -​ Um fazendeiro cria Galinhas, Vacas e Porcos, Cavalos, Girafas, sim ele é um
fazendeiro ousado. Escreva uma função que receba a quantidade de cada animal
que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda.
"""
print("calcula quantas patas que tem atuamente na fazenda")
galinhas = int(input('Digite quantas galinhas que tem atualmente na fazenda: '))
vacas = int(input('Digite quantas vacas que tem atualmente na fazenda: '))
porcos = int(input('Digite quantos porcos que tem atualmente na fazenda: '))
cavalos = int(input('Digite quantas Cavalos que tem atualmente na fazenda: '))
girafas = int(input('Digite quantas Girafas que tem atualmente na fazenda: '))

def patas (galinhas, vacas, porcos, cavalos, girafas):
    return ((galinhas * 2)+(vacas * 4)+(porcos * 4)+(cavalos*4)+(girafas*4))


print(" A quantidade de patas na fazenda sao:", patas (galinhas, vacas, porcos, cavalos, girafas))