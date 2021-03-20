"""Escreva uma função que receba um dicionário composto por 2 chaves(login e senha), essas chaves devem possuir seus respectivos valores. A função deve receber além do dicionário, dois possiveis valores para as duas chaves, dentro da função deve ser feita uma verificação que irá retornar "Acesso concedido" se o valor de login e senha do dicionário forem iguais aos que foram passados no chamado da função. Para ficar mais interessante, receba o login e senha do usuário através do input. """
usuario_acesso = {
    'login':'maju',
    'senha':'maju123'
}

login = input("Digite seu usuario-->")
senha = input("Digite sua senha-->")

def checar_acesso(usuario_acesso,login,senha):
    if login == 'maju' and senha == 'maju123':
        print("Acesso concedido")
    else:
        print("Acesso negado")

checar_acesso(usuario_acesso,login, senha)        


verifica_chave(usuario_acesso,chave)

  


