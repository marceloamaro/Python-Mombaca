print("digite o valor do produto e categoria de 1 á 5")
print("categoria 1 5 porcento desconto")
print("categoria 2 7 porcento desconto")
print("categoria 3 10 porcento desconto")
print("categoria 4 15 porcento desconto")
print("categoria 5 20 porcento desconto")

produto=float(input("informe o valor do produto R$-> "))
categoria=int(input("informe a categoria-> "))

def resultado(produto, categoria):
    if categoria == 1:
        desconto = produto*(5/100)
        return produto - desconto
    elif categoria == 2:
        desconto = produto*(7/100)
        return produto - desconto
    elif categoria == 3:
        desconto = produto*(10/100)
        return produto - desconto
    elif categoria == 4:
        desconto = produto*(15/100)
        return produto - desconto
    elif categoria == 5:
        desconto = produto*(20/100)
        return produto - desconto
    else:
        return "invalido"
            

x = resultado(produto, categoria) 
print("R$", x)  