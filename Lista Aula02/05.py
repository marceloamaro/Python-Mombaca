km_p = int(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

def valor(km_p,dias):
    return (km_p*0.15 + dias*60) 

print ( "Valor do aluguel: R$ ", valor(km_p,dias))
