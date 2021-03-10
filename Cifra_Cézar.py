def recebeModo():
    """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """

    while True:
        option = input("Deseja criptografar ou descriptografar? ")
        option = option.lower()
        if option == 'c' or option == 'criptografar' or option == 'descriptografar' or option == 'd':
            return option
        print("Entrada inválida. Escolha entre ('criptografar', 'c') ou ('descriptografar', 'd')")

def recebeChave():
    """
    Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado
    """
    while True:
        chave = int(input("Digite o valor da chave: "))
        if 1 <= chave <= 26:
            break
        print("Entrada inválida")

    return chave

def geraMsgTraduzida(modo, mensagem, chave):
    """
    Traduz a mensagem do usuário de modo conveniente
    """
    cripto = ''

    if modo == 'c' or modo == 'criptografar':
        for i in mensagem:
            if 'A' <= i <= 'Z':
                if ord(i) + chave > ord('Z'):
                    cripto += chr((ord('A') + chave - (ord('Z')+1 - ord(i))))
                else:
                    cripto += chr(ord(i) + chave)


            elif 'a' <= i <= 'z':
                if ord(i) + chave > ord('z'):
                    cripto += chr((ord('a') + chave - (ord('z')+1 - ord(i))))
                else:
                    cripto += chr(ord(i) + chave)
            else:
                cripto += i

    elif modo == 'd' or modo == 'descriptografar':
        for i in mensagem:
            if 'A' <= i <= 'Z':
                if ord(i) - chave < ord('A'):
                    cripto += chr(ord('Z') - (chave - (ord(i)+1 - ord('A'))))

                else:
                    cripto += chr(ord(i) - chave)


            elif 'a' <= i <= 'z':
                if ord(i) - chave < ord('a'):
                    cripto += chr(ord('z') - (chave - (ord(i)+1 - ord('a'))))
                else:
                    cripto += chr(ord(i) - chave)
            else:
                cripto += i 

    return cripto

def main():
    """
    Função principal do programa
    """

    modo = recebeModo()
    chave = recebeChave()
    mensagem = input("Digite a mensagem: ")
    print(geraMsgTraduzida(modo, mensagem, chave))

main()