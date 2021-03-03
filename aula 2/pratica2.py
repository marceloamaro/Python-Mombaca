print("s=solteiro e c=casado")
eu = input("Meu estado civil-->") 
pessoa02=input("Diga o seu estado civil da segunda pessoa--> ")


def match(eu, pessoa02):

    if eu == pessoa02 :
        return print("Bora")

    else:
        return print("Deixa quieto")

        
match(eu,pessoa02)