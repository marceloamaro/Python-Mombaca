"""Pesquise sobre a Cifra de Cézar e crie duas funções, uma para crifrar uma mensagem e outra para decifrar. Utilize como parâmetro a função da questão 6. """

print("Escolha entre ('criptografar', 'c') ou ('descriptografar', 'd')")
opcao = input("Deseja criptografar ou descriptografar? ")
opcao = opcao.lower()

   
def encripta(mensagem, chave):
    cripto = ''
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) + chave > ord('Z'):
                cripto += chr((ord('A') + chave - (ord('Z') + 1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        elif 'a' <= i <= 'z':
            if ord(i) + chave > ord('z'):
                cripto += chr((ord('a') + chave - (ord('z') + 1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        else:
            cripto += i   
                 
    return cripto

def descripta(mensagem, chave):
    cripto = ''
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) - chave < ord('A'):
                cripto += chr(ord('Z') - (chave - (ord(i) + 1 - ord('A'))))
            else:
                cripto += chr(ord(i) - chave)
        elif 'a' <= i <= 'z':
            if ord(i) - chave < ord('a'):
                cripto += chr(ord('z') - (chave - (ord(i) + 1 - ord('a'))))
            else:
                cripto += chr(ord(i) - chave)
        else:
            cripto += i
    return cripto

if opcao == 'c' or opcao == 'criptografar':
    print("Digite o valor da chave entre 1 e 26")
    chave = int(input("Digite o valor da chave: "))
    mensagem = input("Digite a mensagem: ")
    encripta(mensagem, chave)
    print(encripta(mensagem, chave))

elif opcao == 'd' or opcao == 'descriptografar':
    print("Digite o valor da chave entre 1 e 26")
    chave = int(input("Digite o valor da chave: "))
    mensagem = input("Digite a mensagem: ")    
    descripta(mensagem, chave)
    print(descripta(mensagem, chave))

else:
    print("opção invalida")    

    

