"""Escreva uma função que faça a verificação de existência de uma chave dentro de um dicionário. Caso a chave exista a função deve retornar o valor da chave, caso ela não exista, a função deve adicioná-la e retornar o dicionário."""

def verificacao(d, chave): 
      
    if chave in d:  
        print(" Chave existe o valor é =", d[chave]) 
    else: 
        print("nao presente") 
        #d[chave] = d.get(chave) 
        d[chave] = chave
        print(d)
        
 
d = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6} 
  
chave = input("digite o a chave para verificação:")
verificacao(d, chave) 
  

