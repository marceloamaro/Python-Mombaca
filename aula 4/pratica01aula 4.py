"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
print("calcula perimetro do triangulo")
lado1 = int(input('Digite o valor do lado 1 do triãngulo: '))
lado2 = int(input('Digite o valor do lado 2 do triãngulo: '))
lado3 = 35

def perimetro(lado1, lado2, lado3):
    return(lado1 + lado2 + lado3)

print("O perimetro do triãngulo é:", perimetro(lado1, lado2, lado3))