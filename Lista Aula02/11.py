"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
print("calcula area do triangulo")
altura = int(input('Digite a altura do triãngulo: '))
base = int(input('Digite a base do triãngulo: '))
print("calcula perimetro do triangulo")
lado1 = int(input('Digite o valor do lado 1 do triãngulo: '))
lado2 = int(input('Digite o valor do lado 2 do triãngulo: '))
lado3 = int(input('Digite o valor do lado 3 do triãngulo: '))


def area (base, altura):
    return (base * altura)/2

def perimetro(lado1, lado2, lado3):
    return(lado1 + lado2 + lado3)

print("A área do triãngulo é:", area (base, altura))
print("O perimetro do triãngulo é:", perimetro(lado1, lado2, lado3))