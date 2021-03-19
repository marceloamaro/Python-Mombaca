"""Faça uma função que retorne uma das três operações básicas entre sets: *A função deve receber dois conjuntos que terão intens adicionados manualmente pelo usuário *A operação que será retornada também será escolhida pelo usuário"""
lista = []
lista2 = []

entrada1 = input("\nDigite valores para lista 1:\n ")
lista.append(entrada1)
#print(lista)
set1 = set(lista)
entrada2 = input("\nDigite valores para lista 2: \n")
lista2.append(entrada2)
#print(lista2)
set2 = set(lista2)
print("d = Diferença , u = União ou i = Intesecção")
op = str(input("digite a operação do set-->"))
def opcao(set1, set2, op):
    if op == "d":
        return (set1  - set2)
    elif op == "u":
        return (set1  | set2)
    elif op == "i":
        return (set1.intersection(set2))
    else:
        return "invalido, informe d = Diferença , u = União ou i = Intesecção"

x = opcao(set1, set2, op)
print(x)

    