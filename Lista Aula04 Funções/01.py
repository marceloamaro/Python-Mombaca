"""Escreva três funções sendo que: A Primeira deve receber uma quantidade de dias e retornar o equivalente em horas. A segunda deve receber a quantidade de horas retornada pela primeira função e retornar o equivalente em minutos, a terceira por sua vez recebe a quantidade de minutos da segunda e retorna o equivalente em segundos. Utilize as funções como parâmetros"""

dia = int(input("Por favor, entre com o número de dias que deseja converter:"))

def dia_hora(dia):
    return dia*24
def hora_minuto(dia_hora):
    return dia_hora*60
def minuto_segundo(hora_minuto):
    return hora_minuto*60     
print(minuto_segundo(hora_minuto(dia_hora(dia))) )      


def dia_hora(dia):
    return dia*24
def hora_minuto(dia_hora):
    return dia_hora*60
def minuto_segundo(hora_minuto):
    return hora_minuto*60         
print(minuto_segundo(hora_minuto(dia_hora(2))))