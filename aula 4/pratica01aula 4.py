"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
"""
print("calcula perimetro do triangulo")
lado1 = int(input('Digite o valor do lado 1 do triãngulo: '))
lado2 = int(input('Digite o valor do lado 2 do triãngulo: '))
lado3 = 35

def perimetro(lado1, lado2, lado3):
    return(lado1 + lado2 + lado3)

print("O perimetro do triãngulo é:", perimetro(lado1, lado2, lado3))
"""
"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
"""
print("calcula perimetro do triangulo")
lado1 = int(input('Digite o valor do lado 1 do triãngulo: '))
lado2 = int(input('Digite o valor do lado 2 do triãngulo: '))

def perimetro(lado1, lado2, lado3 = 35):
    return(lado1 + lado2 + lado3)

print("O perimetro do triãngulo é:", perimetro(lado1, lado2))
"""
"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
"""
print("calcula perimetro do triangulo")
lado1 = int(input('Digite o valor do lado 1 do triãngulo: '))
lado2 = int(input('Digite o valor do lado 2 do triãngulo: '))
lado3 = 35

def perimetro(lado1, lado2, lado3):
    return(lado1 + lado2 + lado3)

print("O perimetro do triãngulo é:", perimetro(lado1, lado2, lado3))
"""
"""
Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área
e perímetro
"""
"""
print("calcula perimetro do triangulo")


def perimetro(lado1, lado2, lado3 ):
    return(lado1 + lado2 + lado3)

print("O perimetro do triãngulo é:", perimetro(lado2 = 2, lado3 = 3,lado1 = 5 ))
"""
"""
def perimetro(d, b, c = 4):
    return d + c + b

def imprimi(perimetro):
    print(f'{perimetro}')

imprimi(perimetro(2, 4, 6))
"""
p = lambda a, b, c : print(a+b+c)
a = 1
b = 2
c = 3
p(a,b,c)