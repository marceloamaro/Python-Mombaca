"""
11-​ Faça uma função que receba como argumento o salário de um funcionário e
calcule o valor do aumento com base nos dados abaixo.
- Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%
- Para os inferiores a R $1.250,00 e superiores a R $1.000,00, 15% de aumento.
- Para os inferiores a R $1.000,00 e superiores a R $500,00, 20% de aumento.
- Para os inferiores a R $500,00, 25% de aumento.
"""
print("Valores base de 500, 1000, 1250 não poder ser informado")
salario = float(input("Informe o valor do seu salario para calcula o valor do aumento-->")) 

def aumento(salario):
    if salario > 1250:
        reajuste = salario*(10/100)
        return salario + reajuste
    elif salario < 1250 and salario > 1000:
        reajuste = salario*(15/100)
        return salario + reajuste
    elif salario < 1000 and salario > 500:
        reajuste = salario*(20/100)
        return salario + reajuste
    elif salario < 500:    
        reajuste = salario*(25/100)
        return salario + reajuste
        
x = aumento(salario) 
print("o Valor do seu salario é de R${:.2f}!".format(x) ) 