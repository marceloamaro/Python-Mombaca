"""
Escreva uma função que simule o funcionamento de um radar eletrônico. Essa função deve receber a velocidade do carro de um usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 90 reais pela infração + R$ 5 reais por km acima de 80 km/h
"""
velocidade = float(input("Qual a velocidade Atual do carro em km/h-->"))

if velocidade > 80:
    print("MULTADO, Voce execedeu o limite permitido de 80km/h")
    multa = 90 +((velocidade - 80)*5)
    print("o Valor da multa é de R${:.2f}!".format(multa) )
print("tenha um bom dia, Dirigia com segurança")