qnt_Cigarros = int(input("Qnts cigarros por dia: "))
anos_Fumando = int(input("Anos fumando: "))

total_Cigarros = (anos_Fumando * 365)*qnt_Cigarros
dias_Perdidos = (total_Cigarros * 10)/24

print ('%d dias perdidos ' %dias_Perdidos )