qnt_Cigarros = int(input("Qnts cigarros por dia: "))
anos_Fumando = int(input("Anos fumando: "))

def dias_Perdidos(qnt_Cigarros,anos_Fumando):
    return (((anos_Fumando * 365)*qnt_Cigarros )* 10)/24


print ("dias perdidos: ", dias_Perdidos(qnt_Cigarros,anos_Fumando) )