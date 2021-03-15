"""
lista = [1, 2 , "maju", True, 3.75]

def função(lista, novo):
    lista[2] = novo    
    print(lista)

função(lista, "Maria Julia")

lista2 = ["r", "s", "t", "m"]
print(lista2[0:3])(
print(lista2[:3])
print(lista2[0:])
print(lista2[:])
print(lista2[0:3:2])
print(lista2[::-1])

lista1 = [1, 2 , "maju", True, 3.75]

def corte(lista):
    return(lista)

def fatiamento(corte, n1, n2, n3):
    print(f'''
        {corte[n1:n2]}
        {corte[n3:]}
        {corte[:n2]}
        ''')

fatiamento(corte(lista1), 2, 4, 1)

lista1 = [1, 2 , "maju", True, 3.75]
for i in lista1:
    print(i)

i = 0
while i < len(lista1):
    print(lista1[i])
    i +=1

 
 nova_lista =[x for x in range(0, 100)]
 print(nova_lista)   

impares = []
for i in range(10, 20):
    if i % 2 != 0:
        impares.append(i) 
print("IMPARES:",impares)

impares = [x for x in range(1,10) if x % 2 != 0]
print(impares)

impares = [x - 1 for x in range(1,1000) if x % 2 != 0 and x <500]
print(impares)


numeros = [1, 5, 7, 9, 11, 15]
nova = [x for x in numeros if x < 10]
print(nova)

lista2 = [0, 1, 2, 3, 4, 5]

nova_lista = [x - 1 for x in lista2]
print (nova_lista)

"""
lista1 = [1, 2 , "maju", 2021, 3.75]
t_lista1 = tuple(lista1)
print(t_lista1)
l_lista1 = list(t_lista1)
l_lista1.append('marcelo')
t_lista1 = tuple(l_lista1)
print(t_lista1)