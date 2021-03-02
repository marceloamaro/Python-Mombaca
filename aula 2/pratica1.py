nome=str(input("informe um nome-> "))
idade=int(input("informe a idade-> "))
sexo=str(input("informe a inicial do seu sexo-> "))
estado_civil=str(input("informe a inicial do seu estado civil->"))

def nome_pessoa(nome):
    return nome

def idade_pessoa(idade):
    return idade

def sexo_pessoa(sexo):
    return sexo

def estado_pessoa(estado_civil):
    return estado_civil

print("seu nome é", nome_pessoa(nome))
print("sua idade é",idade_pessoa(idade))
print("Inicial do seu sexo é", sexo_pessoa(sexo))
print("Inicial do seu estado civil é", estado_pessoa(estado_civil))