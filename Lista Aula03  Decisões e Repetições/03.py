"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200 km, e R$ 0.45 para viagens mais longas.
"""
distancia = float(input("Qual a distância da sua viagem em km-->"))

def valor(distancia):
    if distancia > 200:
        return distancia * 0.45
    else: 
        return distancia * 0.50

x = valor(distancia) 
print("o Valor da sua viagem é de R${:.2f}!".format(x) ) 