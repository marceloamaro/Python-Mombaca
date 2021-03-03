"""
Escreva uma função que receba como argumento a quantidade de Km percorridos por um
carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. A
função deve retornar o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15
por km rodado R$.
"""
km_p = int(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

def valor(km_p,dias):
    return (km_p*0.15 + dias*60) 

print ( "Valor do aluguel: R$ ", valor(km_p,dias))
