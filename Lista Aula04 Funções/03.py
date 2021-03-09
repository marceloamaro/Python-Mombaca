"""Escreva um função que receba sua idade, sua profissão e comormidade = False, altere o valor deste último parâmetro na chamada da função, caso necessário. Essa função deve retornar "Hápto" se você estiver dentro do grupo prioritário para receber a primeira dose da vacina."""
print(" exemplo de profissão saude, indigena, professor")
print("policial, pedreiro,sistema prisional, outros ")
profissão = str(input("Digite seu profissão:"))   
idade = int(input("digite sua idade:"))
print("Se tiver uma comorbidades digite sim, se nao dê enter")
comorbidades = str(input("se tiver alguma comorbidade: "))

def vacina(profissão, idade, comorbidades = "nao"):
    if profissão == "saude" or profissão == "indigena" or idade >= 75:
        return "Hápto fase 1"
    elif idade >= 60:
        return "Hápto fase 2"
    elif comorbidades == "sim":
        return "Hápto fase 3"
    elif profissão == "professor" or profissão == "policial" or profissão == "sistema prisional" :
        return "Hápto fase 4"
    else:
        return "Use mascara, sua fase de vacinação ainda nao foi liberada"

x = vacina(profissão, idade, comorbidades )
print(x)