"""
Escreva uma função para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um
fumante perde 10 minutos de vida a cada cigarro, a função deverá retornar quantos dias de vida
um fumante perderá. Exiba o total em dia.
"""
qnt_Cigarros = int(input("Qnts cigarros por dia: "))
anos_Fumando = int(input("Anos fumando: "))

def dias_Perdidos(qnt_Cigarros,anos_Fumando):
    return (((anos_Fumando * 365)*qnt_Cigarros )* 10)/24


print ("dias perdidos: ", dias_Perdidos(qnt_Cigarros,anos_Fumando) )