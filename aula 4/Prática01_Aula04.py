"""
Escreva uma função que receba o total de vendas 
de um funcionário no período de 1 mês e 
seu nome. Se o valor total de suas vendas for 
maior que a metade do salário, o funcionário
deve receber um adicional de 50%, caso não seja,
ele recebe apenas o salário bruto. Retorne quanto 
o funcionário irá receber no mês. O valor do salário 
deve estar armazenado em uma variável global e o 
nome do funcionário deve ser um parâmetro opcional.
"""
vendas = float(input("Total de vendas do funcionario no mês: "))
salario = 1100
def bonificacao(salario, vendas, nome = "marcelo" ): 
    if vendas > 550: 
        salario += 550
        print(f"O vendendor {nome}, seu salário do mês mas a bonificação é: R${salario}\n")
    else:
        print(f"O vendendor {nome}, voce nao atingiu a meta de vendas, seu salário do mês é: R${salario}")


bonificacao(salario, vendas) 