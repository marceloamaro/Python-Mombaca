"""
Crie uma função que resolva a seguinte equação do segundo grau X2 + 3x +3 = 0 . Dica
para calcular a raiz quadrada -> num ** 0.5
""" 
# 1 5 6/ 4 4 1
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

def raiz(a, b, c):
    delta = (b**2 - 4*a*c)
    print("o valor de delta é:", delta)
    if delta < 0:
        print("A equação não possui raizes reais.")
    elif delta == 0:
        raiz = (-1*b + (delta** 0.5))/(2 * a)
        print("A equacao possui apenas uma raiz que e ",raiz)
    elif delta > 0:
        x1 =(-1*b + (delta** 0.5))/(2 * a)
        x2 =(+1*b + (delta** 0.5))/(2 * a)
        print("O x1", x1)
        print("O x2", x2)
    return
raiz(a, b, c)    