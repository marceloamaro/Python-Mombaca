input = input('Escreva qualquer coisa: ')
input = input.lower()
output = []
for caracteres in input:
    numero = ord(caracteres) - 96
    output.append(numero)
print (output)