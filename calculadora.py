operação = input('''
Digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

num1 = int(input('Digite seu primeiro número: '))
num2 = int(input('Digite seu segundo número: '))

if operação == '+':
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)

elif operação == '-':
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)

elif operação == '*':
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)

elif operação == '/':
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)

else:
    print('Você não digitou um operador válido, execute o programa novamente.')