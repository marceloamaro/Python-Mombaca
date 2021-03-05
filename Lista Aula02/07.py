"""
Escreva uma função que receba a idade do usuário e indique se ele pode ou não encher a
cara de cachaça
"""


def result(idade):
    if idade < 18:
        print('Você é de Menor, vai tomar leite')
    elif idade >= 18 and idade < 45:
        print('Você é de Maior, Pode encher a cara de caçacha')
    elif idade >= 45 and idade <= 80:
        print('Cuidado com cirrose, Mas pode encher a cara de caçacha')
    else:
        print('se tu tiver vivo!, puder bebe')

idade = int(input("qual sua idade?"))
x = result(idade)