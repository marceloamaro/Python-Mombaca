"""
Escreva uma função para aprovar o empréstimo bancário para compra de uma casa. Essa função deve receber o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""
print('Calculo de emprestimo ')
valor_casa = float(input('Valor da casa:'))
salario = float(input('Salario:'))
anos = int(input('Anos a pagar:'))
meses = anos * 12
parcelas = valor_casa / meses
minimo = salario *(30/100)
def juros (parcelas, minimo):
    if parcelas < minimo:
        print('seu emprestimo foi aprovado.')
    else:
        print('emprestimo não foi aprovado,o valor das parcelas é maior que 30% do seu salário que é de',minimo)

print('')
print('O valor da casa dividido em', meses , 'meses é de:', parcelas,'por mes.')
print('')
x = juros (parcelas, minimo)