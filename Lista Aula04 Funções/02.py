"""No Basquete os lances podem valer três pontuações diferentes. Finalização dentro do garrafão(2 pontos), finalização fora do garrafão (3 pontos), cobrança de falta(1 ponto). Faça uma função que receba a quantidade de finalização de cada tipo e retorne quantos pontos no total o time fez. Já que os valores dos pontos são fixos, utilize parâmetros opcionais. Construa outra função que recebe os mesmos dados equivalente ao time adversário, e em seguida crie uma terceira função que receba a primeira e a segunda como parâmetro e retorne o time vencedor"""
print("Time da Casa")
pto_d = int(input("entre com o número de Finalização dentro do garrafão:"))
pto_f = int(input("entre com o número de Finalização fora do garrafão:"))
pto_cf = int(input("entre com o número de cobrança de falta:"))
print("Time Visitante")
v_pto_d = int(input("entre com o número de Finalização dentro do garrafão:"))
v_pto_f = int(input("entre com o número de Finalização fora do garrafão:"))
v_pto_cf = int(input("entre com o número de cobrança de falta:")) 

def placa_csa(pto_d, pto_f, pto_cf):
    return (pto_d * 2)+(pto_f * 3)+(pto_cf * 1)
print("Pontuação do Time da Casa")  
print(placa_csa(pto_d, pto_f, pto_cf))    

def placa_visit(v_pto_d, v_pto_f, v_pto_cf):
    return (v_pto_d * 2)+(v_pto_f * 3)+(v_pto_cf * 1) 
print("Pontuação do Time da Visitante")  
print(placa_visit(v_pto_d, v_pto_f, v_pto_cf))

def placa(placa_visit, placa_csa):
    
    if placa_csa > placa_visit:
        print("Time da Casa Vencedor!!!") 
    else: 
        print("Time Visitante vencedor ")      
         
placa(placa_visit(v_pto_d, v_pto_f, v_pto_cf), placa_csa(pto_d, pto_f,pto_cf))