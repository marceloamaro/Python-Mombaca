"""
Esreva uma função que receba a medida do raio e calcule a área e perímetro de uma
circuferência.
"""
print("calcula perimetro do circuferencia")
raio = float(input('Entre com o valor do raio, para obter o perimetro do círculo: '))
print("calcula area da circuferencia")
raio2 = float(input('Entre com o valor do raio, para obter a area do círculo: '))

def perimetro (raio):
    return 2 * 3.14 * raio

def area(raio2):
    return(3.14 *(raio2)**2)









print("O perimetro da circuferncia é:", perimetro (raio))
print("A area do da circuferncia é:", area(raio2))