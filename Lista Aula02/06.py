"""
Suponha que o preço de cada  um livro seja 24.95 mas as livrarias recebem um desconto
de 40%. O transporte custa 3.00 para o primeiro exemplar e 75 centavos para cada exemplar
adicional. Qual é o custo total de atacado para 60 copias?
"""

q_livro = 60

def custo(q_livro):  
    return ((24.95*(40/100))*q_livro)+(((q_livro - 1)*0.75)+3)
    

print("o custo total para 60 unidades sao: R$", custo(q_livro))
   