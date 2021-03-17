"""traticas da aula"""
"""
set1 = set()
set1.add("Marcelo")
set1.add("Maria Julia")
set1.add("Aline")
print(set1)

set2 = {"Gabriel", "Maria", "Isabel", "Isadora"}
print(set2)

lista =["uva", "banana", "jaca"]
frutas = set(lista)
print(frutas)

set2 = {"Gabriel", "Maria", "Isabel", "Isadora"}
for i in set2:
    print(i)

aluno_uece = {"Amaro"}   
novos = ["moreira", "jonas"]
novatos = ("rafael", "vidal")
aluno_uece.update(novos, novatos)
print(aluno_uece)


lista = ["jaca", "uva"]
tupla = ("pera", "maça")
def conjunto (lista, tupla):
    tudo = set(tupla)
    tudo.update (lista)
    print(tudo)

conjunto(lista, tupla)

set2 = {"Gabriel", "Maria", "Isabel", "Isadora"}
set2.remove("Isabel")
set2.discard("paulo")
set2.pop()
set2.clear()
del set2
print(set2)

set1 ={1, 2, 3, 4}
set2 ={2, 3, 4, 5, 6, 7, 8}
#difernça
print(set1 - set2)
print(set2 - set1)
dif = set1.difference(set2)
print(dif)

# uniao

set1 ={1, 2, 3, 4}
set2 ={2, 3, 4, 5, 6, 7, 8}
print(set1 | set2)
uni = set1.union(set2)
print(uni)

# interseção
set1 ={1, 2, 3, 4}
set2 ={2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)

set1 ={1, 2, 3, 4}
set2 ={2, 3, 4, 5, 6, 7, 8}

def uni(set1, set2):
    print(set1 | set2)
    uni = set1.union(set2)
    print(uni)
   
uni(set1, set2) 

# dicionario
#dicio = {"chave": valor, "chave2":valor2, "chave3":valor3}

usuario_acesso = {
    "login":"adm",
    "senha": 123
}
print(usuario_acesso)
usuario_acesso["login"]= "marcelo"
print(usuario_acesso)

usuario_acesso = {
    "login":"adm",
    "senha": 123
}
v = usuario_acesso.get("login")
v2 = usuario_acesso["login"]
print(v)
print(v2)
v3 = usuario_acesso.keys()
print(v3)
v4 = usuario_acesso.values()
print(v4)
v5 = usuario_acesso.items()
print(v5)

usuario_acesso = {
    "login":"adm",
    "senha": 123
}
if "senha" in usuario_acesso:
    print("existe")
else:
    print("nao")    

terra = {"alien" : "binladen", "planeta" : "marciano"}
def esta_entre_nos (dicio, chave):
    if chave in terra:
        print(f'Existe {chave} com o valor  {dicio[chave]}')
    else:
        terra[chave] = "binladen"

esta_entre_nos(terra, "alien")

a = {x: x for x in range(0,10)}
print(a)
#a = {x: x/2 for x in range(0,10)}
#print(a)
#a = {x: x//2 for x in range(0,10)}
#print(a)
#a = {x: x**2 for x in range(0,10)}
#print(a)
#for i in a.keys():
    #print(i)
#for i in a.values():
    #print(i)    
for i in a.values():
    if i %2 == 0:
        print(i)
"""
a = {x: x*3 for x in range(0,100,2)}
print(a)
