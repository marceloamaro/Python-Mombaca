"""
Escreva uma função que receba a idade do usuário e indique se ele pode ou não encher a
cara de cachaça
"""

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você é de Menor, vai tomar leite')
elif idade >= 18 and idade < 45:
    print('Você é de Maior, Pode encher a cara de caçacha')
elif idade >= 45 and idade <= 80:
    print('Cuidado com cirrose, Mas pode encher a cara de caçacha')
else:
    print('se tu tiver ainda vivo!, puder bebe')
    """
idade = int(input('Digite sua idade: '))

def pinga(idade):
    if idade < 18:
        return print('Você é de Menor, vai tomar leite')
    elif idade >= 18 and idade < 45:
        return print('Você é de Maior, Pode encher a cara de caçacha')   
    elif idade >= 45 and idade <= 80:
        return print('Cuidado com cirrose, Mas pode encher a cara de caçacha')
    else:
        return print('se tu tiver ainda vivo!, puder bebe')

   """   