"""
Faça uma função que receba como argumento o salário de um funcionário e calcule o valor do aumento com base nos dados abaixo.
    • Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%
    • Para os inferiores ou iguais, 15% de aumento.
    """
salario = float(input("Informe o valor do seu salario para calcula o valor do aumento-->")) 

def aumento(salario):
    if salario > 1250:
        reajuste = salario*(10/100)
        return salario + reajuste
    else: #salario <= 1250:
        reajuste = salario*(15/100)
        return salario + reajuste

x = aumento(salario) 
print("o Valor do seu salario é de R${:.2f}!".format(x) ) 