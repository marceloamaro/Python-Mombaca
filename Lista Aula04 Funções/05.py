"""Escreva uma função para validar uma string. Ela deve receber como argumento, uma string, o número minimo e máximo de caracteres e retornar VERDADEIRO se o número de caracteres da string estiver dentro do min e max passado, e FALSO caso contrário. """

nome = str(input("digite uma string:"))

def validar(nome):
    max = 20 # Numero Maximo de caracteres Permitidos.
    min = 4  # Numero Minimo de caracteres Permitidos.
    if len(nome) <= max and len(nome) >= min:
        return True
    else:
        return False

x = validar(nome)
print(x)
