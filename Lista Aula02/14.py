"""
Um fazendeiro cria Galinhas, Vacas e Porcos. Escreva uma função que receba a quantidade
de cada animal que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda.
"""
print("calcula quantas patas tem na fazenda")
galinhas = int(input('Digite quantas galinhas tem na fazenda: '))
vacas = int(input('Digite quantas vacas tem na fazenda: '))
porcos = int(input('Digite quantos porcos tem na fazenda: '))


def patas (galinhas, vacas, porcos):
    return ((galinhas * 2)+(vacas * 4)+(porcos * 4))


print(" A quantidade de patas na fazenda sao:", patas (galinhas, vacas, porcos))